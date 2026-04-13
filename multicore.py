import time
from multiprocessing import Pool

from sensor_task import sensor_task
from image_task import image_task
from decision_task import decision_task


def run_workload(_=None):
    """
    Runs the full system workload once:
    sensor + image + decision
    """
    sensor_result, sensor_time = sensor_task()
    image_result, image_time = image_task()
    decision_result, decision_time = decision_task()

    total_task_time = sensor_time + image_time + decision_time

    return {
        "sensor_time": sensor_time,
        "image_time": image_time,
        "decision_time": decision_time,
        "task_time": total_task_time
    }


def run_parallel_test(num_processes):
    """
    Runs the workload in parallel using the specified number of processes.
    Measures total wall-clock execution time.
    """
    start = time.time()

    with Pool(processes=num_processes) as pool:
        results = pool.map(run_workload, [None] * num_processes)

    end = time.time()
    total_wall_time = end - start

    return results, total_wall_time


def calculate_speedup(single_time, multi_time):
    return single_time / multi_time


def calculate_efficiency(speedup, num_cores):
    return speedup / num_cores


def main():
    print("\n===== MULTICORE PERFORMANCE TEST =====\n")

    timings = {}

    for num_processes in [1, 2, 4]:
        results, wall_time = run_parallel_test(num_processes)
        timings[num_processes] = wall_time

        print(f"{num_processes} Process(es):")
        print(f"Total Wall Time: {wall_time:.6f} sec")

        for i, result in enumerate(results, start=1):
            print(
                f"  Task Run {i}: "
                f"Sensor={result['sensor_time']:.6f}s, "
                f"Image={result['image_time']:.6f}s, "
                f"Decision={result['decision_time']:.6f}s"
            )

        print()

    single_time = timings[1]

    print("===== SPEEDUP AND EFFICIENCY =====")
    for num_processes in [1, 2, 4]:
        time_taken = timings[num_processes]
        speedup = calculate_speedup(single_time, time_taken)
        efficiency = calculate_efficiency(speedup, num_processes)

        print(
            f"{num_processes} Process(es): "
            f"Time = {time_taken:.6f} sec, "
            f"Speedup = {speedup:.4f}, "
            f"Efficiency = {efficiency:.4f}"
        )


if __name__ == "__main__":
    main()