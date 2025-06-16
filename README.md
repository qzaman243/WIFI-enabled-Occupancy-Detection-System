
# 📶 WiFi-Enabled Occupancy Detection using CSI
This repository contains the complete implementation of my Final Year Project (FYP) titled **"WiFi-Enabled Occupancy Detection System Using Channel State Information (CSI)"**, conducted at the **National University of Sciences and Technology (NUST), Islamabad**. The project uses passive WiFi sensing for occupancy detection by analyzing fine-grained CSI data from a Raspberry Pi 4.
This project uses **Channel State Information (CSI)** extracted via Nexmon on Raspberry Pi 4 to detect human occupancy in indoor environments. A combination of signal processing (DWT) and machine learning (Random Forest, SVM, Logistic Regression) is applied to classify occupancy status.

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

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/wifi-occupancy-csi.git
cd wifi-occupancy-csi
```
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/wifi-occupancy-csi.git![Screenshot (1006)](https://github.com/user-attachments/assets/644cad89-d669-46bb-9568-7bd911fdbdb8)

cd wifi-occupancy-csi
### 2. Create Python Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. MATLAB (Optional)
Use the files in the `matlab/` directory for signal analysis.  
Ensure MATLAB **Wavelet Toolbox** and **Signal Processing Toolbox** are installed.

---

## 🚀 Usage

### 1. Extract CSI from PCAP files
```bash
python scripts/extract_csi.py --input data/raw/yourfile.pcap --output data/processed/yourfile.csv
```

### 2. Preprocess CSI (DWT + Kalman Filter)
```bash
python scripts/preprocess.py --input data/processed/yourfile.csv --output data/cleaned/yourfile_cleaned.csv
```

### 3. Feature Extraction
```bash
python scripts/features.py --input data/cleaned/yourfile_cleaned.csv --output data/features/yourfile_features.csv
```

### 4. Train Model
```bash
python scripts/train_model.py --data data/features/ --model models/occupancy_model.pkl
```

---

## 🧠 Machine Learning Pipeline

- **📡 Data Collection**  
  CSI packets are captured using the Nexmon CSI tool on a Raspberry Pi 4 (bcm43455c0 chip).

- **🧼 Preprocessing**  
  - Denoising with **Discrete Wavelet Transform (DWT)**  
  - Smoothing with **Kalman Filter**

- **🛠️ Feature Engineering**  
  Temporal and statistical features extracted from amplitude and phase of CSI.

- **🤖 Classification**  
  Models: **Random Forest**, **SVM**, **Logistic Regression**  
  Task: **Binary classification** — `Occupied` vs `Not Occupied`

- **📊 Evaluation Metrics**  
  Accuracy, Precision, Recall, Confusion Matrix

---

## 📸 Visuals

<p align="center">
  <img src="  ![Uploading Screenshot (1006).png…]()
       " alt="System Architecture" width="500"/>
  <br>
  <em>Figure: System Architecture Overview</em>
</p>

---

## 👨‍💻 Author

**Qamar Zaman**  
Final Year Student, B.E. Computer Engineering  
**National University of Sciences and Technology (NUST), Islamabad**  
📧 Email: zqamar243463@gmail.come

---

## 🧾 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.








