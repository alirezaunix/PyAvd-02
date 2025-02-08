import threading
import time

def task(name, delay):
    print(f"Task {name} started")
    time.sleep(delay)  # Simulate a time-consuming task
    print(f"Task {name} finished after {delay} seconds")

# Create threads
thread1 = threading.Thread(target=task, args=("A", 3))
thread2 = threading.Thread(target=task, args=("B", 2))
thread3 = threading.Thread(target=task, args=("C", 1))

# Start threads
thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()

print("All tasks completed")