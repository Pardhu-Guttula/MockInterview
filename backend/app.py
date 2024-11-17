from flask import Flask
import os
import sys

app = Flask(__name__)

# file1_directory = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), "Interviewer", "controller")
# )
# sys.path.append(file1_directory)

from Interviewer.Controller.InterviewStatus.Pending import register_pending_routes
from Interviewer.Controller.InterviewStatus.Accepted import register_accepted_routes
from Interviewer.Controller.InterviewStatus.Cancelled import register_cancelled_routes
from Interviewer.Controller.InterviewStatus.Completed import register_completed_routes
from Interviewer.Controller.InterviewStatus.JoinButton import register_joinbutton_routes

register_pending_routes(app)
register_accepted_routes(app)
register_cancelled_routes(app)
register_completed_routes(app)
register_joinbutton_routes(app)


@app.route("/", methods=["GET"])
def printHello():
    return "Version:1.0"

if __name__ == "__main__":
    app.run(debug=True)
