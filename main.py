from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import os
import shutil
import glob
from datetime import datetime

from ml_utils import get_model_components, evaluate_dynamic_file, create_plot_image
from preprocessing import process_all_pcap_files  # updated import

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/plot-reconstruction-errors")
def get_plot():
    # Dummy input – replace with real data
    errors = [0.01, 0.02, 0.03, 0.1, 0.5, 0.6]
    threshold = 0.2

    img_buffer = create_plot_image(errors, threshold)
    return StreamingResponse(img_buffer, media_type="image/png")


# @app.post("/preprocess-and-predict")
# async def preprocess_and_predict(room_type: str = Query(..., enum=["small", "large"])):
#     try:
#         # Paths
#         pcap_folder = r"E:\Documents\occupancy-dashboard\pcapfiles"
#         npy_output_folder = r"E:\Documents\occupancy-dashboard\npyfiles"
#         combined_npy_path = os.path.join(npy_output_folder, "combined_data.npy")

#         # Cleanup old npy files
#         for f in glob.glob(f"{npy_output_folder}/*.npy"):
#             os.remove(f)

#         # Preprocess all pcap files → creates one combined_data.npy
#         process_all_pcap_files(pcap_folder)

#         if not os.path.exists(combined_npy_path):
#             raise Exception("Combined .npy file was not created.")

#         # Load model, threshold, and scaler based on room type
#         model, threshold, scaler = get_model_components(room_type)

#         # Run prediction on the combined .npy file
#         prediction_result = evaluate_dynamic_file(combined_npy_path, model, threshold, scaler)

#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         return {
#             "results": [{
#                 "file": "combined_data.npy",
#                 "prediction": prediction_result,
#                 "timestamp": timestamp
#             }]
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Preprocess and predict failed: {str(e)}")

@app.post("/preprocess-and-predict")
async def preprocess_and_predict(room_type: str = Query(..., enum=["small", "large"])):
    try:
        # Paths
        pcap_folder = r"E:\dashboard\pcapfiles"
        npy_output_folder = r"E:\dashboard\npyfiles"
        combined_npy_path = os.path.join(npy_output_folder, "combined_data.npy")

        # Check if .npy file exists and is up to date
        should_preprocess = True
        if os.path.exists(combined_npy_path):
            npy_mtime = os.path.getmtime(combined_npy_path)
            for pcap_file in glob.glob(os.path.join(pcap_folder, "*.pcap")):
                if os.path.getmtime(pcap_file) > npy_mtime:
                    should_preprocess = True
                    break
            else:
                should_preprocess = False  # No pcap is newer than .npy

        # If required, preprocess all .pcap files into one .npy
        if should_preprocess:
            process_all_pcap_files(pcap_folder)
            if not os.path.exists(combined_npy_path):
                raise Exception("Combined .npy file was not created.")
        else:
            print("✔️ Skipping preprocessing — using existing combined_data.npy")

        # Load model, threshold, and scaler based on room type
        model, threshold, scaler = get_model_components(room_type)

        # Run prediction on the combined .npy file
        prediction_result = evaluate_dynamic_file(combined_npy_path, model, threshold, scaler)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "results": [{
                "file": "combined_data.npy",
                "prediction": prediction_result,
                "timestamp": timestamp
            }]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Preprocess and predict failed: {str(e)}")


