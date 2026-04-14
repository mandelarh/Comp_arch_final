import time
import random
from utils import COST_TABLE

def decision_task():
    start = time.time()
    distance = random.uniform(0, 100)
    lane_offset = random.uniform(-5, 5)
    speed = random.uniform(0, 120)

    instr_count = 3 
    
    if distance < 10:
        action = "Brake"
        instr_count += 2 
    elif lane_offset > 2:
        action = "Steer Right"
        instr_count += 3 
    elif lane_offset < -2:
        action = "Steer Left"
        instr_count += 4 
    elif speed < 30:
        action = "Accelerate"
        instr_count += 5 
    else:
        action = "Maintain Speed"
        instr_count += 5 

    total_cycles = instr_count * COST_TABLE["LOGIC"]

    end = time.time()

    return action, (end - start), instr_count, total_cycles

if __name__ == "__main__":
    action, exec_time, inst, cyc = decision_task()
    print(f"Action: {action}")
    print(f"Real Execution time: {exec_time}")
    print(f"Simulated Instructions: {inst}")
    print(f"Simulated Cycles: {cyc}")