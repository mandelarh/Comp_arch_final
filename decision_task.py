import time
import random
from utils import COST_TABLE

def decision_task():
    start = time.time()
    
    # Inputs
    distance = random.uniform(0, 100)
    lane_offset = random.uniform(-5, 5)
    speed = random.uniform(0, 120)

    # Simulation Counters
    # Every comparison (<, >) and assignment (=) is an instruction
    # We start with 3 assignments for the inputs above
    instr_count = 3 
    
    if distance < 10:
        action = "Brake"
        instr_count += 2 # 1 comparison + 1 assignment
    elif lane_offset > 2:
        action = "Steer Right"
        instr_count += 3 # 2 comparisons (dist, lane) + 1 assignment
    elif lane_offset < -2:
        action = "Steer Left"
        instr_count += 4 # 3 comparisons + 1 assignment
    elif speed < 30:
        action = "Accelerate"
        instr_count += 5 # 4 comparisons + 1 assignment
    else:
        action = "Maintain Speed"
        instr_count += 5 # 4 comparisons + 1 final assignment

    # Calculate Cycles
    # Decision logic usually consists of simple arithmetic/logic instructions
    total_cycles = instr_count * COST_TABLE["LOGIC"]

    end = time.time()
    
    # Return everything: action, real time (for your curiosity), 
    # and the simulation data needed for the project.
    return action, (end - start), instr_count, total_cycles

if __name__ == "__main__":
    action, exec_time, inst, cyc = decision_task()
    print(f"Action: {action}")
    print(f"Real Execution time: {exec_time}")
    print(f"Simulated Instructions: {inst}")
    print(f"Simulated Cycles: {cyc}")