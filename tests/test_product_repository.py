from repositories.product_repository import (
    get_product_listing,
    get_product_by_id,
    search_products,
    get_products_by_category,
    get_products_by_subcategory
)


def test_get_product_listing():
    result = get_product_listing(
        None,
        None,
        None,
        None,
        "asc",
        1,
        10
    )

    assert result["succeed"] is True
    assert len(result["data"]) > 0


def test_search_products():
    result = search_products("saree")

    assert result["succeed"] is True
    assert len(result["data"]) >= 2


def test_get_product_by_id():
    result = get_product_by_id(1)

    assert result["succeed"] is True
    assert result["data"][0] == 1
    assert result["data"][1] == "Silk Saree"


def test_products_by_category():
    result = get_products_by_category(1)

    assert result["succeed"] is True
    assert len(result["data"]) > 0


def test_products_by_subcategory():
    result = get_products_by_subcategory(1)

    assert result["succeed"] is True
    assert len(result["data"]) > 0


def test_product_listing_price_ascending():
    result = get_product_listing(
        None,
        None,
        None,
        "price",
        "asc",
        1,
        10
    )

    assert result["succeed"] is True

    prices = [row[3] for row in result["data"]]

    assert prices == sorted(prices)


def test_product_listing_price_descending():
    result = get_product_listing(
        None,
        None,
        None,
        "price",
        "desc",
        1,
        10
    )

    assert result["succeed"] is True

    prices = [row[3] for row in result["data"]]

    assert prices == sorted(prices, reverse=True)


def test_product_listing_pagination():
    result = get_product_listing(
        None,
        None,
        None,
        None,
        "asc",
        1,
        2
    )

    assert result["succeed"] is True
    assert len(result["data"]) <= 2