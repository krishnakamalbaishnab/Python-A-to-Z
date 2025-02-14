import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)  # Simulating a delay
        print(f"Number: {i}")

def print_letters():
    for letter in "ABCDE":
        time.sleep(1)
        print(f"Letter: {letter}")

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Both threads have finished execution.")
