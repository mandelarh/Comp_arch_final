import time
import random

def decision_task():
    start = time.time()
    distance = random.uniform(0, 100)
    lane_offset = random.uniform(-5, 5)
    speed = random.uniform(0, 120)

    if distance < 10:
        action = "Brake"
    elif lane_offset > 2:
        action = "Steer Right"
    elif lane_offset < -2:
        action = "Steer Left"
    elif speed < 30:
        action = "Accelerate"
    else:
        action = "Maintain Speed"

    end = time.time()

    return action, (end - start)

if __name__ == "__main__":
    action, exec_time = decision_task()
    print("Action:", action)
    print("Execution time:", exec_time)