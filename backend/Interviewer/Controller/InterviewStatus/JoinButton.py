from flask import Flask, request, jsonify
from Interviewer.Model.InterviewStatus.JoinButton import *


def register_joinbutton_routes(app):

    @app.route('/interview-slots/getteamslink', methods=['GET'])
    def joinbutton():
        try:
            data = request.json
            if not data or "interviewerID" not in data:
                return jsonify({"error": "Invalid input, 'interviewerID' is required"})

            # Create instance of the model and fetch available slots
            slot_obj = JoinButton()
            result = slot_obj.get_teams_link(data)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {e}"})
        
    @app.route('/interview-slots/getteamslink', methods=['PUT'])   
    def completeslot():
        try:
            data = request.json
            if not data or "interviewerID" not in data:
                return jsonify({"error": "Invalid input, 'interviewerID' is required"})

            # Create instance of the model and fetch available slots
            slot_obj = JoinButton()
            result = slot_obj.complete_slots(data)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {e}"})