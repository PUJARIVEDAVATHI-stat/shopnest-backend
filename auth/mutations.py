import strawberry

from auth.types import LoginResponse, RegistrationResponse
from services.user_service import (
    authenticate_user,
    register_customer
)


@strawberry.type
class Mutation:

    @strawberry.mutation
    def login(
        self,
        email: str,
        password: str
    ) -> LoginResponse:

        result = authenticate_user(email, password)

        if not result["succeed"]:
            raise ValueError(result["message"])

        user = result["data"]

        return LoginResponse(
            user_id=user["user_id"],
            role_id=user["role_id"],
            role_name=user["role_name"],
            first_name=user["first_name"],
            last_name=user["last_name"],
            email=user["email"],
            phone=user["phone"],
            access_token=user["access_token"]
        )
    @strawberry.mutation
    def register(
        self,
        first_name: str,
        last_name: str | None,
        email: str,
        password: str,
        phone: str | None = None
    ) -> RegistrationResponse:

        result = register_customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone=phone
        )

        if not result["succeed"]:
            raise ValueError(result["message"])

        user = result["data"]

        return RegistrationResponse(
            user_id=user["user_id"],
            role_id=user["role_id"],
            role_name=user["role_name"],
            first_name=user["first_name"],
            last_name=user["last_name"],
            email=user["email"],
            phone=user["phone"]
        )    