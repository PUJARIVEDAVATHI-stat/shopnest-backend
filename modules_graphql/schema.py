import graphene

from modules_graphql.queries.get_categories import GetCategories


class Query(GetCategories, graphene.ObjectType):
    """
    Root Query
    """
    pass


schema = graphene.Schema(query=Query)