# Assignment - Week 5

## 要求二：建立資料庫和資料表

建立一個新的資料庫，取名字為website

```mysql
CREATE DATABASE IF NOT EXISTS website CHARACTER SET 'utf8mb4';
```

![2-1.JPG](./Figs/2-1.JPG)

在資料庫中，建立會員資料表，取名字為member

```mysql
USE website;
CREATE TABLE IF NOT EXISTS member(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    follower_count INT NOT NULL DEFAULT 0,
    `time` DATETIME NOT NULL DEFAULT NOW()
);
```

![2-2.jpg](./Figs/2-2.jpg)



## 要求三：SQL CRUD

使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

```mysql
INSERT INTO member(`name`, username, `password`)
VALUES ('name1', 'test', 'test');
INSERT INTO member(`name`, username, `password`)
VALUES 
('name2', 'account2', 'pwd2'),
('name3', 'account3', 'pwd3'),
('name4', 'account4', 'pwd4'),
('name5', 'account5', 'pwd5');
```

![3-1.jpg](./Figs/3-1.jpg)

![3-2.jpg](./Figs/3-2.jpg)

使用 SELECT 指令取得所有在 member 資料表中的會員資料。

```mysql
SELECT * FROM member;
```

![3-2.jpg](./Figs/3-2.jpg)

使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排。

```mysql
SELECT *
FROM member
ORDER BY `time` DESC;
```

![3-3.jpg](./Figs/3-3.jpg)

使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。

```mysql
SELECT *
FROM member
ORDER BY `time` DESC
LIMIT 1, 3;
```

![3-4.jpg](./Figs/3-4.jpg)

使用 SELECT 指令取得欄位 username 是 test 的會員資料。

```mysql
SELECT *
FROM member
WHERE username = 'test';
```

![3-5.jpg](./Figs/3-5.jpg)

使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

```mysql
SELECT *
FROM member
WHERE username = 'test'
AND `password` = 'test';
```

![3-5.jpg](./Figs/3-5.jpg)

使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

```mysql
UPDATE member
SET `name` = 'test2'
WHERE username = 'test';
```

![3-6.jpg](./Figs/3-6.jpg)

## 要求四：SQL Aggregate Functions

取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )

```mysql
SELECT COUNT(id)
FROM member;
```

![4-1.jpg](./Figs/4-1.jpg)

取得 member 資料表中，所有會員 follower_count 欄位的總和

```mysql
SELECT SUM(follower_count)
FROM member;
```

![4-2.jpg](./Figs/4-2.jpg)

取得 member 資料表中，所有會員 follower_count 欄位的平均數

```mysql
SELECT AVG(follower_count)
FROM member;
```

![4-3.jpg](./Figs/4-3.jpg)

## 要求五：SQL JOIN

建表

```mysql
CREATE TABLE IF NOT EXISTS message(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id BIGINT NOT NULL,
    FOREIGN KEY (member_id) REFERENCES member(id),
    content VARCHAR(255) NOT NULL,
    `time` DATETIME NOT NULL DEFAULT NOW()
)
INSERT INTO message(member_id, content)
VALUES
(1, 'test comment'),
(2, 'name2 comment'),
(3, 'name3 comment'),
(4, 'name4 comment'),
(5, 'name5 comment');
```

![5-1.jpg](./Figs/5-1.jpg)

使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名

```mysql
SELECT m.`name` AS "留言者", msg.`content` AS "流言"
FROM message msg JOIN member m
ON msg.`member_id` = m.`id`;
```

![5-2.jpg](./Figs/5-2.jpg)

使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。

```mysql
SELECT m.`name` AS "留言者", msg.`content` AS "流言"
FROM message msg JOIN member m
ON msg.`member_id` = m.`id`
WHERE m.`username` = 'test';
```

![5-3.jpg](./Figs/5-3.jpg)