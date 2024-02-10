import threading
import time

buffer = []
MAX_BUFFER_SIZE = 5


empty_semaphore = threading.Semaphore(MAX_BUFFER_SIZE)
full_semaphore = threading.Semaphore(0)
mutex = threading.Semaphore(1)

print_lock = threading.Lock()


def producer():
    while True:
        item = time.time()
        empty_semaphore.acquire()
        mutex.acquire()
        buffer.append(item)
        mutex.release()
        full_semaphore.release()
        with print_lock:
            print(f"Produced: {item}")
        time.sleep(1)


def consumer():
    while True:
        full_semaphore.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        mutex.release()
        empty_semaphore.release()
        with print_lock:
            print(f"Consumed: {item}")
        time.sleep(1)


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
