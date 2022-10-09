import psycopg2
import pandas as pd
import os

def create_db():
    conn = psycopg2.connect(
        host="localhost",
        database="race",
        user="postgres",
        password="1234")

    # Open a cursor to perform database operations
    cursor = conn.cursor()

    # Execute a command: this creates a new table
     
    cursor.execute("CREATE TABLE IF NOT EXISTS testing_data_phase_4 (query varchar (500) NOT NULL,"
                                                            "predited_answer varchar (800),"
                                                            "original_question_no varchar (800) DEFAULT 'User entry',"
                                                            "original_question varchar (800) DEFAULT 'User entry',"
                                                            "original_answer varchar (800) DEFAULT 'User entry',"
                                                            "date_added date DEFAULT CURRENT_TIMESTAMP);"
                                                            )

    cursor.close()
    conn.commit()
    conn.close()

def insert_db(query,predicted_answer,original_question_no,original_question,original_answer):
    conn = psycopg2.connect(
        host="localhost",
        database="race",
        user="postgres",
        password="1234")
    
    # Open a cursor to perform database operations
    cursor = conn.cursor()

    s = "INSERT INTO testing_data_phase_4 "
    s += "("
    s += "query"
    s += ", predited_answer"
    s += ", original_question_no"
    s += ", original_question"
    s += ", original_answer"
    s += ") VALUES ("
    #s += " '" + str(query) + "'"
    #s += ",'" + str(original_question_no) + "'"
    #s += ",'" + str(original_question) + "'"
    #s += ",'" + str(original_answer) + "'"
    #s += ")"
    s += " '" + "This for testing" + "'"
    s += ",'" + "This for testing" + "'"
    s += ",'" + "This for testing" + "'"
    s += ",'" + "This for testing" + "'"
    s += ",'" + "This for testing" + "'"
    s += ")"


    # Insert data into the table

    cursor.execute(s)
    
    conn.commit()
    cursor.close()
    conn.close()

#query = " I wanted to know more about artificial intelligence course "
#predicted_answer = " Thank you for your interest in RACE programs! RACE offers both long-term and short-term programs in emerging technologies such as Data Science, Cybersecurity, Artificial Intelligence, and Cloud Architecture and Security to meet the futurist demands of these industries. The long-term programs offered are; 1. PGD/MS in Business Analytics 2. PGD/ M. Tech/M.S in Artificial Intelligence 3. PGD/M. Tech/MS in Cybersecurity, and, 4. M. Sc. in Cloud Architecture and Security. We also have 20+ short-term programs customized to add value to the participants."

def extract_all_data():
    conn = psycopg2.connect(
        host="localhost",
        database="race",
        user="postgres",
        password="1234")
    
    # Open a cursor to perform database operations
    cursor = conn.cursor()

    df = pd.read_sql_query('select * from "testing_data"',con=conn)
    #print(df)
    # determining the name of the file
    file_name = 'ResultData.xlsx'
    #os.remove("ResultData.xlsx")
    # saving the excel
    df.to_excel(file_name)
    #print('DataFrame is written to Excel File successfully.')

    conn.commit()
    cursor.close()
    conn.close()

    



create_db()

insert_db(query = "This for testing",predicted_answer = "This for testing",original_question_no = "This for testing",original_question = "This for testing",original_answer = "This for testing")
