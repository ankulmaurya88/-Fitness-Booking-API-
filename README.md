



# 🧘‍♀️ Fitness Booking API

A simple Booking API for a fictional fitness studio built with **Python**, **Flask**, **SQLite**, and **Pydantic**.

This API allows clients to:
- View upcoming fitness classes (Yoga, Zumba, HIIT)
- Book a class (if slots are available)
- View all bookings by a specific email address

---

## 📁 Project Structure
```
fitness_booking_api/
├── app.py                # Flask app entry point
├── database.py           # SQLite DB functions
├── models.py             # Data classes (Class, Booking)
├── schemas.py            # Pydantic request validation
├── utils.py              # Timezone utilities
├── seed_classes.py       # Seeds initial class data into DB
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── views/
│   └── class_view.py     # Class-based API endpoints
└── data/
    └── database.db       # SQLite DB (auto-generated)

```




---
## 🚀 How to Run This Project

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/ankulmaurya88/-Fitness-Booking-API-.git
cd -Fitness-Booking-API-
```
```bash
python3 -m venv venv
source venv/bin/activate  
```
```bash
pip install -r requirements.txt
```
```bash
python seed_classes.py
```
```bash
python app.py
```
🧪 Testing
Tests are located in the test/ folder. You can run them (if provided) with:

```bash
python -m unittest discover test

```
📷 Loom Demo Video
🎥 [Add your Loom video link here]

💡 Tips
To change timezones dynamically, use any IANA timezone string (e.g., Asia/Kolkata, America/New_York)

Ensure you seed the database before hitting endpoints

Use Postman or curl for testing your endpoints


👨‍💻 Author
Ankul Maurya





