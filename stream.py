import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="Vehicle Detection Dashboard",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Real World Applications")
st.caption("Vehicle Detection and Tracking System using YOLOv8n")

st.markdown("---")

# Project Objectives

st.subheader("🎯 Project Objectives")

obj1, obj2, obj3 = st.columns(3)

with obj1:
    st.info("🚗 Detect vehicles automatically using YOLOv8n.")

with obj2:
    st.info("🔢 Count different types of vehicles accurately.")

with obj3:
    st.info("📊 Store detection results and display them through a dashboard.")

st.markdown("---")

# Technologies Used

st.subheader("🛠️ Technologies Used")

tech1, tech2, tech3, tech4, tech5 = st.columns(5)

with tech1:
    st.markdown("**🐍 Python**")
    st.caption("Programming Language")

with tech2:
    st.markdown("**🤖 YOLOv8n**")
    st.caption("Object Detection")

with tech3:
    st.markdown("**👁️ OpenCV**")
    st.caption("Video Processing")

with tech4:
    st.markdown("**🐼 Pandas**")
    st.caption("Data Processing")

with tech5:
    st.markdown("**📈 Matplotlib**")
    st.caption("Data Visualization")

st.markdown("---")

# Key Features

st.subheader("⭐ Key Features")

feature1, feature2, feature3, feature4 = st.columns(4)

with feature1:
    st.success("🔍 Vehicle Detection")
    st.caption("Detects vehicles from video.")

with feature2:
    st.success("🏷️ Vehicle Classification")
    st.caption("Identifies Cars, Motorcycles, Buses and Trucks.")

with feature3:
    st.success("🔢 Vehicle Counting")
    st.caption("Provides total and category-wise counts.")

with feature4:
    st.success("📊 Data Visualization")
    st.caption("Displays vehicle statistics using charts.")

st.markdown("---")

# USP

st.subheader("🚀 USP – Unique Selling Points")

usp1, usp2, usp3 = st.columns(3)

with usp1:
    st.warning("⚡ Fast Detection")
    st.caption("YOLOv8n provides fast and efficient vehicle detection.")

with usp2:
    st.warning("📁 Automated Data Storage")
    st.caption("Detection results are stored in CSV format for analysis.")

with usp3:
    st.warning("💻 Simple Dashboard")
    st.caption("Easy-to-understand interface for vehicle statistics.")

st.markdown("---")

# Check if file exists

if not os.path.exists("vehicle_data.csv"):
    st.warning("⚠️ vehicle_data.csv not found. Please run vehicle_detection.py first.")
    st.stop()

# Load data

data = pd.read_csv("vehicle_data.csv")

# Fix name if detection code used "Bike"

data["Vehicle Type"] = data["Vehicle Type"].replace(
    "Bike", "Motorcycle"
)

# Sidebar

st.sidebar.header("Dashboard Controls")
st.sidebar.write(f"Total Records: {len(data)}")

# Summary Metrics

st.subheader("📊 Summary Data")

total = len(data)
cars = len(data[data["Vehicle Type"] == "Car"])
bikes = len(data[data["Vehicle Type"] == "Motorcycle"])
buses = len(data[data["Vehicle Type"] == "Bus"])
trucks = len(data[data["Vehicle Type"] == "Truck"])

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Vehicles", total)
col2.metric("Cars", cars)
col3.metric("Motorcycles", bikes)
col4.metric("Buses", buses)
col5.metric("Trucks", trucks)

st.markdown("---")

# Tabs

tab1, tab2 = st.tabs(
    ["Detected Vehicle Data", "Distribution Pie Chart"]
)

with tab1:

    st.subheader("Detected Vehicles with Confidence Score")

    st.dataframe(
        data,
        use_container_width=True,
        height=400
    )

    st.subheader("Count Summary Table")

    summary_df = data["Vehicle Type"].value_counts().reset_index()

    summary_df.columns = [
        "Vehicle Type",
        "Count"
    ]

    st.table(summary_df)

with tab2:

    st.subheader("Vehicle Type Distribution")

    # Prepare data for pie chart

    chart_data = data["Vehicle Type"].value_counts()

    # Medium size pie chart

    fig, ax = plt.subplots(figsize=(5, 5))

    ax.pie(
        chart_data,
        labels=chart_data.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=[
            "#4CAF50",
            "#2196F3",
            "#FF9800",
            "#F44336"
        ]
    )

    ax.axis("equal")

    ax.set_title(
        "Distribution of Detected Vehicles",
        fontsize=14,
        fontweight="bold"
    )

    # Center the chart

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.pyplot(fig)

st.markdown("---")

st.info(
    "**Model**: YOLOv8n | "
    "**Input**: Highway vehicles.mp4 | "
    "**Output**: CSV + Dashboard"
)

st.success("✅ Project Completed Successfully")