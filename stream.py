import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Vehicle Detection and Tracking System",
    page_icon="🚗",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

body{
    background-color:#f5f7fa;
}

.main-header{
    background:linear-gradient(90deg,#1E3C72,#2A5298);
    padding:25px;
    border-radius:15px;
    text-align:center;
    color:white;
    margin-bottom:20px;
}

.main-header h1{
    font-size:40px;
    margin:0;
}

.main-header h3{
    margin-top:10px;
    color:#f1f1f1;
}

.card{
    background:white;
    padding:15px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.15);
}

.tech-card{
    color:white;
    text-align:center;
    padding:18px;
    border-radius:12px;
    font-size:20px;
    font-weight:bold;
    margin-bottom:15px;
}

.footer{
    text-align:center;
    color:gray;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<div class="main-header">
<h1>🚗 Vehicle Detection and Tracking System</h1>
<h3>YOLOv8 • OpenCV • Python • Streamlit</h3>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# CHECK CSV
# -----------------------------
if not os.path.exists("vehicle_data.csv"):
    st.error("vehicle_data.csv not found.")
    st.stop()

# -----------------------------
# LOAD DATA
# -----------------------------
data = pd.read_csv("vehicle_data.csv")

# Replace Bike with Motorcycle
data["Vehicle Type"] = data["Vehicle Type"].replace(
    "Bike",
    "Motorcycle"
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🚗 Dashboard Controls")

st.sidebar.success("Vehicle Detection System")

st.sidebar.write("### Dataset Information")

st.sidebar.write("Total Records :", len(data))

st.sidebar.markdown("---")

vehicle_filter = st.sidebar.multiselect(
    "Select Vehicle Types",
    options=data["Vehicle Type"].unique(),
    default=data["Vehicle Type"].unique()
)

filtered_data = data[
    data["Vehicle Type"].isin(vehicle_filter)
]

st.sidebar.markdown("---")

st.sidebar.info("""
**Project**

Vehicle Detection and Tracking System

**Model**

YOLOv8n

**Framework**

Streamlit

**Libraries**

OpenCV

Pandas

Matplotlib
""")

# -----------------------------
# TABS
# -----------------------------
home, dashboard, charts, project = st.tabs(
    [
        "🏠 Home",
        "📊 Dashboard",
        "📈 Charts",
        "📖 Project Info"
    ]
)

# ==========================================================
# HOME TAB
# ==========================================================

with home:

    st.header("🏠 Welcome")

    st.markdown("""
### 🚗 Vehicle Detection and Tracking System

The **Vehicle Detection and Tracking System** is a computer vision project
developed using **YOLOv8**, **OpenCV**, **Python**, and **Streamlit**.

The system automatically detects vehicles from traffic videos,
classifies them into different categories, tracks their movement,
counts each vehicle type, and stores the results in a CSV file.

An interactive Streamlit dashboard is used to visualize the
detected vehicle information through tables, summary cards,
and graphical charts.
""")

    st.markdown("---")

    st.subheader("✨ Project Features")

    col1, col2 = st.columns(2)

    with col1:
        st.success("✅ Real-Time Vehicle Detection")
        st.success("✅ Vehicle Classification")
        st.success("✅ Vehicle Counting")
        st.success("✅ Vehicle Tracking")

    with col2:
        st.success("✅ CSV Report Generation")
        st.success("✅ Interactive Dashboard")
        st.success("✅ Graphical Visualization")
        st.success("✅ Easy Data Analysis")

    st.markdown("---")

    st.subheader("⚙ Workflow")

    st.info("""
🎥 Input Video

⬇

🚗 Vehicle Detection (YOLOv8)

⬇

📌 Vehicle Classification

⬇

🔄 Vehicle Tracking

⬇

📊 Vehicle Counting

⬇

💾 CSV Storage

⬇

📈 Streamlit Dashboard
""")


# ==========================================================
# PROJECT INFORMATION TAB
# ==========================================================

with project:

    st.header("📖 Project Information")

    st.markdown("---")

    # AIM
    with st.expander("🎯 Aim", expanded=True):

        st.write("""
To develop an intelligent **Vehicle Detection and Tracking System**
using **YOLOv8** and **OpenCV** that automatically detects,
classifies, tracks, and counts vehicles from traffic videos.

The system also provides an interactive **Streamlit Dashboard**
to visualize vehicle statistics, improve traffic monitoring,
and generate useful analytical reports.
""")

    # OBJECTIVES
    with st.expander("📌 Objectives", expanded=True):

        st.markdown("""
1. Detect vehicles accurately using the YOLOv8 object detection model.

2. Classify detected vehicles into Car, Motorcycle, Bus and Truck.

3. Track vehicles across consecutive video frames.

4. Count the total number of detected vehicles.

5. Store vehicle information in a CSV file.

6. Display detection results in an interactive Streamlit dashboard.

7. Generate statistical reports using graphs and charts.

8. Demonstrate the use of Artificial Intelligence and Computer Vision for traffic monitoring.
""")

    # TECHNOLOGIES
    with st.expander("🛠 Technologies Used", expanded=True):

        tech = [
            ("Python", "#4CAF50"),
            ("YOLOv8", "#2196F3"),
            ("OpenCV", "#FF9800"),
            ("Streamlit", "#9C27B0"),
            ("Pandas", "#009688"),
            ("Matplotlib", "#F44336"),
            ("CSV", "#795548"),
            ("Ultralytics", "#3F51B5"),
            ("VS Code", "#607D8B")
        ]

        index = 0

        for i in range(3):

            col1, col2, col3 = st.columns(3)

            for col in [col1, col2, col3]:

                name, color = tech[index]

                col.markdown(
                    f"""
                    <div style="
                    background:{color};
                    color:white;
                    padding:20px;
                    border-radius:12px;
                    text-align:center;
                    font-size:20px;
                    font-weight:bold;
                    margin-bottom:15px;">
                    {name}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                index += 1

    # PROJECT DETAILS
    with st.expander("📋 Project Details", expanded=False):

        st.table(
            pd.DataFrame(
                {
                    "Attribute": [
                        "Project Name",
                        "Model Used",
                        "Programming Language",
                        "Framework",
                        "Libraries",
                        "Input",
                        "Output"
                    ],
                    "Details": [
                        "Vehicle Detection and Tracking System",
                        "YOLOv8n",
                        "Python",
                        "Streamlit",
                        "OpenCV, Pandas, Matplotlib",
                        "Traffic Video",
                        "CSV File + Interactive Dashboard"
                    ]
                }
            )
        )

# ==========================================================
# DASHBOARD TAB
# ==========================================================

with dashboard:

    st.header("📊 Vehicle Detection Dashboard")

    st.markdown(
        "Monitor the detected vehicle statistics, browse the detection records, "
        "and download the generated CSV report."
    )

    st.markdown("---")

    # -----------------------------
    # SUMMARY
    # -----------------------------
    total = len(filtered_data)

    cars = len(filtered_data[filtered_data["Vehicle Type"] == "Car"])
    motorcycles = len(filtered_data[filtered_data["Vehicle Type"] == "Motorcycle"])
    buses = len(filtered_data[filtered_data["Vehicle Type"] == "Bus"])
    trucks = len(filtered_data[filtered_data["Vehicle Type"] == "Truck"])

    st.subheader("🚗 Detection Summary")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("🚘 Total", total)
    col2.metric("🚗 Cars", cars)
    col3.metric("🏍 Motorcycles", motorcycles)
    col4.metric("🚌 Buses", buses)
    col5.metric("🚚 Trucks", trucks)

    st.markdown("---")

    # -----------------------------
    # QUICK INSIGHTS
    # -----------------------------
    st.subheader("📌 Quick Insights")

    left, right = st.columns(2)

    with left:

        if total > 0:
            most_detected = filtered_data["Vehicle Type"].value_counts().idxmax()
            most_count = filtered_data["Vehicle Type"].value_counts().max()

            st.success(
                f"Most Detected Vehicle : **{most_detected}** ({most_count})"
            )

        else:
            st.warning("No vehicle detected.")

    with right:

        unique_types = filtered_data["Vehicle Type"].nunique()

        st.info(
            f"Vehicle Categories Present : **{unique_types}**"
        )

    st.markdown("---")

    # -----------------------------
    # VEHICLE DATA
    # -----------------------------
    st.subheader("📋 Detected Vehicle Records")

    st.dataframe(
        filtered_data,
        use_container_width=True,
        height=450
    )

    st.markdown("---")

    # -----------------------------
    # SUMMARY TABLE
    # -----------------------------
    st.subheader("📑 Vehicle Count Summary")

    summary = (
        filtered_data["Vehicle Type"]
        .value_counts()
        .reset_index()
    )

    summary.columns = ["Vehicle Type", "Count"]

    summary["Percentage (%)"] = (
        summary["Count"] /
        summary["Count"].sum() *
        100
    ).round(2)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.dataframe(
            summary,
            use_container_width=True
        )

    with col2:

        st.metric(
            "Vehicle Types",
            len(summary)
        )

        if len(summary) > 0:

            highest = summary.iloc[0]["Vehicle Type"]

            st.metric(
                "Highest Category",
                highest
            )

    st.markdown("---")

    # -----------------------------
    # DOWNLOAD CSV
    # -----------------------------
    st.subheader("📥 Export Data")

    csv = filtered_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Vehicle Data (CSV)",
        data=csv,
        file_name="vehicle_detection_report.csv",
        mime="text/csv"
    )

    st.markdown("---")

    # -----------------------------
    # PROJECT STATUS
    # -----------------------------
    st.success("✅ Vehicle Detection Completed Successfully")

    st.info("""
**Model Used:** YOLOv8n

**Framework:** Streamlit

**Input:** Highway Traffic Video

**Output:** Vehicle Detection Report + Interactive Dashboard
""")

# ==========================================================
# CHARTS TAB
# ==========================================================

with charts:

    st.header("📈 Vehicle Statistics & Analysis")

    st.markdown(
        "Visual representation of detected vehicle data using different charts."
    )

    st.markdown("---")

    vehicle_count = filtered_data["Vehicle Type"].value_counts()

    if len(vehicle_count) == 0:
        st.warning("No vehicle data available for the selected filter.")
    else:

        # ------------------------------------------------------
        # Pie Chart & Bar Chart
        # ------------------------------------------------------
        col1, col2 = st.columns(2)

        with col1:

            st.subheader("🥧 Vehicle Distribution")

            fig1, ax1 = plt.subplots(figsize=(6, 6))

            colors = [
                "#4CAF50",
                "#2196F3",
                "#FF9800",
                "#F44336"
            ]

            ax1.pie(
                vehicle_count.values,
                labels=vehicle_count.index,
                autopct="%1.1f%%",
                startangle=90,
                colors=colors
            )

            ax1.axis("equal")

            st.pyplot(fig1)

        with col2:

            st.subheader("📊 Vehicle Count")

            fig2, ax2 = plt.subplots(figsize=(7, 5))

            ax2.bar(
                vehicle_count.index,
                vehicle_count.values,
                color=colors
            )

            ax2.set_xlabel("Vehicle Type")
            ax2.set_ylabel("Count")
            ax2.set_title("Detected Vehicles")

            for i, value in enumerate(vehicle_count.values):
                ax2.text(i, value + 0.2, str(value), ha="center")

            st.pyplot(fig2)

        st.markdown("---")

        # ------------------------------------------------------
        # Horizontal Bar Chart
        # ------------------------------------------------------
        st.subheader("📉 Vehicle Comparison")

        fig3, ax3 = plt.subplots(figsize=(8, 4))

        ax3.barh(
            vehicle_count.index,
            vehicle_count.values,
            color=colors
        )

        ax3.set_xlabel("Count")
        ax3.set_ylabel("Vehicle Type")
        ax3.set_title("Vehicle Category Comparison")

        for i, value in enumerate(vehicle_count.values):
            ax3.text(value + 0.2, i, str(value))

        st.pyplot(fig3)

        st.markdown("---")

        # ------------------------------------------------------
        # Line Chart
        # ------------------------------------------------------
        st.subheader("📈 Vehicle Trend")

        fig4, ax4 = plt.subplots(figsize=(8, 4))

        ax4.plot(
            vehicle_count.index,
            vehicle_count.values,
            marker="o",
            linewidth=3
        )

        ax4.set_xlabel("Vehicle Type")
        ax4.set_ylabel("Count")
        ax4.set_title("Vehicle Distribution Trend")

        st.pyplot(fig4)

        st.markdown("---")

        # ------------------------------------------------------
        # Percentage Table
        # ------------------------------------------------------
        st.subheader("📋 Percentage Analysis")

        percentage = (
            vehicle_count / vehicle_count.sum() * 100
        ).round(2)

        percent_df = percentage.reset_index()
        percent_df.columns = [
            "Vehicle Type",
            "Percentage (%)"
        ]

        st.dataframe(
            percent_df,
            use_container_width=True
        )

        st.markdown("---")

        # ------------------------------------------------------
        # Analysis
        # ------------------------------------------------------
        st.subheader("📌 Statistical Analysis")

        highest = vehicle_count.idxmax()
        lowest = vehicle_count.idxmin()

        col1, col2 = st.columns(2)

        with col1:
            st.success(
                f"🚗 Highest Detected Vehicle : {highest}"
            )

            st.info(
                f"Count : {vehicle_count.max()}"
            )

        with col2:
            st.warning(
                f"🚙 Lowest Detected Vehicle : {lowest}"
            )

            st.info(
                f"Count : {vehicle_count.min()}"
            )

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
"""
<div style='text-align:center; padding:15px;'>

<h3>🚗 Vehicle Detection and Tracking System</h3>

<b>Model :</b> YOLOv8n &nbsp;&nbsp; | &nbsp;&nbsp;
<b>Framework :</b> Streamlit &nbsp;&nbsp; | &nbsp;&nbsp;
<b>Language :</b> Python

<br><br>

Developed as a Diploma Final Year Project using
Computer Vision and Artificial Intelligence.

</div>
""",
unsafe_allow_html=True
)