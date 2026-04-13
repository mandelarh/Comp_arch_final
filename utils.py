# utils.py
import time

# Cost Table: Defines cycles per instruction type
COST_TABLE = {
    "ADD_SUB": 1,
    "MUL_DIV": 2,
    "LOAD_STORE": 5,  # Change this to 20 or 50 for your experiments
    "LOGIC": 1
}

CLOCK_FREQUENCY = 1_000_000_000  # 1 GHz (10^9 cycles per second)

def measure_time(func):
    start = time.time()
    result = func()
    end = time.time()
    return result, (end - start)