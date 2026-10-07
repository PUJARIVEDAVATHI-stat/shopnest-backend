from auth.jwt import decode_access_token


def get_current_user(token: str):
    if not token:
        return {
            "succeed": False,
            "message": "Authentication token is required"
        }

    result = decode_access_token(token)

    if not result["succeed"]:
        return result

    payload = result["data"]

    return {
        "succeed": True,
        "data": {
            "user_id": int(payload["sub"]),
            "role_id": payload["role_id"],
            "role_name": payload["role_name"]
        }
    }


def require_authenticated_user(info):
    context = info.context

    current_user = context.get("current_user")

    if not current_user or not current_user["succeed"]:
        raise ValueError(
            current_user["message"]
            if current_user
            else "Authentication required"
        )

    return current_user["data"]


def require_role(info, allowed_roles: list[str]):
    user = require_authenticated_user(info)

    if user["role_name"] not in allowed_roles:
        raise ValueError("You do not have permission to access this resource")

    return user