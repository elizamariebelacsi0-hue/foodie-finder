# Deployment Guide

## Deploy to Render

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/foodie-finder.git
git push -u origin main
```

### 2. Create Render Web Service
1. Go to [render.com](https://render.com) and sign up
2. Click "New" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: foodie-finder
   - **Environment**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn foodie_finder.wsgi:application`

### 3. Environment Variables
Add these in Render dashboard:
- `SECRET_KEY`: Generate a new secret key
- `DATABASE_URL`: (Render will provide PostgreSQL URL)
- `PYTHON_VERSION`: 3.11.0

### 4. Database Setup
- Add PostgreSQL database in Render
- Copy the DATABASE_URL to your environment variables

Your app will be available at: `https://your-app-name.onrender.com`