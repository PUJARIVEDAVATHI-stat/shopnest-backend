from database.db import get_connection
from utils.logger import logger


def get_user_by_email(email):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT
                u.user_id,
                u.role_id,
                r.role_name,
                u.first_name,
                u.last_name,
                u.email,
                u.password_hash,
                u.phone,
                u.is_active,
                u.created_at
            FROM shopnest.users u
            INNER JOIN shopnest.role r
                ON u.role_id = r.role_id
            WHERE LOWER(u.email) = LOWER(%s)
        """

        cursor.execute(query, (email,))

        data = cursor.fetchone()

        cursor.close()
        conn.close()

        if not data:
            return {
                "succeed": False,
                "message": "User not found"
            }

        return {
            "succeed": True,
            "data": data
        }

    except Exception as e:
        logger.exception("User repository operation failed")

        return {
            "succeed": False,
            "message": "Unable to process user request"
        }
        
def create_user(
    first_name,
    last_name,
    email,
    password_hash,
    phone=None
):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO shopnest.users (
                role_id,
                first_name,
                last_name,
                email,
                password_hash,
                phone,
                is_active
            )
            VALUES (
                2,
                %s,
                %s,
                %s,
                %s,
                %s,
                TRUE
            )
            RETURNING user_id
        """

        cursor.execute(
            query,
            (
                first_name,
                last_name,
                email,
                password_hash,
                phone
            )
        )

        user_id = cursor.fetchone()[0]

        conn.commit()

        cursor.close()
        conn.close()

        return {
            "succeed": True,
            "data": {
                "user_id": user_id
            }
        }

    except Exception as e:
            logger.exception("User repository operation failed")
    
            return {
                "succeed": False,
                "message": "Unable to process user request"
            }