from fastapi import FastAPI, Request
from strawberry.fastapi import GraphQLRouter

from shopsy_graphql.schema import schema
from auth.context import get_current_user


app = FastAPI()


async def get_context(request: Request):
    authorization = request.headers.get("Authorization")

    token = None

    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ", 1)[1]

    current_user = get_current_user(token)

    return {
        "request": request,
        "current_user": current_user
    }


graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context
)

app.include_router(
    graphql_app,
    prefix="/graphql"
)