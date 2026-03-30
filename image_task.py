import numpy as np
import time
#simulating large compute operations

def image_task():
    start = time.time()

    matrix_a = np.random.rand(100, 100)
    matrix_b = np.random.rand(100, 100)

    result_matrix = np.dot(matrix_a, matrix_b)
    total_value = np.sum(result_matrix)

    end = time.time()

    return total_value, (end - start)

if __name__ == "__main__":
    result, exec_time = image_task()
    print("Result:", result)
    print("Execution time:", exec_time)