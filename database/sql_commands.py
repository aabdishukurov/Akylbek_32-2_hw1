import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_db(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.commit()

    def sql_insert_user_command(self, telegram_id, username,
                                first_name, last_name):
        self.cursor.execute(sql_queries.START_INSERT_USER_QUERY,
                            (None,
                             telegram_id,
                             username,
                             first_name,
                             last_name)
                            )
        self.connection.commit()

    def sql_admin_select_user_command(self):
        self.cursor.row_factory = lambda cursor, row:{
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3]
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY
        )