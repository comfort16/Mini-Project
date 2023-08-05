# Function to generate random student information
def generate_student_info():
    name = "Student" + str(random.randint(1, 100))
    student_id = str(random.randint(10000000, 99999999))
    programme = "Programme" + str(random.randint(1, 5))
    num_courses = random.randint(3, 6)
    courses = [f"Course{str(i)}" for i in range(1, num_courses + 1)]
    marks = [random.randint(40, 100) for _ in range(num_courses)]
    return ITStudent(name, student_id, programme, courses, marks)

# Function to write student information to an XML file
def write_to_xml(student, file_path):
    root = ET.Element("Student")
    ET.SubElement(root, "Name").text = student.name
    ET.SubElement(root, "StudentID").text = student.student_id
    ET.SubElement(root, "Programme").text = student.programme

    courses_elem = ET.SubElement(root, "Courses")
    for course, mark in zip(student.courses, student.marks):
        course_elem = ET.SubElement(courses_elem, "Course")
        ET.SubElement(course_elem, "CourseName").text = course
        ET.SubElement(course_elem, "Mark").text = str(mark)

    tree = ET.ElementTree(root)
    tree.write(file_path)

# Function to read student information from an XML file
def read_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    name = root.find("Name").text
    student_id = root.find("StudentID").text
    programme = root.find("Programme").text

    courses = []
    marks = []
    for course_elem in root.find("Courses"):
        courses.append(course_elem.find("CourseName").text)
        marks.append(int(course_elem.find("Mark").text))

    return ITStudent(name, student_id, programme, courses, marks)

# Function to calculate average mark and pass/fail status
def calculate_average(student):
    total_marks = sum(student.marks)
    average = total_marks / len(student.marks)
    return average, "Pass" if average >= 50 else "Fail"

# Producer function to generate student information and write to XML files
def producer(buffer):
    for i in range(1, 11):
        student_info = generate_student_info()
        file_path = f"student{i}.xml"
        write_to_xml(student_info, file_path)
        print(f"Produced: {file_path}")
        buffer.add_to_buffer(i)
        time.sleep(random.randint(1, 3))




    # Create producer and consumer threads
    producer_thread = threading.Thread(target=producer, args=(buffer,))
    consumer_thread = threading.Thread(target=consumer, args=(buffer,))

    
