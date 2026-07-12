import strawberry

from shopsy_graphql.queries import Query
schema = strawberry.Schema(query=Query)