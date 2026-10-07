import strawberry


@strawberry.type
class LoginResponse:
    user_id: int
    role_id: int
    role_name: str
    first_name: str
    last_name: str | None
    email: str
    phone: str | None
    access_token: str
    
@strawberry.type
class RegistrationResponse:
    user_id: int
    role_id: int
    role_name: str
    first_name: str
    last_name: str | None
    email: str
    phone: str | None    