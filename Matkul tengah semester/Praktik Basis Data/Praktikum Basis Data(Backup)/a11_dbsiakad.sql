-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: 10.252.0.151    Database: a11_dbsiakad
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
-- Table structure for table `Buku`
--

DROP TABLE IF EXISTS `Buku`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Buku` (
  `ID` int NOT NULL,
  `Judul` varchar(100) NOT NULL,
  `Pengarang` varchar(50) DEFAULT NULL,
  `Tahun_Terbit` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Buku`
--

LOCK TABLES `Buku` WRITE;
/*!40000 ALTER TABLE `Buku` DISABLE KEYS */;
/*!40000 ALTER TABLE `Buku` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dosen`
--

DROP TABLE IF EXISTS `Dosen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Dosen` (
  `NID` int NOT NULL,
  `NamaDosen` varchar(100) NOT NULL,
  `Jabatan` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`NID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dosen`
--

LOCK TABLES `Dosen` WRITE;
/*!40000 ALTER TABLE `Dosen` DISABLE KEYS */;
/*!40000 ALTER TABLE `Dosen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MataKuliah`
--

DROP TABLE IF EXISTS `MataKuliah`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MataKuliah` (
  `KodeMK` varchar(10) NOT NULL,
  `NamaMK` varchar(100) NOT NULL,
  `SKS` int DEFAULT NULL,
  PRIMARY KEY (`KodeMK`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MataKuliah`
--

LOCK TABLES `MataKuliah` WRITE;
/*!40000 ALTER TABLE `MataKuliah` DISABLE KEYS */;
/*!40000 ALTER TABLE `MataKuliah` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Nilai`
--

DROP TABLE IF EXISTS `Nilai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Nilai` (
  `ID_Nilai` int NOT NULL,
  `ID_Siswa` int NOT NULL,
  `KodeMK` varchar(10) NOT NULL,
  `Nilai_Akhir` float DEFAULT NULL,
  PRIMARY KEY (`ID_Nilai`),
  UNIQUE KEY `ID_Siswa` (`ID_Siswa`),
  UNIQUE KEY `KodeMK` (`KodeMK`),
  CONSTRAINT `fk_Nilai_MataKuliah` FOREIGN KEY (`KodeMK`) REFERENCES `MataKuliah` (`KodeMK`),
  CONSTRAINT `fk_Nilai_Siswa` FOREIGN KEY (`ID_Siswa`) REFERENCES `Siswa` (`ID`),
  CONSTRAINT `Nilai_ibfk_1` FOREIGN KEY (`KodeMK`) REFERENCES `MataKuliah` (`KodeMK`),
  CONSTRAINT `Nilai_ibfk_2` FOREIGN KEY (`ID_Siswa`) REFERENCES `Buku` (`ID`),
  CONSTRAINT `Nilai_ibfk_3` FOREIGN KEY (`KodeMK`) REFERENCES `MataKuliah` (`KodeMK`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Nilai`
--

LOCK TABLES `Nilai` WRITE;
/*!40000 ALTER TABLE `Nilai` DISABLE KEYS */;
/*!40000 ALTER TABLE `Nilai` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pengajaran`
--

DROP TABLE IF EXISTS `Pengajaran`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Pengajaran` (
  `ID_Pengajaran` int NOT NULL,
  `NID` int NOT NULL,
  `KodeMK` varchar(10) NOT NULL,
  PRIMARY KEY (`ID_Pengajaran`),
  UNIQUE KEY `NID` (`NID`),
  UNIQUE KEY `KodeMK` (`KodeMK`),
  CONSTRAINT `fk_Pengajaran_Dosen` FOREIGN KEY (`NID`) REFERENCES `Dosen` (`NID`),
  CONSTRAINT `fk_Pengajaran_MataKuliah` FOREIGN KEY (`KodeMK`) REFERENCES `MataKuliah` (`KodeMK`),
  CONSTRAINT `Pengajaran_ibfk_1` FOREIGN KEY (`NID`) REFERENCES `Dosen` (`NID`),
  CONSTRAINT `Pengajaran_ibfk_2` FOREIGN KEY (`KodeMK`) REFERENCES `MataKuliah` (`KodeMK`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pengajaran`
--

LOCK TABLES `Pengajaran` WRITE;
/*!40000 ALTER TABLE `Pengajaran` DISABLE KEYS */;
/*!40000 ALTER TABLE `Pengajaran` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Siswa`
--

DROP TABLE IF EXISTS `Siswa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Siswa` (
  `ID` int NOT NULL,
  `Nama_Siswa` varchar(50) DEFAULT NULL,
  `Tanggal_Masuk` date DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Siswa`
--

LOCK TABLES `Siswa` WRITE;
/*!40000 ALTER TABLE `Siswa` DISABLE KEYS */;
/*!40000 ALTER TABLE `Siswa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transaksi`
--

DROP TABLE IF EXISTS `Transaksi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Transaksi` (
  `TransaksiID` int NOT NULL,
  `ID_Siswa` int NOT NULL,
  `ID_BUKU` int NOT NULL,
  `Tanggal_Peminjaman` date DEFAULT NULL,
  PRIMARY KEY (`TransaksiID`),
  KEY `ID_Siswa` (`ID_Siswa`),
  CONSTRAINT `Transaksi_ibfk_1` FOREIGN KEY (`ID_Siswa`) REFERENCES `Buku` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transaksi`
--

LOCK TABLES `Transaksi` WRITE;
/*!40000 ALTER TABLE `Transaksi` DISABLE KEYS */;
/*!40000 ALTER TABLE `Transaksi` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-14 13:09:53
