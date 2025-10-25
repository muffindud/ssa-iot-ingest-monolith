from services.postgres import Database


db = Database()


def get_user_from_db(username: str) -> dict | None:
    result = db.execute_query(
        "SELECT id, username, password_hash FROM users WHERE username = %s",
        (username,)
    )[0]

    if result:
        user_id, username, password_hash, roles = result
        return {
            'id': user_id,
            'username': username,
            'password_hash': password_hash
        }

    return None


def create_user_in_db(username: str, password_hash: bytes) -> int:
    result = db.execute_query(
        "INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING id",
        (username, password_hash)
    )

    user_id = result[0][0]
    return user_id


def get_user_device_ids(user_id: int) -> list[int]:
    results = db.execute_query(
        "SELECT device_id FROM devices WHERE user_id = %s",
        (user_id,)
    )

    device_ids = [row[0] for row in results]
    return device_ids


def truncate_user_data() -> None:
    db.execute_query("TRUNCATE TABLE user_devices")
    db.execute_query("TRUNCATE TABLE users")
    db.execute_query("TRUNCATE TABLE devices")
