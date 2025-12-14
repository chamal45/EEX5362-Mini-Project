import matplotlib.pyplot as plt

# Simulation Results

# Varying number of librarians (arrival interval = 4 min)
librarians = [1, 2, 3]
avg_wait_time = [4.91, 0.16, 0.07]
utilization = [69.42, 33.66, 26.30]  
throughput = [14.0, 13.5, 15.5]

# Different load conditions (2 librarians)
arrival_rates = ["4 min", "3 min", "2 min"]
load_avg_wait = [0.16, 0.36, 2.40]
load_utilization = [33.66, 46.34, 76.02]

# 1. Average Waiting Time vs Number of Librarians
plt.figure(figsize=(6,4))
plt.plot(librarians, avg_wait_time, marker='o', color='blue', linewidth=2)
plt.xlabel("Number of Librarians")
plt.ylabel("Average Waiting Time (minutes)")
plt.title("Average Waiting Time vs Number of Librarians")
plt.grid(True)
plt.xticks(librarians)
plt.show()

# 2. Librarian Utilization vs Number of Librarians
plt.figure(figsize=(6,4))
plt.plot(librarians, utilization, marker='o', color='green', linewidth=2)
plt.xlabel("Number of Librarians")
plt.ylabel("Librarian Utilization (%)")
plt.title("Librarian Utilization vs Number of Librarians")
plt.grid(True)
plt.xticks(librarians)
plt.show()

# 3. Throughput vs Number of Librarians
plt.figure(figsize=(6,4))
plt.plot(librarians, throughput, marker='o', color='red', linewidth=2)
plt.xlabel("Number of Librarians")
plt.ylabel("Throughput (students/hour)")
plt.title("Throughput vs Number of Librarians")
plt.grid(True)
plt.xticks(librarians)
plt.show()

# 4. Average Waiting Time under Different Load Conditions
plt.figure(figsize=(6,4))
plt.plot(arrival_rates, load_avg_wait, marker='o', color='purple', linewidth=2)
plt.xlabel("Average Arrival Interval")
plt.ylabel("Average Waiting Time (minutes)")
plt.title("Waiting Time under Different Load Conditions")
plt.grid(True)
plt.show()

# 5. Librarian Utilization under Different Load Conditions
plt.figure(figsize=(6,4))
plt.plot(arrival_rates, load_utilization, marker='o', color='orange', linewidth=2)
plt.xlabel("Average Arrival Interval")
plt.ylabel("Librarian Utilization (%)")
plt.title("Utilization under Different Load Conditions")
plt.grid(True)
plt.show()
