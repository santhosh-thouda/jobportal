# Django Admin Panel Access Guide

## 🌐 Admin Panel URL
**URL:** http://127.0.0.1:8000/admin/

---

## 👤 Step 1: Create Superuser Account

### Option A: Interactive Command (Recommended)
Run this command and follow the prompts:
```bash
python manage.py createsuperuser
```

You'll be asked for:
- Username (e.g., `admin`)
- Email address (optional)
- Password (enter twice)

### Option B: Quick Script
Run the provided script:
```bash
python create_admin.py
```

**Default credentials:**
- Username: `admin`
- Email: `admin@example.com`
- Password: `admin123`

⚠️ **Change the password after first login!**

---

## 🔐 Step 2: Login to Admin Panel

1. Make sure your development server is running:
   ```bash
   python manage.py runserver
   ```

2. Open your browser and go to:
   ```
   http://127.0.0.1:8000/admin/
   ```

3. Enter your superuser credentials:
   - Username
   - Password

4. Click "Log in"

---

## 📋 What You Can Manage in Admin Panel

### User Management
- **Custom Users** - All user accounts
- **Employers** - Employer profiles and company information
- **Job Seekers** - Job seeker profiles and resumes

### Job Management
- **Jobs** - View, edit, and manage all job listings
- **Categories** - Manage job categories with icons
- **Applications** - View and manage job applications

### Features
- ✅ Search and filter records
- ✅ Create, edit, and delete entries
- ✅ Bulk actions
- ✅ Date hierarchy navigation
- ✅ Custom list displays

---

## 🔧 Admin Configuration

The admin panel is configured in:
- `apps/accounts/admin.py` - User models
- `apps/jobs/admin.py` - Job models

---

## 🚨 Troubleshooting

### "No superuser exists"
- Create one using Step 1 above

### Can't log in
- Make sure you created a superuser account
- Check that the username/password are correct
- Ensure `is_superuser=True` and `is_staff=True` in the database

### Server not running
- Run: `python manage.py runserver`
- Check for any error messages

---

## 📝 Notes

- Superuser accounts have full access to all models
- Regular users (employers/job seekers) cannot access the admin panel
- Only users with `is_staff=True` can access the admin interface
- Always use strong passwords in production!

