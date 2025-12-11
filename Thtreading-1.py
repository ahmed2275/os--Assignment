import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Thread: {threading.current_thread().name} → {i}")
        time.sleep(0.5)

# Create 2 threads
t1 = threading.Thread(target=print_numbers, name="T1")
t2 = threading.Thread(target=print_numbers, name="T2")

t1.start()
t2.start()

t1.join()
t2.join()

print("Threading example finished.")
