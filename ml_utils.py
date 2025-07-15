from io import BytesIO
from fastapi.responses import StreamingResponse
import os
import numpy as np
from tensorflow.keras.models import load_model  # type: ignore
from sklearn.preprocessing import MinMaxScaler
import joblib

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for server environment

import matplotlib.pyplot as plt


#BASE_MODEL_PATH = r"E:\Documents\occupancy-dashboard\occupancy_backend\models"  # your folder where models and scalers are saved

BASE_MODEL_PATH = r"E:\dashboard\occupancy_backend\models"


def get_model_components(room_type):
    model_path = os.path.join(BASE_MODEL_PATH, f"autoencoder_{room_type}_static.h5")
    threshold_path = os.path.join(BASE_MODEL_PATH, f"threshold_{room_type}_static.npy")
    scaler_path = os.path.join(BASE_MODEL_PATH, f"scaler_{room_type}_static.save")

    model = load_model(model_path, compile=False)
    threshold = np.load(threshold_path).item()
    scaler = joblib.load(scaler_path)

    return model, threshold, scaler


def predict_occupancy(model, threshold, scaler, raw_data):
    if len(raw_data.shape) == 1:
        raw_data = raw_data.reshape(-1, 1)

    data_scaled = scaler.transform(raw_data)
    reconstructed = model.predict(data_scaled)
    error = np.mean(np.abs(data_scaled - reconstructed), axis=1)

    predictions = error > threshold
    occupied_count = int(np.sum(predictions))
    total = len(predictions)
    occupancy_ratio = occupied_count / total
    room_status = "Occupied" if occupancy_ratio > 0.4 else "Unoccupied"

    return {
        "status": room_status,
        "occupied_count": occupied_count,
        "total": total,
        "mean_error": float(np.mean(error)),
        "threshold": float(threshold),
        "errors": error.tolist()
    }

def evaluate_dynamic_file(file_path, model, threshold, scaler):
    data = np.load(file_path)
    result = predict_occupancy(model, threshold, scaler, data)
    return result





def create_plot_image(errors, threshold):
    errors = np.array(errors)
    fig, axs = plt.subplots(2, 1, figsize=(12, 8))

    axs[0].hist(errors, bins=100, alpha=0.7, color='skyblue', label='Reconstruction Errors')
    axs[0].axvline(threshold, color='red', linestyle='--', label=f'Threshold = {threshold:.4f}')
    axs[0].set_title('📊 Histogram of Reconstruction Errors')
    axs[0].set_xlabel('Reconstruction Error')
    axs[0].set_ylabel('Frequency')
    axs[0].legend()
    axs[0].grid(True)

    axs[1].plot(errors, color='orange', label='Reconstruction Error')
    axs[1].axhline(threshold, color='red', linestyle='--', label='Threshold')
    axs[1].set_title('🕒 Reconstruction Error Over Time')
    axs[1].set_xlabel('Sample Index')
    axs[1].set_ylabel('Reconstruction Error')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf



