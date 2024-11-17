import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()


class Acceptslots:
    def __init__(self):
        self.connection_source = mysql.connector.connect(
            host = os.getenv("MYSQL_HOST"),
            user = os.getenv("MYSQL_USER"),
            password = os.getenv("MYSQL_PASSWORD"),
            database = os.getenv("MYSQL_DB")
        )
        self.cursor = self.connection_source.cursor()
        
    def get_accepted_slots(self,data):
        try:
            interviewerID = data["interviewerID"]
            query = f"SELECT intervieweeID, slotID, time FROM InterviewFact WHERE interviewStatus = 'Accepted' AND interviewerID = '{interviewerID}'"
            self.cursor.execute(query)
            response = self.cursor.fetchall()
            # Convert the result into a list of objects
            result = [
                {"intervieweeID": row[0], "slotID": row[1], "time": datetime.strftime(row[2], "%d-%m-%Y %H:%M:%S"),} for row in response
            ]
            return result
        except Exception as e:
            return {"error": str(e)}
        
    def accept_slots(self,data):
        try:
            intervieweeID = data["intervieweeID"]
            interviewerID = data["interviewerID"]
            query = f"UPDATE InterviewFact SET interviewerID = '{interviewerID}', interviewStatus = 'Accepted' WHERE interviewStatus = 'Pending' AND intervieweeID = '{intervieweeID}'"
            self.cursor.execute(query)
            # Commit the changes to the database
            self.connection_source.commit()
            rows_affected = self.cursor.rowcount
            # print(f"Rows affected: {rows_affected}")
            if rows_affected > 0:
                return {"message": "Interview status updated successfully"}
            else:
                return {"message": "No records updated, possibly no matching 'Pending' status"}
        except Exception as e:
            return {"error": str(e)}