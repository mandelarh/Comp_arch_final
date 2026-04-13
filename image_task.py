# image_task.py
import numpy as np
from utils import COST_TABLE

def image_task(n=100):
    # --- Functional Logic ---
    matrix_a = np.random.rand(n, n)
    matrix_b = np.random.rand(n, n)
    result_matrix = np.dot(matrix_a, matrix_b)
    
    # --- Simulation Logic ---
    # Matrix multiplication (dot product) is roughly O(n^3) operations
    num_ops = n**3
    
    instructions = num_ops
    cycles = num_ops * COST_TABLE["MUL_DIV"]
    
    return np.sum(result_matrix), instructions, cycles