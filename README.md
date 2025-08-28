#  Travel Booking Application (Django)

A simple **Travel Booking Web Application** built using **Python (Django)**.  
This project allows users to **view available travel options, book tickets, and manage their bookings** with a clean and responsive interface.

---


##  Features

###  User Management
- User **registration, login, and logout** using Django’s built-in authentication system.
- Profile update functionality.

###  Travel Options
- Manage **Travel Options** (Flight, Train, Bus) with fields:
  - Travel ID  
  - Type (Flight / Train / Bus)  
  - Source & Destination  
  - Date & Time  
  - Price  
  - Available Seats  

###  Booking
- Book travel options by selecting available seats.  
- Each booking contains:
  - Booking ID  
  - User (Foreign Key)  
  - Travel Option (Foreign Key)  
  - Number of Seats  
  - Total Price  
  - Booking Date  
  - Status (Confirmed / Cancelled)  

###  Manage Bookings
- View current and past bookings.  
- Cancel existing bookings.  

###  Frontend
- User-friendly UI using **Django Templates**.  
- Pages for:
  - Registration, Login, Profile Management  
  - Travel options listing with filters (type, source, destination, date)  
  - Booking form & confirmation  
  - Booking history & cancellation  
- Responsive design with **Bootstrap / CSS**.

---

##  Tech Stack

- **Backend:** Python (Django 5.x)  
- **Frontend:** Django Templates, HTML, CSS, Bootstrap  
- **Database:** MySQL  
- **Testing:** Django Test Framework (Unit Tests included)  
- **Deployment :** PythonAnywhere  

---

##  Getting Started

Follow these steps to run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/travel_booking.git
cd travel_booking
```
2. Create Virtual Environment
```bash
python -m venv venv
```
3. Install Dependencies
```bash
pip install -r requirements.txt
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

4. Configure Database

By default, the project uses SQLite.
For MySQL setup , update settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel_booking',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Create Superuser
```bash
python manage.py createsuperuser
```

6. Run Development Server
```bash
python manage.py runserver
```

Open in browser:
```bash
http://127.0.0.1:8000/
```

Running Tests
```bash
python manage.py test
```


License

This project is for educational purposes as part of the Assignment: Travel Booking Application.
You are free to modify and extend it.






















