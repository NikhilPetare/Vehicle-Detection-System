# Vehicle Detection System

## 📌 Project Overview

The **Vehicle Detection System** is a Python-based computer vision project developed to detect vehicles from a traffic video using the **YOLOv8n object detection model**.

The system processes a highway traffic video and identifies different types of vehicles such as **cars, motorcycles, buses, and trucks**. The detected vehicle information is stored in CSV files and can be viewed through a Streamlit dashboard.

## 🚗 Features

* Vehicle detection using YOLOv8n
* Detection of cars, motorcycles, buses, and trucks
* Real-time processing of traffic video
* Vehicle confidence score calculation
* Vehicle data storage in CSV format
* Summary of detected vehicles
* Streamlit dashboard for displaying vehicle information

## 🛠️ Technologies Used

* **Python**
* **YOLOv8**
* **Ultralytics**
* **OpenCV**
* **Pandas**
* **NumPy**
* **Streamlit**

## 📂 Project Structure

```text
PROJECT/
│
├── project.py
├── stream.py
├── summary.py
├── yolov8n.pt
├── highway.mp4
├── vehicle_data.csv
├── summary.csv
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd PROJECT
```

### 3. Install required libraries

```bash
python -m pip install -r requirements.txt
```

## ▶️ How to Run

### Run Vehicle Detection

```bash
python project.py
```

The program processes the traffic video and detects vehicles.

### Run the Dashboard

```bash
python -m streamlit run stream.py
```

The Streamlit dashboard displays the vehicle detection data.

## 📊 Output

The system generates vehicle information such as:

* Vehicle ID
* Vehicle Type
* Confidence
* Position

The information is stored in:

```text
vehicle_data.csv
```

A summary of the detected vehicles is stored in:

```text
summary.csv
```

## 🎯 Vehicle Classes

The system focuses on common road vehicles, including:

* 🚗 Car
* 🏍️ Motorcycle
* 🚌 Bus
* 🚚 Truck

## 🔮 Future Scope

The project can be further improved by adding:

* Traffic counting
* Speed estimation
* Lane-wise vehicle counting
* Traffic density analysis
* Real-time camera support
* Advanced traffic analytics

## 👨‍💻 Project

**Vehicle Detection System**

Developed as part of a **Python with Data Analytics Internship Project**.

---

**Note:** This project focuses on vehicle detection and traffic analysis. Number-plate recognition is not included in the current version.
