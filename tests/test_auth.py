from auth.password import hash_password, verify_password
from auth.jwt import create_access_token, decode_access_token
from auth.context import get_current_user
from services.user_service import register_customer
import uuid

def test_password_hash_and_verify():
    password = "TestPassword123"

    password_hash = hash_password(password)

    assert password_hash != password
    assert password_hash.startswith("$2b$")

    assert verify_password(
        password,
        password_hash
    ) is True

    assert verify_password(
        "WrongPassword",
        password_hash
    ) is False
    
def test_jwt_create_and_decode():
    token = create_access_token(
        user_id=1,
        role_id=2,
        role_name="Customer"
    )

    assert token is not None
    assert isinstance(token, str)

    result = decode_access_token(token)

    assert result["succeed"] is True

    payload = result["data"]

    assert payload["sub"] == "1"
    assert payload["role_id"] == 2
    assert payload["role_name"] == "Customer"
    assert "exp" in payload    
    
def test_get_current_user():
    token = create_access_token(
        user_id=1,
        role_id=2,
        role_name="Customer"
    )

    result = get_current_user(token)

    assert result["succeed"] is True

    user = result["data"]

    assert user["user_id"] == 1
    assert user["role_id"] == 2
    assert user["role_name"] == "Customer"    
    
def test_get_current_user_with_invalid_token():
    result = get_current_user("invalid-token")

    assert result["succeed"] is False
    assert result["message"] == "Invalid token"
    
def test_get_current_user_without_token():
    result = get_current_user(None)

    assert result["succeed"] is False
    assert result["message"] == "Authentication token is required" 
    
def test_register_customer():
    email = f"pytest.customer.{uuid.uuid4()}@example.com"

    result = register_customer(
        first_name="Pytest",
        last_name="Customer",
        email=email,
        password="TestPassword123",
        phone="7777777777"
    )

    assert result["succeed"] is True

    user = result["data"]

    assert user["first_name"] == "Pytest"
    assert user["last_name"] == "Customer"
    assert user["email"] == email
    assert user["phone"] == "7777777777"
    assert user["role_id"] == 2
    assert user["role_name"] == "Customer"
    
def test_register_customer_duplicate_email():
    email = f"duplicate.customer.{uuid.uuid4()}@example.com"

    first_result = register_customer(
        first_name="Duplicate",
        last_name="Customer",
        email=email,
        password="TestPassword123",
        phone="6666666666"
    )

    assert first_result["succeed"] is True

    second_result = register_customer(
        first_name="Duplicate",
        last_name="Customer",
        email=email,
        password="TestPassword123",
        phone="6666666666"
    )

    assert second_result["succeed"] is False
    assert second_result["message"] == "Email is already registered"  
    
def test_register_customer_short_password():
    result = register_customer(
        first_name="Test",
        last_name="Customer",
        email="short.password@example.com",
        password="short",
        phone="7777777777"
    )

    assert result["succeed"] is False
    assert result["message"] == "Password must be at least 8 characters"            

def test_register_customer_empty_first_name():
    result = register_customer(
        first_name="",
        last_name="Customer",
        email="empty.firstname@example.com",
        password="TestPassword123",
        phone="7777777777"
    )

    assert result["succeed"] is False
    assert result["message"] == "First name is required"
    
def test_decode_expired_token():
    import jwt
    from datetime import datetime, timedelta, timezone
    from auth.jwt import SECRET_KEY, ALGORITHM

    expired_payload = {
        "sub": "1",
        "role_id": 2,
        "role_name": "Customer",
        "exp": datetime.now(timezone.utc) - timedelta(minutes=1)
    }

    expired_token = jwt.encode(
        expired_payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    result = decode_access_token(expired_token)

    assert result["succeed"] is False
    assert result["message"] == "Token has expired"
    
def test_decode_malformed_token():
    result = decode_access_token(
        "this-is-not-a-valid-jwt"
    )

    assert result["succeed"] is False
    assert result["message"] == "Invalid token"            