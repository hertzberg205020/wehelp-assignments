/*
SQLyog Ultimate v11.25 (64 bit)
MySQL - 8.0.27 : Database - website
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`website` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `website`;

/*Table structure for table `member` */

DROP TABLE IF EXISTS `member`;

CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `member` */

insert  into `member`(`id`,`name`,`username`,`password`,`follower_count`,`time`) values (1,'test2','test','test',0,'2022-01-24 22:57:29'),(2,'name2','account2','pwd2',0,'2022-01-24 22:59:10'),(3,'name3','account3','pwd3',0,'2022-01-24 22:59:10'),(4,'name4','account4','pwd4',0,'2022-01-24 22:59:10'),(5,'name5','account5','pwd5',0,'2022-01-24 22:59:10');

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `member_id` bigint NOT NULL,
  `content` varchar(255) NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `message` */

insert  into `message`(`id`,`member_id`,`content`,`time`) values (1,1,'test comment','2022-01-24 23:11:27'),(2,2,'name2 comment','2022-01-24 23:11:27'),(3,3,'name3 comment','2022-01-24 23:11:27'),(4,4,'name4 comment','2022-01-24 23:11:27'),(5,5,'name5 comment','2022-01-24 23:11:27');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
