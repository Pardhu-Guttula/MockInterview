from flask import Flask, request, jsonify
from Interviewer.Model.InterviewStatus.Accepted import Acceptslots


def register_accepted_routes(app):

    @app.route('/interview-slots/accepted', methods=['POST'])
    def acceptedSlots():
        try:
            data = request.json
            if not data or "interviewerID" not in data:
                return jsonify({"error": "Invalid input, 'interviewerID' is required"})

            # Create instance of the model and fetch available slots
            slot_obj = Acceptslots()
            result = slot_obj.get_accepted_slots(data)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {e}"})

    @app.route('/interview-slots/accept', methods=['PUT'])   
    def acceptslots():
        try:
            data = request.json
            if not data or "interviewerID" not in data:
                return jsonify({"error": "Invalid input, 'interviewerID' is required"})

            # Create instance of the model and fetch available slots
            slot_obj = Acceptslots()
            result = slot_obj.accept_slots(data)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {e}"})
