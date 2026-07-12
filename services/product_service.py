from database.db import get_connection


def get_categories():
    """
    Fetch all active categories.
    """

    connection = None

    try:
        connection = get_connection()

        cursor = connection.cursor()

        query = """
            SELECT
                category_id,
                category_name,
                description
            FROM shopnest.category
            WHERE is_active = TRUE
            ORDER BY category_name;
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        return {
            "succeed": True,
            "data": rows,
            "msg": ""
        }

    except Exception as error:

        return {
            "succeed": False,
            "data": [],
            "msg": str(error)
        }

    finally:

        if connection:
            connection.close()
            
def get_products():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
      SELECT
                p.product_id,
                p.product_name,
                p.brand,
                p.price,
                i.quantity
            FROM shopnest.product p
            INNER JOIN shopnest.inventory i
                ON p.product_id = i.product_id
            ORDER BY p.product_id;
        """)

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return {
            "succeed": True,
            "data": data
        }

    except Exception as e:
        return {
            "succeed": False,
            "message": str(e)
        }
def get_product_by_id(product_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                p.product_id,
                p.product_name,
                p.brand,
                p.price,
                i.quantity
            FROM shopnest.product p
            INNER JOIN shopnest.inventory i
                ON p.product_id = i.product_id
            WHERE p.product_id = %s;
        """, (product_id,))

        data = cursor.fetchone()

        cursor.close()
        conn.close()

        return {
            "succeed": True,
            "data": data
        }

    except Exception as e:
        return {
            "succeed": False,
            "message": str(e)
        }        
def get_products_by_category(category_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
    SELECT
        p.product_id,
        p.product_name,
        p.brand,
        p.price,
        i.quantity
    FROM shopnest.product p
    INNER JOIN shopnest.inventory i
        ON p.product_id = i.product_id
    INNER JOIN shopnest.subcategory s
        ON p.subcategory_id = s.subcategory_id
    WHERE s.category_id = %s
    ORDER BY p.product_id;
""", (category_id,))

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return {
            "succeed": True,
            "data": data
        }

    except Exception as e:
        return {
            "succeed": False,
            "message": str(e)
        }        

def get_products_by_subcategory(subcategory_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                p.product_id,
                p.product_name,
                p.brand,
                p.price,
                i.quantity
            FROM shopnest.product p
            INNER JOIN shopnest.inventory i
                ON p.product_id = i.product_id
            WHERE p.subcategory_id = %s
            ORDER BY p.product_id;
        """, (subcategory_id,))

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return {
            "succeed": True,
            "data": data
        }

    except Exception as e:
        return {
            "succeed": False,
            "message": str(e)
        }        
def search_products(keyword):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                p.product_id,
                p.product_name,
                p.brand,
                p.price,
                i.quantity
            FROM shopnest.product p
            INNER JOIN shopnest.inventory i
                ON p.product_id = i.product_id
            WHERE
                LOWER(p.product_name) LIKE LOWER(%s)
                OR LOWER(p.brand) LIKE LOWER(%s)
            ORDER BY p.product_name;
        """, (f"%{keyword}%", f"%{keyword}%"))

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return {
            "succeed": True,
            "data": data
        }

    except Exception as e:
        return {
            "succeed": False,
            "message": str(e)
        }    
def get_products_sorted(sort_by):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        order_by = {
            "PRICE_ASC": "p.price ASC",
            "PRICE_DESC": "p.price DESC",
            "NAME_ASC": "p.product_name ASC",
            "NAME_DESC": "p.product_name DESC"
        }.get(sort_by, "p.product_id ASC")

        query = f"""
            SELECT
                p.product_id,
                p.product_name,
                p.brand,
                p.price,
                i.quantity
            FROM shopnest.product p
            INNER JOIN shopnest.inventory i
                ON p.product_id = i.product_id
            ORDER BY {order_by};
        """

        cursor.execute(query)

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return {
            "succeed": True,
            "data": data
        }

    except Exception as e:
        return {
            "succeed": False,
            "message": str(e)
        }            