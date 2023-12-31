CREATE_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS telegram_users
        (ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        USERNAME CHAR(50),
        FIRST_NAME CHAR(50),
        LAST_NAME CHAR(50),
        REFERENCE_LINK TEXT NULL,
        UNIQUE (TELEGRAM_ID)
        )
"""

CREATE_USER_FORM_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS user_form
        (ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        NICKNAME CHAR(50),
        AGE INTEGER,
        BIO TEXT,
        MARRIED CHAR(50),
        PHOTO TEXT,
        UNIQUE (TELEGRAM_ID)
        )
"""
CREATE_LIKE_FORM_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS like_form
        (ID INTEGER PRIMARY KEY,
        OWNER_TELEGRAM_ID INTEGER,
        LIKER_TELEGRAM_ID INTEGER
        )
"""

CREATE_REFERENCE_USERS_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS reference_users
        (ID INTEGER PRIMARY KEY,
        OWNER_TELEGRAM_ID INTEGER,
        REFERENCE_TELEGRAM_ID INTEGER
        )
"""

START_INSERT_USER_QUERY = """INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?,?)"""

SELECT_USER_QUERY = """SELECT * FROM telegram_users"""

INSERT_USER_FORM_QUERY = """INSERT OR IGNORE INTO user_form VALUES (?,?,?,?,?,?,?)"""

SELECT_USER_FORM_BY_TELEGRAM_ID_QUERY = """
SELECT * FROM user_form WHERE TELEGRAM_ID = ?"""

SELECT_USER_FORM_QUERY = """SELECT * FROM user_form"""

INSERT_LIKE_FORM_QUERY = """INSERT OR IGNORE INTO like_form VALUES (?,?,?)"""

SELECT_LIKE_FORM_QUERY = """
SELECT * FROM like_form WHERE OWNER_TELEGRAM_ID = ? AND LIKER_TELEGRAM_ID = ?
"""
UPDATE_USER_FORM_QUERY = """
UPDATE user_form SET NICKNAME = ?, AGE = ?, BIO = ?, MARRIED = ?, PHOTO = ? WHERE TELEGRAM_ID = ?
"""

DELETE_USER_FORM_QUERY = """
DELETE FROM user_form WHERE TELEGRAM_ID = ?
"""

UPDATE_USER_BY_LINK_QUERY = """
UPDATE telegram_users SET REFERENCE_LINK = ? WHERE TELEGRAM_ID = ?
"""

SELECT_USER_LINK_QUERY = """
SELECT REFERENCE_LINK FROM telegram_users WHERE TELEGRAM_ID = ?"""

SELECT_OWNER_LINK_QUERY = """
SELECT TELEGRAM_ID FROM telegram_users WHERE REFERENCE_LINK = ?"""

INSERT_REFERENCE_USERS_QUERY = """
INSERT OR IGNORE INTO reference_users VALUES (?,?,?)"""

SELECT_EXIST_REFERENCE_QUERY = """
SELECT REFERENCE_TELEGRAM_ID FROM reference_users WHERE REFERENCE_TELEGRAM_ID = ?"""

SELECT_ALL_REFERENCE_QUERY = """
SELECT * FROM reference_users WHERE OWNER_TELEGRAM_ID = ?"""
