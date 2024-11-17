import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()


class JoinButton:
    def __init__(self):
        self.connection_source = mysql.connector.connect(
            host = os.getenv("MYSQL_HOST"),
            user = os.getenv("MYSQL_USER"),
            password = os.getenv("MYSQL_PASSWORD"),
            database = os.getenv("MYSQL_DB")
        )
        self.cursor = self.connection_source.cursor()
        
    def get_teams_link(self,data):
        try:
            interviewerID = data["interviewerID"]
            intervieweeID = data["intervieweeID"]
            query = f"SELECT microsoftTeamsLink FROM InterviewFact WHERE interviewStatus = 'Pending' AND interviewerID = '{interviewerID}' AND intervieweeID = '{intervieweeID}'"
            self.cursor.execute(query)
            response = self.cursor.fetchall()
            if response:
                result = {
                    "TeamsLink": response,
                }
                return result
            else:
                return {"message": "No pending interview slots found for the given interviewerID"}
        except Exception as e:
            return {"error": str(e)}
        
    def complete_slots(self,data):
        try:
            interviewerID = data["interviewerID"]
            intervieweeID = data["intervieweeID"]
            query = f"UPDATE InterviewFact SET interviewerID = '{interviewerID}', interviewStatus = 'Completed' WHERE interviewStatus = 'Accepted' AND intervieweeID = '{intervieweeID}'"
            self.cursor.execute(query)
            # Commit the changes to the database
            self.connection_source.commit()
            rows_affected = self.cursor.rowcount
            # print(f"Rows affected: {rows_affected}")
            if rows_affected > 0:
                return {"message": "Interview status updated successfully"}
            else:
                return {"message": "No records updated, possibly no matching 'Accepted' status"}
        except Exception as e:
            return {"error": str(e)}