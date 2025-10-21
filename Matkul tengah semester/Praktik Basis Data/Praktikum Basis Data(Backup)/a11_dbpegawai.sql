-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: 10.252.0.151    Database: a11_dbpegawai
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
-- Table structure for table `karyawan_dep`
--

DROP TABLE IF EXISTS `karyawan_dep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `karyawan_dep` (
  `no_dep` char(4) DEFAULT NULL,
  `no_pegawai` int DEFAULT NULL,
  `tanggal_mulai` date DEFAULT NULL,
  `tanggal_selesai` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `karyawan_dep`
--

LOCK TABLES `karyawan_dep` WRITE;
/*!40000 ALTER TABLE `karyawan_dep` DISABLE KEYS */;
/*!40000 ALTER TABLE `karyawan_dep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manajer_dep`
--

DROP TABLE IF EXISTS `manajer_dep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manajer_dep` (
  `no_dep` char(4) DEFAULT NULL,
  `no_pegawai` int DEFAULT NULL,
  `tanggal_mulai` date DEFAULT NULL,
  `tanggal_selesai` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manajer_dep`
--

LOCK TABLES `manajer_dep` WRITE;
/*!40000 ALTER TABLE `manajer_dep` DISABLE KEYS */;
/*!40000 ALTER TABLE `manajer_dep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_departemen`
--

DROP TABLE IF EXISTS `tbl_departemen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_departemen` (
  `no_dep` char(4) NOT NULL,
  `nama_departemen` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`no_dep`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_departemen`
--

LOCK TABLES `tbl_departemen` WRITE;
/*!40000 ALTER TABLE `tbl_departemen` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_departemen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_gaji`
--

DROP TABLE IF EXISTS `tbl_gaji`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_gaji` (
  `no_pegawai` int DEFAULT NULL,
  `nominal_gaji` int DEFAULT NULL,
  `tanggal_mulai` date DEFAULT NULL,
  `tanggal_selesai` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_gaji`
--

LOCK TABLES `tbl_gaji` WRITE;
/*!40000 ALTER TABLE `tbl_gaji` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_gaji` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_jabatan`
--

DROP TABLE IF EXISTS `tbl_jabatan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_jabatan` (
  `no_pegawai` int NOT NULL,
  `jabatan` varchar(50) DEFAULT NULL,
  `tanggal_mulai` date DEFAULT NULL,
  `tanggal_selesai` date DEFAULT NULL,
  PRIMARY KEY (`no_pegawai`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_jabatan`
--

LOCK TABLES `tbl_jabatan` WRITE;
/*!40000 ALTER TABLE `tbl_jabatan` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_jabatan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_pegawai`
--

DROP TABLE IF EXISTS `tbl_pegawai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_pegawai` (
  `no_pegawai` int NOT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `nama_depan` varchar(14) DEFAULT NULL,
  `nama_tengah` varchar(30) DEFAULT NULL,
  `gelar_depan` varchar(5) DEFAULT NULL,
  `gelar_akhir` varchar(10) DEFAULT NULL,
  `kelamin` enum('L','P') DEFAULT NULL,
  `tanggal_masuk` date DEFAULT NULL,
  PRIMARY KEY (`no_pegawai`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_pegawai`
--

LOCK TABLES `tbl_pegawai` WRITE;
/*!40000 ALTER TABLE `tbl_pegawai` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_pegawai` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-14 13:09:04
