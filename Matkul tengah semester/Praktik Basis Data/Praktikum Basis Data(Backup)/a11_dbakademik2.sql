-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: 10.252.0.151    Database: a11_dbakademik2
-- ------------------------------------------------------
-- Server version	8.0.43-34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `mata_kuliah`
--

DROP TABLE IF EXISTS `mata_kuliah`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mata_kuliah` (
  `Kode_matkul` varchar(7) NOT NULL,
  `Mata_Kuliah` varchar(20) NOT NULL,
  `Sks` int NOT NULL,
  `Semester` int NOT NULL,
  PRIMARY KEY (`Kode_matkul`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mata_kuliah`
--

LOCK TABLES `mata_kuliah` WRITE;
/*!40000 ALTER TABLE `mata_kuliah` DISABLE KEYS */;
INSERT INTO `mata_kuliah` VALUES ('EE-110','Struktur Data',3,1),('EE-111','K3',2,1),('EE-310','Basis Data',3,4),('Ku-234','Bahasa Indonesia',2,2),('Mma-115','Matematika',3,1);
/*!40000 ALTER TABLE `mata_kuliah` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_mahasiswa`
--

DROP TABLE IF EXISTS `tbl_mahasiswa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_mahasiswa` (
  `Nim` int NOT NULL,
  `Nama` varchar(20) NOT NULL,
  `Alamat` tinytext NOT NULL,
  `Tgl_Lahir` date NOT NULL,
  `Data_foto` mediumblob,
  `Tipe_foto` varchar(50) DEFAULT NULL,
  `tempat_lahir` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Nim`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_mahasiswa`
--

LOCK TABLES `tbl_mahasiswa` WRITE;
/*!40000 ALTER TABLE `tbl_mahasiswa` DISABLE KEYS */;
INSERT INTO `tbl_mahasiswa` VALUES (980001,'Ali Akbar','Jl. Merdeka 10, jakarta 40121','1979-01-02',NULL,'png',NULL),(980002,'Budi haryanto','Jl Gajah Mada 2,jakarta','1978-10-06',NULL,'jpg',NULL),(980003,'Imam Faisal','Kom.Griya Asri D-2 Depok 40151','1978-05-13',NULL,NULL,NULL),(980004,'Indah Susanti','Jl.Adil No. 123 Bogor 43212','1979-06-21',NULL,NULL,NULL);
/*!40000 ALTER TABLE `tbl_mahasiswa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_nilai`
--

DROP TABLE IF EXISTS `tbl_nilai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_nilai` (
  `No` int NOT NULL AUTO_INCREMENT,
  `kd_matkul` varchar(20) NOT NULL,
  `nim` int NOT NULL,
  `Index_nilai` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`No`),
  KEY `kd_matkul` (`kd_matkul`),
  KEY `nim` (`nim`),
  CONSTRAINT `tbl_nilai_ibfk_1` FOREIGN KEY (`kd_matkul`) REFERENCES `mata_kuliah` (`Kode_matkul`),
  CONSTRAINT `tbl_nilai_ibfk_2` FOREIGN KEY (`nim`) REFERENCES `tbl_mahasiswa` (`Nim`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_nilai`
--

LOCK TABLES `tbl_nilai` WRITE;
/*!40000 ALTER TABLE `tbl_nilai` DISABLE KEYS */;
INSERT INTO `tbl_nilai` VALUES (1,'EE-110',980001,'A'),(2,'EE-110',980004,'B'),(3,'EE-111',980001,NULL),(4,'EE-111',980002,NULL),(5,'Ku-234',980004,'B'),(6,'Mma-115',980001,'C');
/*!40000 ALTER TABLE `tbl_nilai` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-14 13:07:23
