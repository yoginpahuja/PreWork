import sqlite3


def input_query(name, marks):
    inputQuery = "insert into Results values ('" + name + "','" + str(marks) + "');"
    print(inputQuery)
    return inputQuery



try:
    sqliteConnection = sqlite3.connect('assignment.db')
    cursor = sqliteConnection.cursor()
    print('DB Initialised')
    # Insert Statements Start #################
    cursor.execute(input_query('Yog',90))
    cursor.execute(input_query('Krish', 80))
    # Insert Statements End ###################
    searchString = input('Enter the string to search : ')

    if searchString == "":
        raise ValueError("Empty String not allowed")

    print(searchString)
    query = "SELECT * FROM Results WHERE name LIKE '%" + searchString + "%';"
    cursor.execute(query)

    result = cursor.fetchall()
    # print(type(result))
    if len(result) == 0:
        print("No rows returned")
    else:
        print(format(result))

        total_marks = sum(row[1] for row in result)
        avg_marks = total_marks / len(result)

        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {avg_marks}")

    cursor.close()

except ValueError as ve:
    print('Error occurred -', ve)
except sqlite3.Error as error:
    print('Error occurred -', error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')
