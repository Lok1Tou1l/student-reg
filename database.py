import sqlite3 

conn = sqlite3.connect('students.db')
cursor = conn.cursor()
def create_table(self):
    self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            specialty TEXT NOT NULL,
            image BLOB NOT NULL
        );
    ''')
    self.conn.commit()

def save_to_database(self, name, email, phone, specialty, image):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    # Insert student details and picture into the database
    cursor.execute("INSERT INTO students (name ,email,phone,specialty,image) VALUES (?, ?, ?, ?, ?)", (name, email, phone, specialty, image))
    
    conn.commit()
    conn.close()