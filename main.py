# main.py
import time
from sensor_task import sensor_task
from image_task import image_task
from decision_task import decision_task
from utils import CLOCK_FREQUENCY

def run_performance_simulation(print_results=True):
    system_start = time.time()

    obs_count, sensor_instr, sensor_cycles = sensor_task()
    img_result, image_instr, image_cycles = image_task()
    drive_action, real_time_val, decision_instr, decision_cycles = decision_task()
    
    # --- Aggregation ---
    total_system_instructions = sensor_instr + image_instr + decision_instr
    total_system_cycles = sensor_cycles + image_cycles + decision_cycles
    average_cpi = total_system_cycles / total_system_instructions
    simulated_execution_time = (total_system_instructions * average_cpi) / CLOCK_FREQUENCY

    results = {
        "sensor_result": obs_count,
        "image_result": img_result,
        "decision_result": drive_action,
        "decision_real_time": real_time_val,
        "wall_time": wall_time,
        "instructions": total_system_instructions,
        "cycles": total_system_cycles,
        "cpi": average_cpi,
        "simulated_execution_time": simulated_execution_time,
    }

    if print_results:
        print("-" * 20 + " Processor Simulation Start " + "-" * 20)
        print(f"Sensor Result:               {results['sensor_result']}")
        print(f"Image Result:                {results['image_result']}")
        print(f"Decision Result:             {results['decision_result']}")
        print(f"Total Instructions Executed: {results['instructions']:,}")
        print(f"Total Simulated Cycles:      {results['cycles']:,}")
        print(f"System-Wide Average CPI:     {results['cpi']:.2f}")
        print(f"Simulated Execution Time:    {results['simulated_execution_time']:.6f} seconds")
        print(f"Wall-Clock Execution Time:   {results['wall_time']:.6f} seconds")

        print("-" * 50)
        if results["simulated_execution_time"] <= 0.1:
            print("STATUS: PASS - System met the 100ms real-time deadline.")
        else:
            print("STATUS: FAIL - System exceeded 100ms deadline (Risk of collision).")
        print("-" * 50)

    return results

if __name__ == "__main__":
    run_performance_simulation()
    print(decision_task())