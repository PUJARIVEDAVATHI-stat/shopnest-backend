from repositories.user_repository import (
    get_user_by_email as repo_get_user_by_email
)

from auth.password import verify_password
from auth.jwt import create_access_token

from auth.password import hash_password
from repositories.user_repository import (
    get_user_by_email as repo_get_user_by_email,
    create_user as repo_create_user
)

def get_user_by_email(email):
    return repo_get_user_by_email(email)


def authenticate_user(email, password):
    email = email.strip().lower()

    result = repo_get_user_by_email(email)

    if not result["succeed"]:
        return {
            "succeed": False,
            "message": "Invalid email or password"
        }

    user = result["data"]

    password_hash = user[6]
    is_active = user[8]

    if not is_active:
        return {
            "succeed": False,
            "message": "Invalid email or password"
        }

    if not verify_password(password, password_hash):
        return {
            "succeed": False,
            "message": "Invalid email or password"
        }

    access_token = create_access_token(
        user_id=user[0],
        role_id=user[1],
        role_name=user[2]
    )

    return {
        "succeed": True,
        "data": {
            "user_id": user[0],
            "role_id": user[1],
            "role_name": user[2],
            "first_name": user[3],
            "last_name": user[4],
            "email": user[5],
            "phone": user[7],
            "access_token": access_token
        }
    }
def register_customer(
    first_name,
    last_name,
    email,
    password,
    phone=None
):
    # Normalize email
    email = email.strip().lower()

    # First name validation
    if not first_name or not first_name.strip():
        return {
            "succeed": False,
            "message": "First name is required"
        }

    if len(first_name.strip()) > 100:
        return {
            "succeed": False,
            "message": "First name cannot exceed 100 characters"
        }

    # Last name validation
    if last_name and len(last_name.strip()) > 100:
        return {
            "succeed": False,
            "message": "Last name cannot exceed 100 characters"
        }

    # Email validation
    if not email:
        return {
            "succeed": False,
            "message": "Email is required"
        }

    if len(email) > 255:
        return {
            "succeed": False,
            "message": "Email cannot exceed 255 characters"
        }

    # Password validation
    if not password:
        return {
            "succeed": False,
            "message": "Password is required"
        }

    if len(password) < 8:
        return {
            "succeed": False,
            "message": "Password must be at least 8 characters"
        }

    # Phone validation
    if phone and len(phone.strip()) > 20:
        return {
            "succeed": False,
            "message": "Phone number cannot exceed 20 characters"
        }

    # Check whether email is already registered
    existing_user = repo_get_user_by_email(email)

    if existing_user["succeed"]:
        return {
            "succeed": False,
            "message": "Email is already registered"
        }

    # Hash password
    password_hash = hash_password(password)

    # Create customer
    result = repo_create_user(
        first_name=first_name.strip(),
        last_name=last_name.strip() if last_name else None,
        email=email,
        password_hash=password_hash,
        phone=phone.strip() if phone else None
    )

    if not result["succeed"]:
        return {
            "succeed": False,
            "message": result["message"]
        }

    return {
        "succeed": True,
        "data": {
            "user_id": result["data"]["user_id"],
            "first_name": first_name.strip(),
            "last_name": last_name.strip() if last_name else None,
            "email": email,
            "phone": phone.strip() if phone else None,
            "role_id": 2,
            "role_name": "Customer"
        }
    }