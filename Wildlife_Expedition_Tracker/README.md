# Wildlife Expedition Tracker

## Project Overview
The **Wildlife Expedition Tracker** is a comprehensive Django-based web application designed for researchers and wildlife enthusiasts to plan expeditions and record animal sightings. It provides a robust platform for managing wildlife data, tracking expedition progress, and visualizing trends through an analytics dashboard.

---

## Features

### 🐾 Animal Database
- View a detailed list of animals including their kingdom, group, and distinctive features.
- Explore individual animal profiles with unique slugs.

### 🗺️ Expedition Management (Full CRUD)
- **Create**: Plan new expeditions specifying target species, expected species, and location.
- **Read**: List all active expeditions with details and filtered views.
- **Update**: Modify expedition details as plans evolve.
- **Delete**: Remove expeditions with a secure confirmation step featuring read-only fields.

### 🔭 Sighting Records (Full CRUD)
- **Log Sightings**: Record specific encounters during expeditions, including date, time, count, coordinates, and notes.
- **Image Uploads**: Attach photos of sighted animals to records.
- **Edit/Delete**: Full control over sighting logs with validation for geographic coordinates and time formats.

### 📊 Analytics Dashboard
- Dynamic visualization of data using **Matplotlib**.
- Track the top 5 most sighted animals and top 5 expedition locations.
- View monthly expedition trends via an interactive line chart.

### 🔍 Search & Discovery
- Site-wide search functionality integrated via custom context processors.
- Dedicated image gallery to browse all wildlife sightings visually.

---

## Technologies Used
- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Frontend**: Tailwind CSS (via `django-tailwind-cli`)
- **Data Visualization**: Matplotlib
- **Environment Management**: `python-dotenv`
- **Validation**: Custom Django validators for coordinates and time.

---

## Database Architecture
The project utilizes a relational PostgreSQL database with the following key models:
- **Animal**: Stores species information.
- **Expedition**:
    - `ForeignKey` to **Animal** (Target Species).
    - `ManyToMany` to **Animal** (Expected Species).
- **Sighting**:
    - `ForeignKey` to **Expedition**.
    - `ForeignKey` to **Animal**.

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Wildlife_Expedition_Tracker
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Unix/macOS
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Configuration
Ensure you have **PostgreSQL** installed and running. Create a database named `wildlife_expedition_tracker_db`.

### 5. Environment Variables
Create a `.env` file in the root directory (where `manage.py` is located) and provide your PostgreSQL credentials:
```env
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
```

### 6. Apply Migrations
```bash
python manage.py migrate
```

### 7. Run the Application
```bash
python manage.py runserver
```
The application will be accessible at `http://127.0.0.1:8000/`.

---

## Project Structure
- `animals/`: Manages the wildlife database and profiles.
- `expeditions/`: Handles planning, location tracking, and expedition CRUD.
- `sightings/`: Manages encounter logs, coordinate validation, and image uploads.
- `analytics_dashboard/`: Logic for data aggregation and Matplotlib chart generation.
- `common/`: Shared resources, home page, search functionality, and base templates.
- `templates/`: Structured Django templates with inheritance and a custom 404 page.

---

## Requirements Fulfillment
- **Apps**: 5 distinct Django apps.
- **Models**: 3 core models with Many-to-One and Many-to-Many relationships.
- **Forms**: Multiple forms with custom widgets, help texts, and disabled/read-only states for deletion confirmation.
- **Templates**: Over 10 templates using a base layout, partials, and custom context processors.
- **Database**: PostgreSQL implementation.
- **Validation**: Robust server-side validation for dates, times, and geographic data.
