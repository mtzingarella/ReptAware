#Write the general annotated framnework and beginning code for a datagrabber object that will connect to an MS server SQL database on the same network and retrieve data by executing stored procedures.
#The data will be stored in a pandas dataframe and the data will be cleaned and preprocessed before being used in a machine learning model.
#The data will be used to predict the next day's closing price of a stock.

import pyodbc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DataGrabber:
    def __init__(self):
    
        
    # Connecting to database
        
        SERVER = self.read_server()
        DATABASE = self.read_database_name()
        USERNAME = self.read_username()
        PASSWORD = self.read_password
        
        
        connectionString = (
        "Driver={ODBC Driver 17 for SQL Server};"
        f"Server={SERVER};"
        "Database=iNaturalist;"
        "Trusted_Connection=yes;"
    )        
        self.connection = pyodbc.connect(connectionString) 
        self.cursor = self.connection.cursor()
      

    # Executing stored procedures to retrieve data
    def get_data(self, stored_procedure, params=None):
        if params:
            placeholders = ', '.join(['?'] * len(params))
            query = f"EXEC {stored_procedure} {placeholders}"
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(f"EXEC {stored_procedure}")
        
        rows = self.cursor.fetchall()
        columns = [column[0] for column in self.cursor.description]
        data = pd.DataFrame.from_records(rows, columns=columns)
        return print(data)
    
    def test(self):
        data = self.cursor.execute(f"EXEC sp_GetObsByDayOfWeek")
        # turn the returned data into a dataframe
        data = pd.DataFrame(data.fetchall())
     

        return print(data)
    

    #Reading server connection info from super secure location
    def read_server(self):
        with open('private/dbserver.txt', 'r') as file:
            print(file.read().strip())
            return file.read().strip()
    def read_database_name(self):
        with open('private/dbname.txt', 'r') as file:
            return file.read().strip()
    def read_username(self):
        with open('private/username.txt', 'r') as file:
            return file.read().strip()
    def read_password(self):
        with open('private/password.txt', 'r') as file:
            return file.read().strip()



   