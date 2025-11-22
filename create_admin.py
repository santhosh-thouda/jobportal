"""
Script to create a Django superuser
Run this with: python create_admin.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.accounts.models import CustomUser

# Create superuser with default credentials
username = 'admin'
email = 'admin@example.com'
password = 'admin123'

if CustomUser.objects.filter(username=username).exists():
    print(f"User '{username}' already exists!")
else:
    CustomUser.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f"Superuser created successfully!")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print("\n⚠️  IMPORTANT: Change the password after first login!")

