import flask  # importing flask to
import mysql.connector
from flask import render_template

app = flask.Flask(__name__)

list1 = []


@app.route('/quiz')
def quiz_table():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='firstapp',
                                             user='root',
                                             password='vahiniheal1')
        list1 = []
        list2 = []

        sql_select_Query = "select * from quiz"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        c = cursor.rowcount
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            list1.append(row[0])
            list2.append(row[1])
            print("Id = ", row[0], )
            print("Question = ", row[1])
            print("A  = ", row[2])
            print("B  = ", row[3])
            print("C  = ", row[4])
            print("D  = ", row[5])
            print("Answer  = ", row[6],"\n")


        # return list1
        return "Heal paradise is the organization for helping poor people and orphans.The main moto is to give health " \
               "and education for all."


    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)



if __name__ == "__main__":
    app.run()
