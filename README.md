# 🚗 Vehicle Detection and Tracking System

## 📌 Project Overview

The **Vehicle Detection and Tracking System** is a Python-based computer vision project developed to detect and track vehicles from highway traffic video using the **YOLOv8n object detection model**.

The system processes traffic video and identifies different vehicle types such as **cars, motorcycles, buses, and trucks**. Detected vehicle information is recorded in CSV files, while a **Streamlit dashboard** is used to display and analyze the generated vehicle data.

This project was developed as part of a **Python with Data Analytics Internship Project**.

---

## ✨ Features

* 🚗 Vehicle detection using YOLOv8n
* 🏍️ Motorcycle detection
* 🚌 Bus detection
* 🚚 Truck detection
* 🎯 Vehicle confidence score calculation
* 🔢 Unique vehicle ID tracking
* 📊 Vehicle data storage in CSV format
* 📈 Vehicle summary generation
* 🌐 Interactive Streamlit dashboard
* 🎥 Traffic video processing
* 📋 Vehicle detection data analysis

---

## 🛠️ Technologies Used

| Technology      | Purpose                              |
| --------------- | ------------------------------------ |
| **Python**      | Main programming language            |
| **YOLOv8n**     | Vehicle detection and tracking       |
| **Ultralytics** | YOLO implementation                  |
| **OpenCV**      | Video processing and computer vision |
| **Pandas**      | Data processing and analysis         |
| **NumPy**       | Numerical operations                 |
| **Streamlit**   | Interactive dashboard                |
| **CSV**         | Vehicle data storage                 |

---

## 🔄 Project Workflow

```text
Highway Traffic Video
        ↓
     YOLOv8n
        ↓
Vehicle Detection
        ↓
Vehicle Tracking
        ↓
Vehicle Classification
        ↓
vehicle_data.csv
        ↓
summary.csv
        ↓
Streamlit Dashboard
```

---

## 📂 Project Structure

```text
Vehicle-Detection-System/
│
├── project.py
├── stream.py
├── summary.py
├── requirements.txt
├── vehicle_data.csv
├── summary.csv
├── README.md
└── .gitignore
```

> **Note:** The traffic video and YOLO model files are not included in the GitHub repository because they are large files and are excluded using `.gitignore`.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/NikhilPetare/Vehicle-Detection-System.git
```

### 2. Open the project folder

```bash
cd Vehicle-Detection-System
```

### 3. Install the required Python libraries

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ How to Run

### Step 1 — Run Vehicle Detection

```bash
python project.py
```

The program processes the traffic video using YOLOv8n and detects and tracks vehicles.

The detected vehicle information is stored in:

```text
vehicle_data.csv
```

### Step 2 — Generate/View Summary

The project also uses the generated vehicle data to create summary information stored in:

```text
summary.csv
```

### Step 3 — Run the Streamlit Dashboard

```bash
python -m streamlit run stream.py
```

The Streamlit dashboard displays the detected vehicle information and analysis.

---

## 📊 Output Data

The system records information such as:

* Vehicle ID
* Vehicle Type
* Confidence Score
* Vehicle Position

The main detection data is stored in:

```text
vehicle_data.csv
```

A summarized version of the detected vehicle information is stored in:

```text
summary.csv
```

---

## 🚘 Vehicle Classes

The system focuses on common highway vehicles:

* 🚗 **Car**
* 🏍️ **Motorcycle**
* 🚌 **Bus**
* 🚚 **Truck**

---

## 📈 Dashboard

The Streamlit dashboard provides a visual representation of the detected vehicle data.

It can be used to view:

* Total detected vehicles
* Vehicle types
* Vehicle counts
* Detection information
* Vehicle data records
* Summary information

### 📸 Screenshots

Screenshots of the Streamlit dashboard will be added here.

---

## 🔮 Future Scope

The system can be further improved by adding:

* 🚦 Traffic volume analysis
* 🛣️ Lane-wise vehicle counting
* 🚗 Vehicle speed estimation
* 📊 Traffic density analysis
* 📹 Real-time CCTV camera support
* 🚨 Traffic violation detection
* 📈 Advanced traffic analytics
* 🔢 Improved number-plate recognition

---

## 👨‍💻 Project Information

**Project:** Vehicle Detection and Tracking System

**Domain:** Python with Data Analytics / Computer Vision

**Model:** YOLOv8n

**Dashboard:** Streamlit

**Developer:** Nikhil Petare

---

## 📝 Note

This project focuses on **vehicle detection, tracking, data collection, and traffic analysis** from video.
