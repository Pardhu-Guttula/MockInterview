from flask import Flask, request, jsonify
from Interviewer.Model.InterviewStatus.Pending import pendingslots



def register_pending_routes(app):
    @app.route('/interview-slots/available', methods=['POST'])
    def availableslots():
        try:
            data = request.json
            if not data or "interviewerID" not in data:
                return jsonify({"error": "Invalid input, 'interviewerID' is required"})

            # Create instance of the model and fetch available slots
            slot_obj = pendingslots()
            result = slot_obj.get_available_slots(data)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {e}"})
