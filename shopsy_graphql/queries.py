import strawberry

from services.product_service import (
    get_categories,
    get_products,
    get_product_by_id,
    get_products_by_category,
    get_products_by_subcategory,
    search_products,
    get_products_sorted,
    get_product_listing
)

from shopsy_graphql.types import (
    CategoryType,
    ProductType,
    ProductSort,
    ProductSortField,
    SortOrder
)



@strawberry.type
class Query:

    @strawberry.field
    def categories(self) -> list[CategoryType]:

        result = get_categories()

        if not result["succeed"]:
            return []

        return [
            CategoryType(
                category_id=row[0],
                category_name=row[1],
                description=row[2]
            )
            for row in result["data"]
        ]

    @strawberry.field
    def products(
        self,
        search: str | None = None,
        category_id: int | None = None,
        subcategory_id: int | None = None,
        sort_by: ProductSortField | None = None,
        sort_order: SortOrder = SortOrder.ASC,
        page: int = 1,
        page_size: int = 10
    ) -> list[ProductType]:

        if page < 1:
            raise ValueError("Page must be greater than or equal to 1")

        if page_size < 1:
            raise ValueError("Page size must be greater than or equal to 1")

        if page_size > 100:
            raise ValueError("Page size cannot exceed 100")
        
        if search is not None:
            search = search.strip()

            if not search:
                raise ValueError("Search cannot be empty")

            if len(search) > 100:
                raise ValueError("Search cannot exceed 100 characters")

        if category_id is not None and category_id < 1:
            raise ValueError("Category ID must be greater than or equal to 1")

        if subcategory_id is not None and subcategory_id < 1:
            raise ValueError("Subcategory ID must be greater than or equal to 1")

        result = get_product_listing(
            search,
            category_id,
            subcategory_id,
            sort_by.value if sort_by else None,
            sort_order.value,
            page,
            page_size
        )

        if not result["succeed"]:
            raise Exception(result.get("message", "Unable to fetch products"))

        return [
            ProductType(
                product_id=row[0],
                product_name=row[1],
                brand=row[2],
                price=row[3],
                stock_quantity=row[4]
            )
            for row in result["data"]
        ]
   
    @strawberry.field
    def product(self, product_id: int) -> ProductType | None:

        result = get_product_by_id(product_id)

        if not result["succeed"]:
            return None

        if result["data"] is None:
            return None

        row = result["data"]

        return ProductType(
            product_id=row[0],
            product_name=row[1],
            brand=row[2],
            price=row[3],
            stock_quantity=row[4]
        )    
   
    @strawberry.field
    def products_by_category(self, category_id: int) -> list[ProductType]:

        result = get_products_by_category(category_id)

        if not result["succeed"]:
            return []

        return [
            ProductType(
                product_id=row[0],
                product_name=row[1],
                brand=row[2],
                price=row[3],
                stock_quantity=row[4]
            )
            for row in result["data"]
        ]     
    @strawberry.field
    def products_by_subcategory(
        self,
        subcategory_id: int
    ) -> list[ProductType]:

        result = get_products_by_subcategory(subcategory_id)

        if not result["succeed"]:
            return []

        return [
            ProductType(
                product_id=row[0],
                product_name=row[1],
                brand=row[2],
                price=row[3],
                stock_quantity=row[4]
            )
            for row in result["data"]
        ]       
    @strawberry.field
    def search_products(
        self,
        keyword: str
    ) -> list[ProductType]:

        result = search_products(keyword)

        if not result["succeed"]:
            return []

        return [
            ProductType(
                product_id=row[0],
                product_name=row[1],
                brand=row[2],
                price=row[3],
                stock_quantity=row[4]
            )
            for row in result["data"]
        ]        
    @strawberry.field
    def products_sorted(
        self,
        sort_by: ProductSort
    ) -> list[ProductType]:

        result = get_products_sorted(sort_by.value)

        if not result["succeed"]:
            return []

        return [
            ProductType(
                product_id=row[0],
                product_name=row[1],
                brand=row[2],
                price=row[3],
                stock_quantity=row[4]
            )
            for row in result["data"]
        ]        