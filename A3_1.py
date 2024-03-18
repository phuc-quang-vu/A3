import psycopg

def createTable():
    # Drop students table if it already exists
    cur.execute('''
    DROP TABLE IF EXISTS students 
    ''')            
    
    # Create students table
    cur.execute('''
    CREATE TABLE students(
        student_id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        enrollment_date DATE      
    )
    ''')

    # Populate students table
    cur.execute('''
    INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
    ''')

#-------------------------------------------------------------------------------
# List all students in table
def getAllStudent():
    cur.execute('''
    SELECT * FROM students ORDER BY student_id
    ''')
    # Print all student records in a formatted way
    rows = cur.fetchall()
    for row in rows:
        print(f'{row[0]:3d} {row[1]:10s} {row[2]:10s} {row[3]:25s} {row[4]}') 

#-------------------------------------------------------------------------------
# Add new student to the end of table
def addStudent(first_name, last_name, email, enrollment_date):
    cur.execute('''
    INSERT INTO students(first_name, last_name, email, enrollment_date)
    VALUES (%s, %s, %s, %s)''', (first_name, last_name, email, enrollment_date))

#-------------------------------------------------------------------------------
# Update student email by student_id
def updateStudentEmail(student_id, new_email):
    cur.execute(f''' 
    UPDATE students 
    SET email = '{new_email}' 
    WHERE student_id = {student_id}
    ''')

#-------------------------------------------------------------------------------
# Delete student by student_id
def deleteStudent(student_id):
    cur.execute(f''' 
    DELETE FROM students
    WHERE student_id = {student_id}
    ''')

#-------------------------------------------------------------------------------
# tester
def main(): 

    createTable()

    print("Student list:")
    getAllStudent()
    
    print("Add new student (Tom Cruise):")
    addStudent("Tom", "Cruise", "tom.cruise@example.com","2023-09-02")
    getAllStudent()
    
    print("Update student id = 1's email :")
    updateStudentEmail(1, "john.doee@example.com")
    getAllStudent()

    print("Delete student id = 1:")
    deleteStudent (1)
    getAllStudent()

    input("Press any key to close...")

#-------------------------------------------------------------------------------
# Get connection to PostgreSQL to a database name A3_1
try:
    conn = psycopg.connect(
    dbname = "A3_1", 
    user = "postgres", 
    password = "8023", 
    host = "localhost", 
    port = 5432
    )


    # Create cursor to process SQL command
    cur = conn.cursor() 
    main()
    conn.commit()
    conn.close()

except psycopg.OperationalError as e:
    print (f" Error:{e}")
    exit (1) 
