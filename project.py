from ultralytics import YOLO
import cv2
import csv

print("----------------------------------------")
print("Vehicle Detection and Tracking System")
print("----------------------------------------")

print("\nLoading YOLOv8 Model...")

model = YOLO("yolov8n.pt")

print("Model Loaded Successfully.")

video_path = "highway.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error : Unable to Open Video")
    exit()

print("Video Loaded Successfully.")

csv_file = open("vehicle_data.csv", "w", newline="")
writer = csv.writer(csv_file)

writer.writerow(["Vehicle ID", "Vehicle Type"])

vehicle_ids = set()

car_count = 0
bike_count = 0
bus_count = 0
truck_count = 0

vehicle_classes = {
    2: "Car",
    3: "Bike",
    5: "Bus",
    7: "Truck"
}

print("----------------------------------------")
print("Initialization Completed")
print("----------------------------------------")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model.track(frame, persist=True)

    for result in results:

        boxes = result.boxes

        if boxes is None:
            continue

        for box in boxes:

            if box.id is None:
                continue

            class_id = int(box.cls[0])

            if class_id not in vehicle_classes:
                continue

            vehicle_id = int(box.id[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            confidence = float(box.conf[0])

            label = vehicle_classes[class_id]

            if vehicle_id not in vehicle_ids:

                vehicle_ids.add(vehicle_id)

                writer.writerow([vehicle_id, label])

                if class_id == 2:
                    car_count += 1

                elif class_id == 3:
                    bike_count += 1

                elif class_id == 5:
                    bus_count += 1

                elif class_id == 7:
                    truck_count += 1

            text = f"{label} ID:{vehicle_id} {confidence:.2f}"

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    total = car_count + bike_count + bus_count + truck_count

    cv2.putText(
        frame,
        f"Cars : {car_count}",
        (20, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2
    )

    cv2.putText(
        frame,
        f"Bikes : {bike_count}",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2
    )

    cv2.putText(
        frame,
        f"Buses : {bus_count}",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2
    )

    cv2.putText(
        frame,
        f"Trucks : {truck_count}",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2
    )

    cv2.putText(
        frame,
        f"Total : {total}",
        (20, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    cv2.imshow("Vehicle Detection and Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

print("\n----------------------------------------")
print("Vehicle Detection Summary")
print("----------------------------------------")

print("Cars :", car_count)
print("Bikes :", bike_count)
print("Buses :", bus_count)
print("Trucks :", truck_count)

total = car_count + bike_count + bus_count + truck_count

print("Total Vehicles :", total)

csv_file.close()
cap.release()
cv2.destroyAllWindows()