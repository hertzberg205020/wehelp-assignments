import mysql.connector
from mysql.connector import Error, pooling

from entity.member import Member


class MysqlUtil:
    __conn_pool = None

    def __init__(self):
        self.__conn = None
        self.__cursor = None

    def __init_database(self):
        try:
            self.__conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="abc123"
            )
            self.__cursor = self.__conn.cursor()
            sql = """
            CREATE DATABASE IF NOT EXISTS member_system_db CHARACTER SET 'utf8mb4'
            """
            self.__cursor.execute(sql)
            self.__conn.commit()
        except Error as e:
            print(e)
        finally:
            if self.__conn.is_connected():
                self.__cursor.close()
                self.__conn.close()

    def connect(self):
        if self.__conn_pool is None:
            self.__init_database()
            try:
                self.__conn_pool = pooling.MySQLConnectionPool(
                    pool_name="pynative_pool",
                    pool_size=5,
                    pool_reset_session=True,
                    host='localhost',
                    database='member_system_db',
                    user='root',
                    password='abc123'
                )
            except Error as e:
                print(e)

        self.__conn = self.__conn_pool.get_connection()
        if self.__conn.is_connected():
            return self.__conn



    @property
    def conn(self):
        return self.__conn

    @property
    def cursor(self):
        return self.__cursor

    def create_cursor(self):
        conn = self.connect()
        try:
            self.__cursor = conn.cursor(dictionary=True)
        except Error as e:
            print(e)

        return self.__cursor

    def disconnect(self):
        if self.__cursor is not None:
            self.__cursor.close()
        print(self.__conn)
        if self.__conn.is_connected():
            self.__conn.close()


class MemberDao:
    def __init__(self):
        self.__util = MysqlUtil()
        self.__table = False

    def __init_table(self):
        try:
            self.__util.create_cursor()
            sql = """
            CREATE TABLE IF NOT EXISTS member(
                id BIGINT PRIMARY KEY AUTO_INCREMENT,
                `name` VARCHAR(255) NOT NULL,
                username VARCHAR(255) NOT NULL UNIQUE,
                `password` VARCHAR(255) NOT NULL,
                follower_count INT NOT NULL DEFAULT 0,
                `time` DATETIME NOT NULL DEFAULT NOW()
            )
            """
            self.__util.create_cursor()
            self.__util.cursor.execute(sql)
            self.__util.conn.commit()
        except Error as e:
            print(e)
        finally:
            self.__util.disconnect()
            self.__table = True

    def insert(self, member: Member):
        if not self.__table:
            self.__init_table()

        try:
            self.__util.create_cursor()
            sql = """INSERT INTO member(name, userName, password) VALUES (%s, %s, %s);"""
            new_data = (member.name, member.userName, member.password)
            self.__util.cursor.execute(sql, new_data)
            self.__util.conn.commit()

        except Error as e:
            print(e)
        finally:
            self.__util.disconnect()

    def is_valid_create_account(self, member: Member):
        rs = None
        try:
            self.__util.create_cursor()
            sql = """
            select id from member where userName = %s
            """
            self.__util.cursor.execute(sql, (member.userName,))
            rs = self.__util.cursor.fetchone()
        except Error as e:
            print(e)
        finally:
            self.__util.disconnect()
            return rs is None

    def is_valid(self, member: Member):
        rs = None
        try:
            self.__util.create_cursor()
            sql = """
            select id from member where userName = %s and password = %s
            """
            self.__util.cursor.execute(sql, (member.userName, member.password))
            rs = self.__util.cursor.fetchone()
        except Error as e:
            print(e)
        finally:
            self.__util.disconnect()
            return rs is not None

    def query_user(self, member: Member):
        try:
            self.__util.create_cursor()
            sql = """
            select id, name, username from member where username = %s
            """
            self.__util.cursor.execute(sql, (member.userName,))
            rs = self.__util.cursor.fetchone()
        except Error as e:
            print(e)
        finally:
            self.__util.disconnect()
            return rs

    def rename(self, member: Member, new_name):
        status = True
        try:
            self.__util.create_cursor()
            sql = """
            update member set `name` = %s where username = %s
            """
            self.__util.cursor.execute(sql, (new_name, member.userName))
            self.__util.conn.commit()
        except Error as e:
            print()
            status = False
        finally:
            self.__util.disconnect()
            return status


def main():
    memberDao = MemberDao()
    member = Member(userName='account2')
    res = memberDao.rename(member, 'Alice')
    print(res)
    # member = Member(None, "name1", "account1", "password1")
    # memberDao.insert(member)
    # print('result', memberDao.is_valid_create_account(member))
    # print(memberDao.is_valid(member))


if __name__ == "__main__":
    main()
