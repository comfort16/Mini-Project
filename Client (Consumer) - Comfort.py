import socket
import xml.etree.ElementTree as ET
import os

# Function to read student information from an XML file
def read_from_xml(file_path):
    # Code to read student information from an XML file...
    # (Same as previous implementation)

# Function to calculate average mark and pass/fail status
def calculate_average(student):
    # Code to calculate average mark and pass/fail status...
    # (Same as previous implementation)

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345

    client_socket.connect((host, port))

    while True:
        file_num_str = client_socket.recv(1024).decode()

        if not file_num_str:
            break

        file_num = int(file_num_str)
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

    client_socket.close()
