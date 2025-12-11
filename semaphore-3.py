import threading
import time

semaphore = threading.Semaphore(2)  # allow only 2 threads at a time

def worker(id):
    print(f"Thread {id} waiting...")
    with semaphore:
        print(f"Thread {id} entered critical section")
        time.sleep(2)
        print(f"Thread {id} leaving")

threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Semaphore example finished.")
