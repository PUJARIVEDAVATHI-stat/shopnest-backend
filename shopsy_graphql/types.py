import strawberry
import enum


@strawberry.type
class CategoryType:
    category_id: int
    category_name: str
    description: str | None


@strawberry.type
class ProductType:
    product_id: int
    product_name: str
    brand: str
    price: float
    stock_quantity: int
    
@strawberry.enum
class ProductSort(enum.Enum):
    PRICE_ASC = "PRICE_ASC"
    PRICE_DESC = "PRICE_DESC"
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"

@strawberry.enum
class ProductSortField(enum.Enum):
    PRICE = "price"
    NAME = "name"


@strawberry.enum
class SortOrder(enum.Enum):
    ASC = "asc"
    DESC = "desc"        