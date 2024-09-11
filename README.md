# Chart Dashboard Application

This project is a web application that uses a **Next.js** frontend and a **Django API** backend. The dashboard displays four different types of charts (Candlestick, Line Chart, Bar Chart, and Pie Chart) by fetching data from the Django API. The charts are rendered using **Recharts**.

## Table of Contents
- [Setup Instructions](#setup-instructions)
  - [Frontend Setup (Next.js)](#frontend-setup-nextjs)
  - [Backend Setup (Django)](#backend-setup-django)
- [Libraries & Tools Used](#libraries--tools-used)
- [Approach and Thought Process](#approach-and-thought-process)

## Setup Instructions

### Frontend Setup (Next.js)

The frontend Next.js directory is located in a different repo [here](https://github.com/ShohruzE/blockhouse-take-home-frontend).

1. **Install Dependencies**:
   Navigate to the frontend directory and install the necessary packages:
   ```
   npm install
   ```
   
Run the Next.js Development Server: Start the development server:
```
npm run dev
```

View the Application: Open your browser and go to http://localhost:3000

###Backend Setup (Django)
Create a Virtual Environment: Create and activate a Python virtual environment:
```
python3 -m venv env
source env/bin/activate
```

Install Dependencies: Install Django and Django REST Framework:
```
pip install django djangorestframework
```

Set Up the Django Project: If the project files are not set up, create a Django project:
```
django-admin startproject backend
cd backend
django-admin startapp api
```

Run the Django Development Server: Start the server:
```
python manage.py runserver
```

View the API Endpoints: The Django API will be running on http://localhost:8000. You can view the data from the following endpoints:
```
/api/candlestick-data/
/api/line-chart-data/
/api/bar-chart-data/
/api/pie-chart-data/
```
###Libraries & Tools Used

Frontend:
-Next.js
-Recharts

Backend:
-Django
-Django Rest Framework

##Approach and Thought Process

Frontend (Next.js):

-The frontend uses Next.js to build a responsive dashboard. It includes multiple charts that fetch data from the backend.
-Recharts was used for rendering the charts because of its simplicity and flexibility for various types of charts and for creating customizable ones.

Backend (Django):

-The Django backend serves as an API to provide the hardcoded chart data to the frontend for each chart type.
-Django Rest Framework is used to create simple API endpoints that return JSON responses, which the frontend can easily take in.
