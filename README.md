# 🌿 Plant Disease Detection System

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-DeepLearning-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

> An AI-powered image classification system that detects plant diseases from leaf images using Deep Learning techniques.

---

## 🧠 Project Overview

Plant diseases significantly impact agricultural productivity and food security.  
This project leverages **Convolutional Neural Networks (CNNs)** to automatically classify plant leaf diseases from images, enabling early detection and preventive action.

The system can:
- Identify multiple plant diseases
- Differentiate healthy vs infected leaves
- Provide prediction confidence
- Be extended for real-time agricultural monitoring

---

## 🚀 Key Features

✔ Deep Learning based image classification  
✔ High accuracy disease detection  
✔ Easy-to-use interface (CLI / Web if included)  
✔ Model training and evaluation support  
✔ Clean and modular project structure  
✔ Ready for deployment  

---

## 🛠 Tech Stack

- **Programming Language:** Python  
- **Deep Learning Framework:** TensorFlow / Keras  
- **Image Processing:** OpenCV / PIL  
- **Data Handling:** NumPy, Pandas  
- **Visualization:** Matplotlib  
- **Web Framework (Optional):** Flask  

---

## 📂 Project Structure

```
Plant_Disease_Final_Project/
│
├── dataset/                # Training and testing images
├── models/                 # Saved trained models
├── notebooks/              # Jupyter notebooks (EDA & training)
├── src/                    # Core source code
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── app.py                  # Main application file (if Flask UI)
├── requirements.txt        # Dependencies
├── .gitignore              # Ignored files
└── README.md               # Documentation
```

---

## ⚙ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/NayanaBhagat28/plant-disease-detection.git
cd plant-disease-detection
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Environment

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### If using Flask Web App:

```bash
python app.py
```

Open browser at:
```
http://127.0.0.1:5000
```

### If using CLI Prediction:

```bash
python predict.py --image path_to_image.jpg
```

---

## 🧪 Model Training

To retrain the model:

```bash
python train.py --data_dir dataset/
```

Model will be saved inside:
```
models/
```

---

## 📊 Sample Results

| Disease Class       | Accuracy |
|--------------------|----------|
| Healthy            | 98%      |
| Early Blight       | 95%      |
| Late Blight        | 94%      |
| Bacterial Spot     | 93%      |

*(Replace with your actual results)*

---

## 📈 Future Improvements

- Add real-time camera detection
- Deploy as a cloud web application
- Mobile application integration
- Increase dataset diversity
- Improve model generalization

---

## 🤝 Contribution Guidelines

Contributions are welcome!

1. Fork the repository  
2. Create a feature branch  
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes  
   ```bash
   git commit -m "Added new feature"
   ```
4. Push to GitHub  
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request  

---
## 🌱 Acknowledgment

This project was developed as part of academic and practical exploration in Machine Learning and Artificial Intelligence applications in agriculture.

---
