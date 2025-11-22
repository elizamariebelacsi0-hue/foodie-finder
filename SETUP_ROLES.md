# Role-Based Dashboard Setup

## Overview
The Foodie Finder app now has three types of dashboards:
- **Admin Dashboard**: For system administrators
- **Restaurant Dashboard**: For restaurant owners
- **User Dashboard**: For regular users (existing main page)

## Setup Instructions

1. **Run the migration** (when Django is available):
   ```bash
   python manage.py migrate
   ```

2. **Setup roles and create sample restaurant accounts**:
   ```bash
   python manage.py setup_roles
   ```

## User Roles

### Admin Users
- **Role**: `admin`
- **Access**: Admin dashboard with sidebar navigation
- **Features**: Manage restaurants, users, and system overview
- **Login**: Existing admin credentials

### Restaurant Users
- **Role**: `restaurant`
- **Access**: Restaurant dashboard
- **Features**: Manage own restaurant, dishes, and images
- **Sample Accounts**: Created by `setup_roles` command

### Regular Users
- **Role**: `user` (default)
- **Access**: Main user dashboard (existing functionality)
- **Features**: Browse restaurants, search dishes

## Dashboard Features

### Admin Dashboard
- Sidebar navigation with sections:
  - Dashboard: Overview and stats
  - Restaurants: Manage all restaurants
  - Users: View all user accounts and roles
  - Foodie Site: Link to main website
- Professional design with Bootstrap 5

### Restaurant Dashboard
- Restaurant-specific management:
  - Edit restaurant details
  - Manage menu/dishes
  - Upload and manage images
  - View what users see (featured restaurants)
- Branded with restaurant colors

## Login Flow
The system automatically redirects users based on their role:
- Admin → Admin Dashboard
- Restaurant → Restaurant Dashboard  
- User → Main Page

## Manual Role Assignment
Admins can change user roles through:
1. Django Admin Panel (`/admin/`)
2. Direct database editing
3. Profile model in admin interface

## Security
- Role-based access control
- Restaurant owners can only manage their own restaurant
- Admins have full system access
- Regular users have read-only access to public content