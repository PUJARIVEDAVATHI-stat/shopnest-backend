from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from shopsy_graphql.schema import schema

app = FastAPI(title="ShopNest Backend")

graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def home():
    return {
        "message": "Welcome to ShopNest Backend 🚀"
    }