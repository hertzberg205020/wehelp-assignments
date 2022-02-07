import mysql.connector
from mysql.connector import Error

from entity.member import Member


class MysqlUtil:
    def __init__(self):
        self.__conn = None
        self.__cursor = None

    def connect(self):
        try:
            self.__conn = mysql.connector.connect(
                host="localhost",
                database="member_system_db",
                user="root",
                password="abc123"
            )
            if self.__conn.is_connected():
                return self.__conn

        except Error as e:
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
                    self.connect()

    @property
    def conn(self):
        return self.__conn

    @property
    def cursor(self):
        return self.__cursor

    def create_cursor(self):
        conn = self.connect()
        try:
            self.__cursor = conn.cursor()
        except Error as e:
            print(e)
        return self.__cursor

    def disconnect(self):
        if self.__cursor is not None:
            self.__cursor.close()
        if self.__conn.is_connected:
            self.__conn.close()


class MemberDao:
    def __init__(self):
        self.__util = MysqlUtil()

    def insert(self, member: Member):
        try:
            sql = """INSERT INTO member(name, userName, password) VALUES (%s, %s, %s);"""
            new_data = (member.name, member.userName, member.password)

            self.__util.cursor.execute(sql, new_data)
            self.__util.conn.commit()

        except Error as e:
            try:
                sql = """
                CREATE TABLE IF NOT EXISTS member(
                    id BIGINT PRIMARY KEY AUTO_INCREMENT,
                    `name` VARCHAR(255) NOT NULL,
                    username VARCHAR(255) NOT NULL,
                    `password` VARCHAR(255) NOT NULL,
                    follower_count INT NOT NULL DEFAULT 0,
                    `time` DATETIME NOT NULL DEFAULT NOW()
                )
                """
                self.__util.create_cursor()
                self.__util.cursor.execute(sql)
                self.__util.conn.commit()
                self.insert(member)
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
            print(rs)
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


def main():
    memberDao = MemberDao()
    member = Member("name", "account", "password")
    print(memberDao.is_valid_create_account(member))
    # print(memberDao.is_valid(member))


if __name__ == "__main__":
    main()
