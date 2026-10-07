import strawberry

from shopsy_graphql.queries import Query
from auth.mutations import Mutation


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)