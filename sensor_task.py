import numpy as np
import time
#simulating large data operations
import time

def sensor_task():
    start = time.time()

    data = np.random.rand(1000)
    scaled_data = data * 100
    filtered_data = scaled_data[scaled_data > 50]

    end = time.time()

    return len(filtered_data), (end - start)
if __name__ == "__main__":
    result, exec_time = sensor_task()
    print("Filtered values:", result)
    print("Execution time:", exec_time)