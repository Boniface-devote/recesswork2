#function for handling(appending in a file) a file automatically

class Handl:
    def __init__(self, name, action):
        self.name = name
        self.action= action
        self.file = None

    def __enter__(self):
        self.file = open(self.name, self.action)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

# using the function
with Handl('devote.txt', 'a') as file:
    file.write(" /n my name is devote boniface")


###########multithreading and multiprocessing#######
import time
import threading
import multiprocessing

# Function to be executed
def my_function(duration):
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= duration:
            break

# Multithreading example
def run_with_threads(durations):
    threads = []
    for duration in durations:
        thread = threading.Thread(target=my_function, args=(duration,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Multiprocessing example
def run_with_processes(durations):
    processes = []
    for duration in durations:
        process = multiprocessing.Process(target=my_function, args=(duration,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

# Example usage
durations = [3, 5, 2, 4]  # Different durations in seconds

# Run with multithreading
print("Running with multithreading...")
run_with_threads(durations)

# Run with multiprocessing
print("Running with multiprocessing...")
run_with_processes(durations)



#function for connecting to database

import sqlite3

class Conn:
    def __init__(self, Database):
        self.Database = Database
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.Database)
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

# Example usage:
with Conn('employee.db') as conn:
    command = conn.cursor()
    command.execute("SELECT * FROM employee")
    rows = command.fetchall()
    for information in rows:
        print(information)
