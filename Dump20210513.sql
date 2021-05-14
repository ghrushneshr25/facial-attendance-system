-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: localhost    Database: attendance
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `0vp57pd01p2q6gnn`
--

DROP TABLE IF EXISTS `0vp57pd01p2q6gnn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `0vp57pd01p2q6gnn` (
  `ROLLNO` varchar(8) NOT NULL,
  `ATTENDANCESTATUS` varchar(2) NOT NULL DEFAULT 'A',
  `NAME` varchar(100) NOT NULL,
  PRIMARY KEY (`ROLLNO`),
  CONSTRAINT `0VP57PD01P2Q6GNNconstraint` FOREIGN KEY (`ROLLNO`) REFERENCES `studentdetails` (`ROLLNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `0vp57pd01p2q6gnn`
--

LOCK TABLES `0vp57pd01p2q6gnn` WRITE;
/*!40000 ALTER TABLE `0vp57pd01p2q6gnn` DISABLE KEYS */;
/*!40000 ALTER TABLE `0vp57pd01p2q6gnn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `7up83g0b7wfrokrn`
--

DROP TABLE IF EXISTS `7up83g0b7wfrokrn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `7up83g0b7wfrokrn` (
  `ROLLNO` varchar(8) NOT NULL,
  `ATTENDANCESTATUS` varchar(2) NOT NULL DEFAULT 'A',
  `NAME` varchar(100) NOT NULL,
  PRIMARY KEY (`ROLLNO`),
  CONSTRAINT `7UP83G0B7WFROKRNconstraint` FOREIGN KEY (`ROLLNO`) REFERENCES `studentdetails` (`ROLLNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `7up83g0b7wfrokrn`
--

LOCK TABLES `7up83g0b7wfrokrn` WRITE;
/*!40000 ALTER TABLE `7up83g0b7wfrokrn` DISABLE KEYS */;
INSERT INTO `7up83g0b7wfrokrn` VALUES ('18CE1011','A','Amit Patil');
/*!40000 ALTER TABLE `7up83g0b7wfrokrn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qwertyuipsoda`
--

DROP TABLE IF EXISTS `qwertyuipsoda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qwertyuipsoda` (
  `ROLLNO` varchar(8) NOT NULL,
  `ATTENDANCESTATUS` varchar(2) NOT NULL DEFAULT 'A',
  `NAME` varchar(100) NOT NULL,
  PRIMARY KEY (`ROLLNO`),
  CONSTRAINT `uniquerollno` FOREIGN KEY (`ROLLNO`) REFERENCES `studentdetails` (`ROLLNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qwertyuipsoda`
--

LOCK TABLES `qwertyuipsoda` WRITE;
/*!40000 ALTER TABLE `qwertyuipsoda` DISABLE KEYS */;
/*!40000 ALTER TABLE `qwertyuipsoda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sessiontables`
--

DROP TABLE IF EXISTS `sessiontables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sessiontables` (
  `SESSIONID` varchar(20) NOT NULL,
  `YEAR` enum('FE','SE','TE','BE') NOT NULL,
  `DIV` varchar(5) NOT NULL,
  `STARTTIME` timestamp NULL DEFAULT NULL,
  `ENDTIME` timestamp NULL DEFAULT NULL,
  `BRANCH` enum('COMPUTER ENGINEERING','INFORMATION TECHNOLOGY','ELECTRONICS AND TELECOMMUNICATION ENGINEERING','ELECTRONICS ENGINEERING','INSTRUMENTATION ENGINEERING') NOT NULL,
  `FACULTYID` varchar(45) NOT NULL,
  `CREATETIME` timestamp NOT NULL,
  PRIMARY KEY (`SESSIONID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sessiontables`
--

LOCK TABLES `sessiontables` WRITE;
/*!40000 ALTER TABLE `sessiontables` DISABLE KEYS */;
INSERT INTO `sessiontables` VALUES ('033ZTPXV9VQMNA8I','TE','C','2021-05-08 17:47:38',NULL,'INFORMATION TECHNOLOGY','18CE7022','2021-05-08 17:47:35'),('0VP57PD01P2Q6GNN','TE','B','2021-05-13 16:19:57','2021-05-13 16:20:25','INFORMATION TECHNOLOGY','18CE7022','2021-05-13 16:19:53'),('5BQ45DI66AE4XMEZ','TE','C',NULL,NULL,'COMPUTER ENGINEERING','18CE7022','2021-05-08 17:41:28'),('7LUKX5GADNPWBZAO','TE','C','2021-05-08 17:48:16','2021-05-08 18:00:28','COMPUTER ENGINEERING','18CE7022','2021-05-08 17:48:13'),('7UP83G0B7WFROKRN','FE','A','2021-05-13 16:35:25',NULL,'INFORMATION TECHNOLOGY','18CE7022','2021-05-13 16:35:23'),('KP6ERZO7L7B9KUGD','TE','C',NULL,NULL,'COMPUTER ENGINEERING','18CE7022','2021-05-08 17:42:17'),('KSUI0WUB6AHPEIKG','TE','C',NULL,NULL,'COMPUTER ENGINEERING','18CE7022','2021-05-08 17:27:48'),('NW2WWQSU5Z3PSTEI','TE','C',NULL,NULL,'COMPUTER ENGINEERING','18CE7022','2021-05-08 17:36:28'),('PLZP9DJA8ZDYTOIM','TE','C',NULL,NULL,'COMPUTER ENGINEERING','18CE7022','2021-05-08 17:25:20'),('TZIJX1I1J0OAPL0S','TE','C',NULL,NULL,'COMPUTER ENGINEERING','18CE7022','2021-05-08 17:26:19');
/*!40000 ALTER TABLE `sessiontables` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_images`
--

DROP TABLE IF EXISTS `student_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_images` (
  `rollNo` varchar(8) NOT NULL,
  `studentPhoto` blob,
  PRIMARY KEY (`rollNo`),
  CONSTRAINT `studentRollNo` FOREIGN KEY (`rollNo`) REFERENCES `studentdetails` (`ROLLNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_images`
--

LOCK TABLES `student_images` WRITE;
/*!40000 ALTER TABLE `student_images` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studentdetails`
--

DROP TABLE IF EXISTS `studentdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `studentdetails` (
  `ROLLNO` varchar(8) NOT NULL,
  `NAME` text NOT NULL,
  `EMAIL ID` varchar(50) NOT NULL,
  `YEAR` enum('FE','SE','TE','BE') NOT NULL,
  `BRANCH` enum('COMPUTER ENGINEERING','INFORMATION TECHNOLOGY','ELECTRONICS AND TELECOMMUNICATION ENGINEERING','ELECTRONICS ENGINEERING','INSTRUMENTATION ENGINEERING') NOT NULL,
  `PASSWORD` varchar(30) NOT NULL,
  `DIV` varchar(2) NOT NULL,
  `role` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ROLLNO`),
  UNIQUE KEY `EMAIL ID` (`EMAIL ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studentdetails`
--

LOCK TABLES `studentdetails` WRITE;
/*!40000 ALTER TABLE `studentdetails` DISABLE KEYS */;
INSERT INTO `studentdetails` VALUES ('18CE1011','Amit Patil','amitpatil@gmail.com','FE','INFORMATION TECHNOLOGY','qwerty12345','A','student'),('18CE5434','Rushikesh Musale','rushikeshmusale@gmail.com','SE','ELECTRONICS AND TELECOMMUNICATION ENGINEERING','1234567','A','student'),('18CE6666','RAM CHANDRA SINGH','ram@chandra.com','TE','COMPUTER ENGINEERING','qwertyqwerty','C','student'),('18CE7022','SHUBHAM MORE','shubhammore@gmail.com','TE','COMPUTER ENGINEERING','pqrst12345','C','Faculty'),('18CE7029','GHRUSHNESH RATHOD','ghrushnesh0825@gmail.com','TE','COMPUTER ENGINEERING','abcd12345','C','student');
/*!40000 ALTER TABLE `studentdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'attendance'
--

--
-- Dumping routines for database 'attendance'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-13 22:08:56
