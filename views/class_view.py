from flask.views import MethodView
from flask import request, jsonify
from pydantic import ValidationError
from schemas import BookingRequest
from database import (
    get_all_classes, get_class_by_id,
    reduce_slot, add_booking, get_bookings_by_email
)
from utils import convert_timezone
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

class ClassesAPI(MethodView):
    def get(self):
        try:
            tz = request.args.get("timezone", "Asia/Kolkata")
            classes = get_all_classes()
            data = [{
                "id": c.id,
                "name": c.name,
                "datetime": convert_timezone(c.datetime, tz),
                "instructor": c.instructor,
                "available_slots": c.available_slots
            } for c in classes]
            return jsonify(data)
        except Exception as e:
            logging.exception("Failed to fetch classes")
            return jsonify({"error": str(e)}), 500


class BookingAPI(MethodView):
    def post(self):
        try:
            data = request.get_json()
            try:
                validated = BookingRequest(**data)
            except ValidationError as ve:
                return jsonify({"error": ve.errors()}), 422

            class_id = validated.class_id
            name = validated.client_name
            email = validated.client_email

            cls = get_class_by_id(class_id)
            if not cls:
                return jsonify({"error": "Class not found"}), 404

            if cls.available_slots <= 0:
                return jsonify({"error": "No slots available"}), 400

            if not reduce_slot(class_id):
                return jsonify({"error": "Could not book slot"}), 500

            add_booking(class_id, name, email)
            return jsonify({"message": "Booking successful"}), 201

        except Exception as e:
            logging.exception("Failed to process booking")
            return jsonify({"error": str(e)}), 500


class BookingListAPI(MethodView):
    def get(self):
        try:
            email = request.args.get("email")
            if not email:
                return jsonify({"error": "Email is required"}), 400

            bookings = get_bookings_by_email(email)
            return jsonify([b._asdict() for b in bookings])
        except Exception as e:
            logging.exception("Failed to fetch bookings")
            return jsonify({"error": str(e)}), 500
