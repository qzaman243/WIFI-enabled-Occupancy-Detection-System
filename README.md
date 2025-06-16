# WiFi-Enabled Occupancy Detection System Using CSI

This repository contains the complete implementation of my Final Year Project (FYP) titled **"WiFi-Enabled Occupancy Detection System Using Channel State Information (CSI)"**, conducted at the **National University of Sciences and Technology (NUST), Islamabad**. The project uses passive WiFi sensing for occupancy detection by analyzing fine-grained CSI data from a Raspberry Pi 4.

---

## 📄 Abstract

This project explores a privacy-preserving and device-free approach to human occupancy detection using WiFi signals. Leveraging the **Broadcom BCM43455c0 chipset** on a **Raspberry Pi 4**, the system captures fine-grained Channel State Information (CSI) using the **Nexmon CSI toolchain**. Variations in CSI, induced by human motion or presence, are analyzed to determine occupancy status in indoor environments without the use of cameras or wearable devices.

The CSI data is processed using signal enhancement techniques including **Discrete Wavelet Transform (DWT)** and **Kalman Filtering** to reduce noise and extract meaningful features. These features are then used to train machine learning models for accurate occupancy classification. Development was carried out using **Python** for data handling and machine learning, and **MATLAB** for signal analysis and visualization.

This project demonstrates the viability of WiFi-based sensing as a low-cost, scalable, and non-invasive solution for smart environments, with applications in energy optimization, surveillance, and space utilization.

---

## 📁 Project Structure

```text
wifi-occupancy-csi/
│
├── data/                  # Raw and preprocessed CSI files (PCAP/CSV)
├── scripts/
│   ├── extract_csi.py     # Script to convert PCAP files to CSV
│   ├── preprocess.py      # DWT, Kalman filtering, denoising
│   ├── features.py        # Feature extraction from CSI
│   └── train_model.py     # Training ML classifier
│
├── matlab/                # MATLAB signal analysis files
├── models/                # Saved models (.pkl, .h5, etc.)
├── utils/                 # Helper functions and tools
├── tests/                 # Unit tests
│
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── .gitignore             # Files to ignore in version control
└── LICENSE                # Open-source license


---
**
# Create Python Virtual Environment (Optional)**
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
