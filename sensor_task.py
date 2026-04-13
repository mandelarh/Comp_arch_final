# sensor_task.py
import numpy as np
from utils import COST_TABLE

def sensor_task(data_size=1000):
    # --- Functional Logic ---
    data = np.random.rand(data_size)
    scaled_data = data * 100
    filtered_data = scaled_data[scaled_data > 50]
    
    # --- Simulation Logic ---
    # 1. Loading raw data (data_size loads)
    # 2. Scaling data (data_size multiplications)
    # 3. Filtering data (data_size comparisons/logic)
    
    instructions = data_size * 3
    cycles = (data_size * COST_TABLE["LOAD_STORE"]) + \
             (data_size * COST_TABLE["MUL_DIV"]) + \
             (data_size * COST_TABLE["LOGIC"])
             
    return len(filtered_data), instructions, cycles