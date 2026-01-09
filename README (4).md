# 🔫 Weapon Detection System (Real-Time)

A real-time weapon detection system built using YOLOv5, OpenCV, and PyTorch.

The system detects weapons such as guns and knives from a live camera feed and can be extended for surveillance and security applications.

## 🚀 Features
- 🎥 Real-time weapon detection using webcam / IP camera
- 🧠 Deep Learning–based object detection (YOLOv5)
- ⚡ Fast inference with PyTorch
- 📦 Lightweight and modular codebase
- 🔒 Suitable for surveillance & safety systems

## 🛠️ Tech Stack
- Python
- PyTorch
- YOLOv5
- OpenCV
- Computer Vision

## 📂 Project Structure

Weapon-Detection-System/

│

├── final_live.py        # Main script for real-time detection

├── requirements.txt     # Python dependencies

├── .gitignore           # Ignored files & folders

├── README.md            # Project documentation

└── weights/

    └── best_weapon.pt   # (Not included – download separately)
    
## 📦 Model Weights
The trained YOLOv5 model (best_weapon.pt) is not included in this repository due to GitHub file size limits.

## 🔽 Download Model Weights

The repository **excludes the model file** due to GitHub file size limits.

### 👉 Download the trained YOLOv5 weights here:  
🔗 https://drive.google.com/file/d/1xUckP056SLF14MkdGqXUWTacxH-FFW9r/view?usp=drive_link

### After downloading save the file as::

Weapon-Detection-System/

└── weights/

          └── best_weapon.pt

## ⚙️ Installation & Setup
### 1️⃣ Clone the Repository
git clone https://github.com/gowthamx25/Weapon-Detection-System.git

cd Weapon-Detection-System

### 2️⃣ Create Virtual Environment
python -m venv .venv

.venv\Scripts\activate   # Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### ▶️ Run the Application
python final_live.py


Press Q to exit the live detection window.

### 📸 Detection Output

- Bounding boxes around detected weapons
- Class labels (e.g., gun, knife)
- Confidence scores

### ⚠️ Disclaimer

This project is for educational and research purposes only.
It should not be solely relied upon for real-world security decisions without proper validation and legal approval.

## 📌 Future Enhancements
- 🔊 Audio alerts on weapon detection
- 📹 CCTV / IP camera integration
- ☁️ Cloud-based monitoring dashboard
- 🧠 Improved model accuracy with custom datasets
- 📱 Mobile & edge deployment (Jetson / Raspberry Pi)

### 👤 Author
Gowtham S

AI & Computer Vision Enthusiast

GitHub: https://github.com/gowthamx25

### ⭐ Support

If you find this project useful:

⭐ Star the repository

🍴 Fork it

🧠 Contribute improvements
