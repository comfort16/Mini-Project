import socket
import random
import xml.etree.ElementTree as ET
import os
import time

# Function to generate random student information
def generate_student_info():
    # Code to generate random student information...
    # (Same as previous implementation)

# Function to write student information to an XML file
def write_to_xml(student, file_path):
    # Code to write student information to an XML file...
    # (Same as previous implementation)

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345
    server_socket.bind((host, port))

    server_socket.listen(1)
    print("Server is listening...")

    connection, address = server_socket.accept()
    print(f"Connected to {address}")

    for i in range(1, 11):
        student_info = generate_student_info()
        file_path = f"student{i}.xml"
        write_to_xml(student_info, file_path)
        print(f"Produced: {file_path}")

        connection.send(str(i).encode())  # Send the file number as a string

        time.sleep(random.randint(1, 3))

    connection.close()
    server_socket.close()
