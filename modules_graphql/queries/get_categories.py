from graphene import ObjectType, List

from modules_graphql.shared.category_response import CategoryResponse
from services.product_service import get_categories


class GetCategories(ObjectType):

    getCategories = List(CategoryResponse)

    @staticmethod
    async def resolve_getCategories(root, info):

        result = get_categories()

        if not result["succeed"]:
            return []

        category_list = []

        for row in result["data"]:

            category = CategoryResponse(
                categoryId=row[0],
                categoryName=row[1],
                description=row[2]
            )

            category_list.append(category)

        return category_list