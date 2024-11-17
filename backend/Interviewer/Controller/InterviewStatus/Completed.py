from flask import Flask, request, jsonify
from Interviewer.Model.InterviewStatus.Completed import *


def register_completed_routes(app):

    @app.route('/interview-slots/completed', methods=['POST'])
    def completedslots():
        try:
            data = request.json
            if not data or "interviewerID" not in data:
                return jsonify({"error": "Invalid input, 'interviewerID' is required"})

            # Create instance of the model and fetch available slots
            slot_obj = CompletedSlots()
            result = slot_obj.get_completed_slots(data)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {e}"})
    
    