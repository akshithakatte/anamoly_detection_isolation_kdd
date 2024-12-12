import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Read anomalies from the log file
log_file = "anomalies_log.csv"
timestamps = []
latencies = []
sizes = []
statuses = []

with open(log_file, mode="r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        timestamps.append(row[0])
        latencies.append(float(row[1]))  # Convert latency to float
        sizes.append(float(row[2]))      # Convert size to float
        statuses.append(row[3])

# Separate anomalies and normal data
anomalous_latencies = [latencies[i] for i in range(len(statuses)) if statuses[i] == "Anomalous"]
anomalous_sizes = [sizes[i] for i in range(len(statuses)) if statuses[i] == "Anomalous"]

normal_latencies = [latencies[i] for i in range(len(statuses)) if statuses[i] == "Normal"]
normal_sizes = [sizes[i] for i in range(len(statuses)) if statuses[i] == "Normal"]

# Plot the anomalies and normal data
plt.figure(figsize=(10, 6))
plt.scatter(anomalous_latencies, anomalous_sizes, color="red", label="Anomalous", marker="x")
plt.scatter(normal_latencies, normal_sizes, color="blue", label="Normal", marker="o")

plt.title("Anomalous vs Normal Traffic")
plt.xlabel("Latency (ms)")
plt.ylabel("Size (bytes)")
plt.legend()
plt.grid(True)
plt.show()

# Print summary of anomalies
print(f"Total anomalies detected: {len(anomalous_latencies)}")
print(f"Total normal data points: {len(normal_latencies)}")
