-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: 10.252.0.151    Database: a11_perpustakaan
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
-- Table structure for table `ANGGOTA`
--

DROP TABLE IF EXISTS `ANGGOTA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ANGGOTA` (
  `id_anggota` varchar(8) NOT NULL,
  `Nama_anggota` varchar(30) DEFAULT NULL,
  `Alamat_anggota` text,
  `Ttl_anggota` date DEFAULT NULL,
  `Status_anggota` enum('Mahasiswa','Pelajar','Masyarakat') DEFAULT NULL,
  PRIMARY KEY (`id_anggota`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ANGGOTA`
--

LOCK TABLES `ANGGOTA` WRITE;
/*!40000 ALTER TABLE `ANGGOTA` DISABLE KEYS */;
INSERT INTO `ANGGOTA` VALUES ('20100201','Triana selviana','Tanjung priuk','1989-05-13','Mahasiswa'),('20100202','Ikhwan aris','Kampung banda','1989-03-02','Mahasiswa'),('20100203','May silvana','Salemba','1995-05-23','Pelajar'),('20100204','Dinda aprilia','Matraman','1994-07-15','Pelajar'),('20100205','Muhammad hasan','Pulo gadung','1970-07-06','Masyarakat');
/*!40000 ALTER TABLE `ANGGOTA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BUKU`
--

DROP TABLE IF EXISTS `BUKU`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BUKU` (
  `Kode_buku` varchar(9) NOT NULL,
  `Judul_buku` text,
  `Pengarang_buku` varchar(30) DEFAULT NULL,
  `Jumlah_buku` int DEFAULT NULL,
  `Penerbit_buku` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Kode_buku`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BUKU`
--

LOCK TABLES `BUKU` WRITE;
/*!40000 ALTER TABLE `BUKU` DISABLE KEYS */;
INSERT INTO `BUKU` VALUES ('101140298','Intermediate akutansi','Zaki Baridwan',150,'Pustaka jaya'),('111250909','Membuat aplikasi akutansi dengan excel 2007','Moh.Taufiq.S.E',150,'Erlangga'),('112120509','PHP dan MYSQL','Bunafit nugroho',75,'Erlangga'),('113010807','Menjadi dokter virus komputer','Rahnat putra',90,'Pustaka jaya'),('122060590','Detektive Conan','Sakura motto',100,'Pustaka jaya'),('131080401','Aqidah akhlaq fiqih islam','Ust. Jefry',70,'Pustaka jaya');
/*!40000 ALTER TABLE `BUKU` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FORMULIR`
--

DROP TABLE IF EXISTS `FORMULIR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FORMULIR` (
  `No_formulir` varchar(10) NOT NULL,
  `Kode_anggota` varchar(8) DEFAULT NULL,
  `No_ktp` varchar(9) DEFAULT NULL,
  `Status_anggota` enum('Mahasiswa','Pelajar','Masyarakat') DEFAULT NULL,
  `Biaya_formulir` int DEFAULT NULL,
  PRIMARY KEY (`No_formulir`),
  KEY `fk_formulir_anggota` (`Kode_anggota`),
  CONSTRAINT `fk_formulir_anggota` FOREIGN KEY (`Kode_anggota`) REFERENCES `ANGGOTA` (`id_anggota`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FORMULIR`
--

LOCK TABLES `FORMULIR` WRITE;
/*!40000 ALTER TABLE `FORMULIR` DISABLE KEYS */;
INSERT INTO `FORMULIR` VALUES ('2009120001','20100201','503020406','Mahasiswa',10000),('2009120002','20100202','513698752','Mahasiswa',10000),('2009120003','20100203','523698423','Pelajar',10000),('2009120004','20100204','503689741','Pelajar',10000),('2009120005','20100205','365412892','Masyarakat',10000);
/*!40000 ALTER TABLE `FORMULIR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PEMINJAMAN`
--

DROP TABLE IF EXISTS `PEMINJAMAN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PEMINJAMAN` (
  `id_anggota` varchar(8) DEFAULT NULL,
  `Kd_buku` varchar(9) DEFAULT NULL,
  `Tgl_pinjam` date DEFAULT NULL,
  `Tgl_kembali` date DEFAULT NULL,
  `Lm_pinjam` int DEFAULT NULL,
  `Keadaan_buku` enum('Baik','Rusak','Cacat','Hilang') DEFAULT NULL,
  KEY `fk_peminjaman_anggota` (`id_anggota`),
  KEY `fk_peminjaman_buku` (`Kd_buku`),
  CONSTRAINT `fk_peminjaman_anggota` FOREIGN KEY (`id_anggota`) REFERENCES `ANGGOTA` (`id_anggota`),
  CONSTRAINT `fk_peminjaman_buku` FOREIGN KEY (`Kd_buku`) REFERENCES `BUKU` (`Kode_buku`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PEMINJAMAN`
--

LOCK TABLES `PEMINJAMAN` WRITE;
/*!40000 ALTER TABLE `PEMINJAMAN` DISABLE KEYS */;
INSERT INTO `PEMINJAMAN` VALUES ('20100204','122060590','2010-02-02','2010-02-16',2,'Rusak'),('20100202','113010807','2010-02-27','2010-03-03',1,'Hilang'),('20100201','112120509','2010-03-05','2010-03-12',1,'Cacat');
/*!40000 ALTER TABLE `PEMINJAMAN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `v_anggota`
--

DROP TABLE IF EXISTS `v_anggota`;
/*!50001 DROP VIEW IF EXISTS `v_anggota`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_anggota` AS SELECT
 1 AS `id_anggota`,
  1 AS `Nama_anggota`,
  1 AS `Alamat_anggota`,
  1 AS `Ttl_anggota`,
  1 AS `Status_anggota` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_buku`
--

DROP TABLE IF EXISTS `v_buku`;
/*!50001 DROP VIEW IF EXISTS `v_buku`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_buku` AS SELECT
 1 AS `Kode_buku`,
  1 AS `Judul_buku`,
  1 AS `Pengarang_buku`,
  1 AS `Jumlah_buku`,
  1 AS `Penerbit_buku` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_formulir`
--

DROP TABLE IF EXISTS `v_formulir`;
/*!50001 DROP VIEW IF EXISTS `v_formulir`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_formulir` AS SELECT
 1 AS `No_formulir`,
  1 AS `Kode_anggota`,
  1 AS `No_ktp`,
  1 AS `Status_anggota`,
  1 AS `Biaya_formulir` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_peminjaman`
--

DROP TABLE IF EXISTS `v_peminjaman`;
/*!50001 DROP VIEW IF EXISTS `v_peminjaman`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_peminjaman` AS SELECT
 1 AS `id_anggota`,
  1 AS `Kd_buku`,
  1 AS `Tgl_pinjam`,
  1 AS `Tgl_kembali`,
  1 AS `Lm_pinjam`,
  1 AS `Keadaan_buku` */;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_anggota`
--

/*!50001 DROP VIEW IF EXISTS `v_anggota`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`254311011`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `v_anggota` AS select `ANGGOTA`.`id_anggota` AS `id_anggota`,`ANGGOTA`.`Nama_anggota` AS `Nama_anggota`,`ANGGOTA`.`Alamat_anggota` AS `Alamat_anggota`,date_format(`ANGGOTA`.`Ttl_anggota`,'%d %M %Y') AS `Ttl_anggota`,`ANGGOTA`.`Status_anggota` AS `Status_anggota` from `ANGGOTA` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_buku`
--

/*!50001 DROP VIEW IF EXISTS `v_buku`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`254311011`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `v_buku` AS select `BUKU`.`Kode_buku` AS `Kode_buku`,`BUKU`.`Judul_buku` AS `Judul_buku`,`BUKU`.`Pengarang_buku` AS `Pengarang_buku`,concat(`BUKU`.`Jumlah_buku`,' buku') AS `Jumlah_buku`,`BUKU`.`Penerbit_buku` AS `Penerbit_buku` from `BUKU` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_formulir`
--

/*!50001 DROP VIEW IF EXISTS `v_formulir`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`254311011`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `v_formulir` AS select `FORMULIR`.`No_formulir` AS `No_formulir`,`FORMULIR`.`Kode_anggota` AS `Kode_anggota`,`FORMULIR`.`No_ktp` AS `No_ktp`,`FORMULIR`.`Status_anggota` AS `Status_anggota`,concat('Rp  ',replace(format(`FORMULIR`.`Biaya_formulir`,0),',','.')) AS `Biaya_formulir` from `FORMULIR` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_peminjaman`
--

/*!50001 DROP VIEW IF EXISTS `v_peminjaman`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`254311011`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `v_peminjaman` AS select `PEMINJAMAN`.`id_anggota` AS `id_anggota`,`PEMINJAMAN`.`Kd_buku` AS `Kd_buku`,date_format(`PEMINJAMAN`.`Tgl_pinjam`,'%d/%m/%Y') AS `Tgl_pinjam`,date_format(`PEMINJAMAN`.`Tgl_kembali`,'%d/%m/%Y') AS `Tgl_kembali`,concat(`PEMINJAMAN`.`Lm_pinjam`,' Minggu') AS `Lm_pinjam`,`PEMINJAMAN`.`Keadaan_buku` AS `Keadaan_buku` from `PEMINJAMAN` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-14 13:10:13
