# app.py
from flask import Flask
from views.class_view import ClassesAPI, BookingAPI, BookingListAPI
from database import init_db
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

if not os.path.exists("data/database.db"):
    init_db()

# Register Routes
app.add_url_rule('/classes', view_func=ClassesAPI.as_view('classes'))
app.add_url_rule('/book', view_func=BookingAPI.as_view('book'))
app.add_url_rule('/bookings', view_func=BookingListAPI.as_view('bookings'))

if __name__ == '__main__':
    app.run(debug=True)
