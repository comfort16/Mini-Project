import random
import xml.etree.ElementTree as ET
import os
import threading
import time

# Class representing student information
class ITStudent:
    def __init__(self, name, student_id, programme, courses, marks):
        self.name = name
        self.student_id = student_id
        self.programme = programme
        self.courses = courses
        self.marks = marks

# Buffer class to implement shared buffer
class Buffer:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.queue = []
        self.semaphore_producer = threading.Semaphore(max_size)
        self.semaphore_consumer = threading.Semaphore(0)
        self.mutex = threading.Lock()

    def add_to_buffer(self, item):
        self.semaphore_producer.acquire()
        self.mutex.acquire()
        self.queue.append(item)
        self.mutex.release()
        self.semaphore_consumer.release()

    def remove_from_buffer(self):
        self.semaphore_consumer.acquire()
        self.mutex.acquire()
        item = self.queue.pop(0)
        self.mutex.release()
        self.semaphore_producer.release()
        return item

# Consumer function to read student information from XML files and calculate results
def consumer(buffer):
    while True:
        file_num = buffer.remove_from_buffer()
        file_path = f"student{file_num}.xml"
        student_info = read_from_xml(file_path)
        os.remove(file_path)
        print(f"Consumed: {file_path}")
        average, pass_fail = calculate_average(student_info)
        print(f"Student Name: {student_info.name}")
        print(f"Student ID: {student_info.student_id}")
        print(f"Programme: {student_info.programme}")
        print("Courses and Marks:")
        for course, mark in zip(student_info.courses, student_info.marks):
            print(f"  {course}: {mark}")
        print(f"Average Mark: {average:.2f}")
        print(f"Pass/Fail: {pass_fail}")
        print("\n")
        time.sleep(random.randint(1, 3))

if __name__ == "__main__":
    buffer = Buffer(max_size=10)

    # Start the threads
    producer_thread.start()
    consumer_thread.start()

    # Wait for both threads to finish
    producer_thread.join()
    consumer_thread.join()
