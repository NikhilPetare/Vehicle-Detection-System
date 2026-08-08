import pandas as pd

data = pd.read_csv("vehicle_data.csv")

total_vehicles = len(data)

car_count = len(data[data["Vehicle Type"] == "Car"])
bike_count = len(data[data["Vehicle Type"] == "Motorcycle"])
bus_count = len(data[data["Vehicle Type"] == "Bus"])
truck_count = len(data[data["Vehicle Type"] == "Truck"])

summary = pd.DataFrame({
    "Vehicle Type": [
        "Car",
        "Motorcycle",
        "Bus",
        "Truck",
        "Total Vehicles"
    ],
    "Count": [
        car_count,
        bike_count,
        bus_count,
        truck_count,
        total_vehicles
    ]
})

summary.to_csv("summary.csv", index=False)

print("--------------------------------")
print("Vehicle Detection Summary")
print("--------------------------------")
print(summary)

print("\nSummary saved as summary.csv")