import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

class DbHelper:

    def __init__(self):
        load_dotenv()

        try:
            self.conn = mysql.connector.connect(
            host=os.environ['HOST'],
            user=os.environ['USER'],
            password='root',
            database=os.environ['DB']
            )
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
        except Error as error:
            print("Failed to connect to MySQL: {}".format(error))

    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        self.cursor.execute('select max(salary) from employee;')
        max_salaray = self.cursor.fetchone()
        return max_salaray[0]

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        self.cursor.execute('select min(salary) from employee;')
        min_salary = self.cursor.fetchone()
        return min_salary[0]

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)