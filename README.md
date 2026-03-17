# Wildlife Expedition Tracker

A Django-based web application for researchers and wildlife enthusiasts to plan expeditions and record animal sightings made for my PythonWeb course at Softuni.

---

## 🚀 How to Run

### Prerequisites

- **Python 3.13+**
- **PostgreSQL** installed and running
- **pip** and **virtualenv**

### Step 1: Clone the Repository

```bash
git clone https://github.com/BobiBash/Softuni-Django-basics-project.git
cd Softuni-Django-basics-project/Wildlife_Expedition_Tracker
```

### Step 2: Create and Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** Tailwind CSS is handled by `django-tailwind-cli` and `pytailwindcss`. No Node.js needed!

### Step 4: Configure PostgreSQL

1. Create a database named `testing_wildlife_tracker`:
   ```sql
   CREATE DATABASE testing_wildlife_tracker;
   ```

2. Update the `.env` file with your PostgreSQL credentials:
   ```env
   DB_USER=postgres
   DB_PASSWORD=your_password
   ```

### Step 5: Apply Migrations

```bash
python manage.py migrate
```

### Step 6: (Optional) Populate Sample Data

```bash
python populate_db.py
```

This adds 20 sample animals for testing.

### Step 7: Run the Server

```bash
python manage.py tailwind runserver
```

The application will be available at: **http://127.0.0.1:8000/**

---

## 📁 Project Structure

```
Wildlife_Expedition_Tracker/
├── animals/              # Animal database management
├── expeditions/          # Expedition planning & CRUD
├── sightings/            # Animal sighting records
├── analytics_dashboard/  # Data visualization (Matplotlib charts)
├── common/               # Home, About, Search, Gallery
├── templates/            # Base templates & 404 page
├── static/               # CSS and Tailwind assets
├── media/                # Uploaded images
└── populate_db.py        # Sample data seeder
```

---

## 📊 Database Models

| Model | Relationships |
|-------|---------------|
| **Animal** | — |
| **Expedition** | ForeignKey → Animal (target_species), ManyToMany → Animal (expected_species) |
| **Sighting** | ForeignKey → Expedition, ForeignKey → Animal |

---

## ✨ Features

### Animal Management
- Browse all animals with kingdom, group, and distinctive features
- View detailed animal profiles
- Add new animals with form validation

### Expedition CRUD
- Create, Read, Update, Delete expeditions
- Specify target and expected species
- Location tracking with custom validation

### Sighting CRUD
- Log animal encounters with date, time, count, and coordinates
- Upload wildlife photos
- Latitude/Longitude validation

### Analytics Dashboard
- Top 5 most sighted animals
- Top 5 expedition locations
- Monthly trend chart (Matplotlib)

### Search & Navigation
- Site-wide search (animals & expeditions)
- Media gallery with all sighting images
- Custom 404 error page - view at `/404/`

---

## 🛠️ Technologies

| Technology | Purpose |
|------------|---------|
| Django 6.0.1 | Backend framework |
| PostgreSQL | Database |
| Tailwind CSS | Styling (via django-tailwind-cli) |
| Matplotlib | Data visualization |
| Pillow | Image handling |

---

## 🔧 Configuration

### Environment Variables (.env)

```env
DB_USER=postgres              # Your PostgreSQL username
DB_PASSWORD=your_password     # Your PostgreSQL password
```

### Database Settings

Default connection uses `localhost:5432`. Update in `settings.py` if needed:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "testing_wildlife_tracker",
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```
