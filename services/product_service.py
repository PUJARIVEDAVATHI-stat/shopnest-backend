from repositories.product_repository import (
    get_categories as repo_get_categories,
    get_products as repo_get_products,
    get_product_by_id as repo_get_product_by_id,
    get_products_by_category as repo_get_products_by_category,
    get_products_by_subcategory as repo_get_products_by_subcategory,
    search_products as repo_search_products,
    get_products_sorted as repo_get_products_sorted,
    get_product_listing as repo_get_product_listing
)


def get_categories():
    return repo_get_categories()


def get_products():
    return repo_get_products()


def get_product_by_id(product_id):
    return repo_get_product_by_id(product_id)


def get_products_by_category(category_id):
    return repo_get_products_by_category(category_id)


def get_products_by_subcategory(subcategory_id):
    return repo_get_products_by_subcategory(subcategory_id)


def search_products(keyword):
    return repo_search_products(keyword)


def get_products_sorted(sort_by):
    return repo_get_products_sorted(sort_by)


def get_product_listing(
    search,
    category_id,
    subcategory_id,
    sort_by,
    sort_order,
    page,
    page_size
):
    return repo_get_product_listing(
        search,
        category_id,
        subcategory_id,
        sort_by,
        sort_order,
        page,
        page_size
    )