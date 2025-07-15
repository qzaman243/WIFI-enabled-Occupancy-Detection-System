# import os
# import numpy as np
# import pywt  
# from sklearn.decomposition import PCA
# import interleaved as decoder

# # Constants
# C = 3e8  # Speed of light (m/s)
# fc = 2.4e9  # WiFi frequency (Hz)
# fd_max = 80  # Max Doppler frequency (Hz)
# sampling_rate = 1000  # CSI sample rate
# window_size = 50
# subcarrier_count = 44
# wavelet = 'db4'

# # Derived wavelet level
# dwt_level = int(np.floor(np.log2(sampling_rate / (2 * fd_max))))

# # File paths
# data_folders = r"E:\Documents\occupancy-dashboard\pcapfiles"
# output_dir = r"E:\Documents\occupancy-dashboard\npyfiles"
# os.makedirs(output_dir, exist_ok=True)

# def process_all_pcap_files(folder_path):
#     for filename in os.listdir(folder_path):
#         if filename.endswith(".pcap"):
#             scenario = os.path.splitext(filename)[0]
#             file_path = os.path.join(folder_path, filename)
#             process_single_pcap(file_path, scenario)

# def process_single_pcap(file_path, scenario):
#     print(f"Processing: {file_path}")
#     samples = decoder.read_pcap(file_path)
#     pc1_values = []
#     csi_magnitude_data = []

#     for i in range(samples.nsamples):
#         csi = samples.get_csi(index=i, rm_nulls=True, rm_pilots=True)
#         csi_magnitude = np.abs(csi[:subcarrier_count])

#         coeffs = pywt.wavedec(csi_magnitude, wavelet, level=dwt_level)
#         threshold = np.std(coeffs[-1]) * 0.4
#         coeffs_filtered = [pywt.threshold(c, threshold, mode='soft') for c in coeffs]
#         filtered_csi = pywt.waverec(coeffs_filtered, wavelet)[:subcarrier_count]

#         csi_magnitude_data.append(filtered_csi)

#     csi_magnitude_data = np.array(csi_magnitude_data)

#     for i in range(len(csi_magnitude_data) - window_size):
#         window_data = csi_magnitude_data[i : i + window_size]
#         pca = PCA(n_components=1)
#         pc1 = pca.fit_transform(window_data)
#         #pc1_values.append(pca.mean())
#         pc1_values.append(pca.explained_variance_ratio_[0])

#     pc1_data = np.array(pc1_values)
#     output_path = os.path.join(output_dir, f"{scenario}.npy")
#     np.save(output_path, pc1_data)
#     print(f"Saved to: {output_path}")


# def process_pcap_folder(folder_path, scenario):
#     file_path = os.path.join(folder_path, f"{scenario}.pcap")
#     process_single_pcap(file_path, scenario)
#     return os.path.join(output_dir, f"{scenario}.npy")



import os
import numpy as np
import pywt  
from sklearn.decomposition import PCA
import interleaved as decoder

# Constants
C = 3e8  # Speed of light (m/s)
fc = 2.4e9  # WiFi frequency (Hz)
fd_max = 80  # Max Doppler frequency (Hz)
sampling_rate = 1000  # CSI sample rate
window_size = 50
subcarrier_count = 44
wavelet = 'db4'

# Derived wavelet level
dwt_level = int(np.floor(np.log2(sampling_rate / (2 * fd_max))))

# File paths
pcap_folder = r"E:\dashboard\pcapfiles"
npy_output_folder = r"E:\dashboard\npyfiles"
os.makedirs(npy_output_folder, exist_ok=True)

def process_single_pcap(file_path):
    print(f"Processing: {file_path}")
    samples = decoder.read_pcap(file_path)
    pc1_values = []
    csi_magnitude_data = []

    for i in range(samples.nsamples):
        csi = samples.get_csi(index=i, rm_nulls=True, rm_pilots=True)
        csi_magnitude = np.abs(csi[:subcarrier_count])

        coeffs = pywt.wavedec(csi_magnitude, wavelet, level=dwt_level)
        threshold = np.std(coeffs[-1]) * 0.4
        coeffs_filtered = [pywt.threshold(c, threshold, mode='soft') for c in coeffs]
        filtered_csi = pywt.waverec(coeffs_filtered, wavelet)[:subcarrier_count]

        csi_magnitude_data.append(filtered_csi)

    csi_magnitude_data = np.array(csi_magnitude_data)

    for i in range(len(csi_magnitude_data) - window_size):
        window_data = csi_magnitude_data[i : i + window_size]
        pca = PCA(n_components=1)
        pc1 = pca.fit_transform(window_data)
        pc1_values.append(pca.explained_variance_ratio_[0])

    return np.array(pc1_values)

def process_all_pcap_files(folder_path):
    all_pc1_data = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".pcap"):
            file_path = os.path.join(folder_path, filename)
            pc1_data = process_single_pcap(file_path)
            all_pc1_data.extend(pc1_data)  # Append data to the final list

    # Combine all into one NumPy array
    all_pc1_data = np.array(all_pc1_data)
    
    # Save to a single file
    output_path = os.path.join(npy_output_folder, "combined_data.npy")
    np.save(output_path, all_pc1_data)
    print(f"\n✅ All files processed. Combined data saved to:\n{output_path}")

# Run the processing
process_all_pcap_files(pcap_folder)
