# multicore.py
import time
from multiprocessing import Pool
from main import run_performance_simulation

def run_workload(_=None):
    # Reuse the full single-core pipeline, but suppress printing
    return run_performance_simulation(print_results=False)

def run_parallel_test(num_processes):
    start = time.time()
    with Pool(processes=num_processes) as pool:
        results = pool.map(run_workload, [None] * num_processes)
    total_wall_time = time.time() - start
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
                f"  Run {i}: "
                f"WallTime={result['wall_time']:.6f}s, "
                f"Instr={result['instructions']}, "
                f"Cycles={result['cycles']}, "
                f"CPI={result['cpi']:.2f}"
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