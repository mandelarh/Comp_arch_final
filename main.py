# main.py
from sensor_task import sensor_task
from image_task import image_task
from decision_task import decision_task
from utils import CLOCK_FREQUENCY

def run_simulation():
    # Get data from all tasks
    _, instr_s, cycles_s = sensor_task()
    _, instr_i, cycles_i = image_task()
    _, instr_d, cycles_d = decision_task()
    
    # Totals
    total_instructions = instr_s + instr_i + instr_d
    total_cycles = cycles_s + cycles_i + cycles_d
    
    # --- Calculations ---
    # CPI = total cycles / # of instructions
    cpi = total_cycles / total_instructions
    
    # ET = (total instructions * CPI) / clock frequency
    execution_time = (total_instructions * cpi) / CLOCK_FREQUENCY
    
    print(f"Total Instructions: {total_instructions}")
    print(f"Total Cycles: {total_cycles}")
    print(f"CPI: {cpi:.2f}")
    print(f"Simulated Execution Time (ET): {execution_time:.6f} seconds")
    
    # Check Real-Time Constraint (10 FPS = 100ms = 0.1s)
    if execution_time <= 0.1:
        print("RESULT: Real-time requirement MET.")
    else:
        print("RESULT: Real-time requirement FAILED.")

if __name__ == "__main__":
    run_simulation()