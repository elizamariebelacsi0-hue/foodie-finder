# Foodie Finder

A Django-powered web application to discover the best restaurants and dishes in Naval Proper.

## Features

✨ **User Experience**
- Preloader on page load with animated logo
- Personalized welcome messages
- Toast notifications for registration, login, errors
- Smooth scrolling effects
- Back-to-Top button for easy navigation
- Fully responsive and mobile-friendly design

🔍 **Search & Discovery**
- Live search suggestions (A-Z food suggestions)
- Category filters with icons (🍔 Fast Food, 🍤 Seafood, 🍰 Dessert, etc.)
- Price tier badges (₱ - Affordable, ₱₱ - Moderate, ₱₱₱ - Expensive)
- Open/Closed status indicators (green for open, red for closed)

🏪 **Restaurant Details**
- Image carousel for browsing restaurant photos
- Complete menu with prices
- Operating hours
- Category tags and status badges

📱 **Authentication & Role-Based Access**
- User registration with profile creation
- Secure login/logout with automatic role-based redirection
- Three dashboard types: Admin, Restaurant, and User
- Role-based access control system

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Navigate to the project directory:
```bash
cd "C:\Users\Christine Elaine\Desktop\my foodie app"
```

2. Activate the virtual environment:
```bash
.venv\Scripts\Activate.ps1
```

3. Run migrations (if not already done):
```bash
python manage.py migrate
```

4. Create a superuser (optional, already created):
```bash
python manage.py createsuperuser
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Visit `http://127.0.0.1:8000/` in your browser

### Admin Access
- Admin Dashboard: `http://127.0.0.1:8000/console/`
- Django Admin: `http://127.0.0.1:8000/admin/`
- Username: `admin`
- Password: `adminpass123`

### Role-Based Dashboards
- **Admin Dashboard**: Professional sidebar interface for system management
- **Restaurant Dashboard**: Restaurant owners can manage their own restaurants
- **User Dashboard**: Regular users see the main Foodie Finder interface
- **Automatic Redirection**: Users are redirected based on their role after login

## Usage

1. **Register**: Fill out the registration form to create an account (defaults to 'user' role)
2. **Login**: Enter your email and password - automatic redirection based on role:
   - Admin users → Admin Dashboard with sidebar navigation
   - Restaurant users → Restaurant Dashboard for managing their restaurant
   - Regular users → Main Foodie Finder page
3. **Admin Features**: Manage restaurants, users, and system overview
4. **Restaurant Features**: Edit restaurant details, manage menu and images
5. **User Features**: Browse restaurants, search dishes, view details
6. **Role Management**: Admins can change user roles through Django admin panel

## Project Structure

```
├── core/               # Main application
│   ├── models.py      # Restaurant, Dish, Profile models
│   ├── views.py       # Views and logic
│   ├── admin.py       # Admin configuration
│   └── migrations/    # Database migrations
├── templates/         # HTML templates
├── static/            # CSS, images
│   ├── css/
│   └── img/
├── foodie_finder/     # Django settings
└── manage.py         # Django management script
```

## Technologies

- Django 5.2.7
- SQLite (default database)
- Pillow (image processing)
- HTML/CSS/JavaScript
- Poppins font (Google Fonts)

## Customization

### Adding Restaurants
Access the admin panel and use the Restaurant model to:
- Add new restaurants
- Upload images
- Set operating hours
- Assign categories
- Mark as featured

### Changing Theme Colors
Edit `static/css/styles.css` to adjust CSS variables:
```css
:root {
  --primary:#F54749;
  --accent:#FFB703;
  --green:#16a34a;
  --red:#dc2626;
}
```

## Notes

- All user data is stored in the database and visible only to admin
- The background image and logo are customizable in `static/img/`
- Restaurant images should be uploaded via admin panel
- Search suggestions cover A-Z popular dishes

## License

Created for educational purposes.

