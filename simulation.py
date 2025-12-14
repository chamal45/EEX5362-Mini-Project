import simpy
import random
import statistics


# Global Simulation Parameters
SIM_TIME = 8 * 60          # 8 hours (minutes)
SERVICE_TIME_MIN = 2       # Min service time (minutes)
SERVICE_TIME_MAX = 4       # Max service time (minutes)


# Performance Metrics
wait_times = []
queue_lengths = []
students_served = 0
busy_time = 0.0


# Student Process
def student(env, name, librarians):
    global wait_times, queue_lengths, students_served, busy_time

    arrival_time = env.now
    with librarians.request() as request:
        queue_lengths.append(len(librarians.queue))
        yield request

        # Waiting time
        wait_time = env.now - arrival_time
        wait_times.append(wait_time)

        # Service time
        service_time = random.uniform(SERVICE_TIME_MIN, SERVICE_TIME_MAX)
        busy_time += service_time
        students_served += 1

        yield env.timeout(service_time)


# Student Arrival Generator
def generate_students(env, librarians, arrival_interval):
    student_id = 0
    while True:
        inter_arrival = random.expovariate(1.0 / arrival_interval)
        yield env.timeout(inter_arrival)
        student_id += 1
        env.process(student(env, f"Student {student_id}", librarians))


# Simulation Runner
def run_simulation(num_librarians, arrival_interval):
    global wait_times, queue_lengths, students_served, busy_time

    # Reset metrics
    wait_times = []
    queue_lengths = []
    students_served = 0
    busy_time = 0.0

    env = simpy.Environment()
    librarians = simpy.Resource(env, capacity=num_librarians)

    env.process(generate_students(env, librarians, arrival_interval))
    env.run(until=SIM_TIME)

    # Calculate metrics
    avg_wait = statistics.mean(wait_times) if wait_times else 0
    max_queue = max(queue_lengths) if queue_lengths else 0
    utilization = busy_time / (num_librarians * SIM_TIME)
    throughput = students_served / (SIM_TIME / 60)

    return {
        "students_served": students_served,
        "avg_wait": avg_wait,
        "max_queue": max_queue,
        "utilization": utilization,
        "throughput": throughput
    }


# Run Experiment
def run_experiment(num_librarians, arrival_interval):
    metrics = run_simulation(num_librarians, arrival_interval)

    print("=" * 55)
    print("     UNIVERSITY LIBRARY BORROWING DESK SIMULATION")
    print("=" * 55)
    print(f"Number of Librarians     : {num_librarians}")
    print(f"Average Arrival Interval: {arrival_interval} minutes")
    print("-" * 55)
    print("Performance Results")
    print("-" * 55)
    print(f"Total Students Served   : {metrics['students_served']}")
    print(f"Average Waiting Time    : {metrics['avg_wait']:.2f} minutes")
    print(f"Maximum Queue Length    : {metrics['max_queue']} students")
    print(f"Librarian Utilization   : {metrics['utilization'] * 100:.2f}%")
    print(f"Throughput              : {metrics['throughput']:.2f} students/hour")
    print()


# Main Execution
if __name__ == "__main__":
    # Effect of Number of Librarians
    run_experiment(num_librarians=1, arrival_interval=4)
    run_experiment(num_librarians=2, arrival_interval=4)
    run_experiment(num_librarians=3, arrival_interval=4)

    # Load Sensitivity Analysis
    run_experiment(num_librarians=2, arrival_interval=3)
    run_experiment(num_librarians=2, arrival_interval=2)
