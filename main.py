from sensor_task import sensor_task
from image_task import image_task
from decision_task import decision_task
def sensor():
    result, exec_time = sensor_task()

    print("-"*20+"Sensor Task Results"+"-"*20)
    print("Filtered values:", result)
    print("Execution time:", exec_time, "seconds")

def image():
    result, exec_time = image_task()
    print("-"*20+"Image Task Results"+"-"*20)
    print("Result:", result)
    print("Execution time:", exec_time)

def decision():
    print("-"*20+"Decision Task Results"+"-"*20)
    print(decision_task())






if __name__ == "__main__":
    sensor()
    image()
    decision()