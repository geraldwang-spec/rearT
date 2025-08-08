import pyodbc

class dbProcess:
    def __init__(self):
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = pyodbc.connect(
                "Driver={ODBC Driver 17 for SQL Server};"
                "Server=localhost\\"
            )

