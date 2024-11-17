from flask import Flask, request, jsonify
from Interviewer.Model.InterviewStatus.Cancelled import *


def register_cancelled_routes(app):

    @app.route('/interview-slots/cancelled', methods=['POST'])
    def acceptedslots():
        try:
            data = request.json
            if not data or "interviewerID" not in data:
                return jsonify({"error": "Invalid input, 'interviewerID' is required"})

            # Create instance of the model and fetch available slots
            slot_obj = CancelledSlots()
            result = slot_obj.get_cancelled_slots(data)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {e}"})
        
    @app.route('/interview-slots/cancel', methods=['PUT'])   
    def cancelslots():
        try:
            data = request.json
            if not data or "interviewerID" not in data:
                return jsonify({"error": "Invalid input, 'interviewerID' is required"})

            # Create instance of the model and fetch available slots
            slot_obj = CancelledSlots()
            result = slot_obj.cancel_slots(data)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {e}"})

    