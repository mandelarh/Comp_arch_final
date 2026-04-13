# main.py
from sensor_task import sensor_task
from image_task import image_task
from decision_task import decision_task
from utils import CLOCK_FREQUENCY

def run_performance_simulation():
    print("-" * 20 + " Processor Simulation Start " + "-" * 20)

    # 1. Execute Sensor Task (Memory Intensive)
    # Returns: (filtered_count, instruction_count, cycle_count)
    obs_count, sensor_instr, sensor_cycles = sensor_task()

    # 2. Execute Image Task (Compute Intensive)
    # Returns: (sum_result, instruction_count, cycle_count)
    img_result, image_instr, image_cycles = image_task()

    # 3. Execute Decision Task (Logic Intensive)
    # Returns: (action_string, real_time, instruction_count, cycle_count)
    drive_action, real_time_val, decision_instr, decision_cycles = decision_task()

    # --- Aggregation ---
    total_system_instructions = sensor_instr + image_instr + decision_instr
    total_system_cycles = sensor_cycles + image_cycles + decision_cycles

    # --- Performance Metric Calculations ---
    # CPI = total cycles / total instructions
    average_cpi = total_system_cycles / total_system_instructions
    
    # ET = (total instructions * CPI) / clock frequency (1 GHz)
    simulated_execution_time = (total_system_instructions * average_cpi) / CLOCK_FREQUENCY

    # --- Output Results ---
    print(f"Total Instructions Executed: {total_system_instructions:,}")
    print(f"Total Simulated Cycles:      {total_system_cycles:,}")
    print(f"System-Wide Average CPI:     {average_cpi:.2f}")
    print(f"Simulated Execution Time:    {simulated_execution_time:.6f} seconds")

    # --- Real-Time Constraint Check (10 FPS = 0.1s Deadline) ---
    print("-" * 50)
    if simulated_execution_time <= 0.1:
        print("STATUS: PASS - System met the 100ms real-time deadline.")
    else:
        print("STATUS: FAIL - System exceeded 100ms deadline (Risk of collision).")
    print("-" * 50)

if __name__ == "__main__":
    run_performance_simulation()
    print(decision_task())