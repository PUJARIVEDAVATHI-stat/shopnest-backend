from graphene import ObjectType, Int, String


class CategoryResponse(ObjectType):
    categoryId = Int()
    categoryName = String()
    description = String()