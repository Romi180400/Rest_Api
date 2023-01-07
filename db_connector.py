import pymysql

import datetime


class user_connector:

    def add_user(user_id, username):
        """
        This function adds a user to the database with the given parameters 

        Args:
        user_id (int): The User ID
        username (str): The User name
        """
        conn = pymysql.connect(host='sql.freedb.tech',
                               port=3306,
                               user='freedb_freedb_test123456',
                               passwd='UWk2nu8b8#2%82G',
                               db='freedb_sql.freedb.tech2')
        conn.autocommit(True)

        cursor = conn.cursor()

        cursor.execute(
            f"INSERT into users (name, id, created) VALUES ('{username}', {user_id}, '{datetime.datetime.now()}')"
        )

        cursor.close()
        conn.close()

    def GetUserByID(user_id):
        """Getting the User details by the User ID

        Args:
        user_id (int): The User ID

        Returns:
        [tuple]: [Return the row of the user table selected by the User ID]
        """
        conn = pymysql.connect(host='sql.freedb.tech',
                               port=3306,
                               user='freedb_freedb_test123456',
                               passwd='UWk2nu8b8#2%82G',
                               db='freedb_sql.freedb.tech2')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

        value = cursor.fetchone()
        cursor.close()
        conn.close()
        return value

    def GetAllUsers():
        """Return all users from the users table

        Returns:
        [tuple]: [All the users]
        """
        conn = pymysql.connect(host='sql.freedb.tech',
                               port=3306,
                               user='freedb_freedb_test123456',
                               passwd='UWk2nu8b8#2%82G',
                               db='freedb_sql.freedb.tech2')
        conn.autocommit(True)

        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM users")
        value = cursor.fetchall()
        cursor.close()
        conn.close()
        return value

    def UpdateUser(user_id, user_name):
        """
        This function update a user in the database with the given parameters 

        Args:
        user_id (int): The User ID
        username (str): The User name
        """

        conn = pymysql.connect(host='sql.freedb.tech',
                           port=3306,
                           user='freedb_freedb_test123456',
                           passwd='UWk2nu8b8#2%82G',
                           db='freedb_sql.freedb.tech2')
        conn.autocommit(True)

        cursor = conn.cursor()

        cursor.execute(
        f"UPDATE users SET name = '{user_name}' WHERE id = {user_id}")

        cursor.close()
        conn.close()


    def DeleteUser(user_id):
        """
        This function deletes a user from the database with the given parameter

        Args:
            user_id (int): The User ID
        """
        conn = pymysql.connect(host='sql.freedb.tech',
                           port=3306,
                           user='freedb_freedb_test123456',
                           passwd='UWk2nu8b8#2%82G',
                           db='freedb_sql.freedb.tech2')
        conn.autocommit(True)

        cursor = conn.cursor()

        cursor.execute(f"DELETE FROM users WHERE id = {user_id}")

        cursor.close()
        conn.close()


    def getUserName(user_id):
        """This function gets and returns a user name from the database with the given parameter

        Args:
        user_id ([int]): [The User ID]

        Returns:
        [str]: [The User name]
        """
        conn = pymysql.connect(host='sql.freedb.tech',
                           port=3306,
                           user='freedb_freedb_test123456',
                           passwd='UWk2nu8b8#2%82G',
                           db='freedb_sql.freedb.tech2')
        cursor = conn.cursor()

        cursor.execute(f"SELECT name FROM users WHERE id = {user_id}")

        value = cursor.fetchone()
        cursor.close()
        conn.close()

        return value[0]
