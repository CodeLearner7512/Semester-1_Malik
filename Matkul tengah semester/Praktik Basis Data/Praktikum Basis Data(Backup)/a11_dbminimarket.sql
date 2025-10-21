-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: 10.252.0.151    Database: a11_dbminimarket
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
-- Table structure for table `ms_cabang`
--

DROP TABLE IF EXISTS `ms_cabang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ms_cabang` (
  `kode_cabang` varchar(10) NOT NULL,
  `nama_cabang` varchar(100) DEFAULT NULL,
  `kode_kota` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`kode_cabang`),
  KEY `fk_cabang_kota` (`kode_kota`),
  CONSTRAINT `fk_cabang_kota` FOREIGN KEY (`kode_kota`) REFERENCES `ms_kota` (`kode_kota`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ms_cabang`
--

LOCK TABLES `ms_cabang` WRITE;
/*!40000 ALTER TABLE `ms_cabang` DISABLE KEYS */;
INSERT INTO `ms_cabang` VALUES ('1234567891','Cabang Madiun','00000001');
/*!40000 ALTER TABLE `ms_cabang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ms_harga_harian`
--

DROP TABLE IF EXISTS `ms_harga_harian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ms_harga_harian` (
  `kode_produk` varchar(12) NOT NULL,
  `tgl_berlaku` datetime NOT NULL,
  `kode_cabang` varchar(10) NOT NULL,
  `harga_berlaku_cabang` int DEFAULT NULL,
  `modal_cabang` int DEFAULT NULL,
  `biaya_cabang` int DEFAULT NULL,
  PRIMARY KEY (`kode_produk`,`tgl_berlaku`,`kode_cabang`),
  KEY `fk_harga_harian_penjualan` (`tgl_berlaku`),
  CONSTRAINT `fk_harga_harian_penjualan` FOREIGN KEY (`tgl_berlaku`) REFERENCES `tr_penjualan` (`tgl_transaksi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ms_harga_harian`
--

LOCK TABLES `ms_harga_harian` WRITE;
/*!40000 ALTER TABLE `ms_harga_harian` DISABLE KEYS */;
/*!40000 ALTER TABLE `ms_harga_harian` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ms_karyawan`
--

DROP TABLE IF EXISTS `ms_karyawan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ms_karyawan` (
  `kode_cabang` varchar(10) DEFAULT NULL,
  `kode_karyawan` varchar(10) NOT NULL,
  `nama_depan` varchar(8) DEFAULT NULL,
  `nama_belakang` varchar(9) DEFAULT NULL,
  `jenis_kelamin` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`kode_karyawan`),
  CONSTRAINT `ms_karyawan_chk_1` CHECK ((`jenis_kelamin` in (_cp850'L',_cp850'P')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ms_karyawan`
--

LOCK TABLES `ms_karyawan` WRITE;
/*!40000 ALTER TABLE `ms_karyawan` DISABLE KEYS */;
INSERT INTO `ms_karyawan` VALUES ('1234567891','00000010','Andi','Saputra','L');
/*!40000 ALTER TABLE `ms_karyawan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ms_kategori`
--

DROP TABLE IF EXISTS `ms_kategori`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ms_kategori` (
  `kode_kategori` varchar(7) NOT NULL,
  `nama_kategori` varchar(17) DEFAULT NULL,
  PRIMARY KEY (`kode_kategori`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ms_kategori`
--

LOCK TABLES `ms_kategori` WRITE;
/*!40000 ALTER TABLE `ms_kategori` DISABLE KEYS */;
INSERT INTO `ms_kategori` VALUES ('0000001','Alat');
/*!40000 ALTER TABLE `ms_kategori` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ms_kota`
--

DROP TABLE IF EXISTS `ms_kota`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ms_kota` (
  `kode_kota` varchar(8) NOT NULL,
  `nama_kota` varchar(16) DEFAULT NULL,
  `kode_provinsi` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`kode_kota`),
  KEY `fk_kota_propinsi` (`kode_provinsi`),
  CONSTRAINT `fk_kota_propinsi` FOREIGN KEY (`kode_provinsi`) REFERENCES `ms_propinsi` (`kode_provinsi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ms_kota`
--

LOCK TABLES `ms_kota` WRITE;
/*!40000 ALTER TABLE `ms_kota` DISABLE KEYS */;
INSERT INTO `ms_kota` VALUES ('00000001','Madiun','001');
/*!40000 ALTER TABLE `ms_kota` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ms_produk`
--

DROP TABLE IF EXISTS `ms_produk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ms_produk` (
  `kode_item` varchar(7) DEFAULT NULL,
  `kode_produk` varchar(12) NOT NULL,
  `kode_kategori` varchar(7) DEFAULT NULL,
  `nama_produk` varchar(100) DEFAULT NULL,
  `unit` int DEFAULT NULL,
  `kode_satuan` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`kode_produk`),
  KEY `fk_produk_kategori` (`kode_kategori`),
  CONSTRAINT `fk_produk_kategori` FOREIGN KEY (`kode_kategori`) REFERENCES `ms_kategori` (`kode_kategori`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ms_produk`
--

LOCK TABLES `ms_produk` WRITE;
/*!40000 ALTER TABLE `ms_produk` DISABLE KEYS */;
INSERT INTO `ms_produk` VALUES ('0000001','000000000001','0000001','Thinkpad',5,'PCS');
/*!40000 ALTER TABLE `ms_produk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ms_propinsi`
--

DROP TABLE IF EXISTS `ms_propinsi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ms_propinsi` (
  `kode_provinsi` varchar(3) NOT NULL,
  `nama_provinsi` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`kode_provinsi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ms_propinsi`
--

LOCK TABLES `ms_propinsi` WRITE;
/*!40000 ALTER TABLE `ms_propinsi` DISABLE KEYS */;
INSERT INTO `ms_propinsi` VALUES ('001','Jawa Timur');
/*!40000 ALTER TABLE `ms_propinsi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tr_penjualan`
--

DROP TABLE IF EXISTS `tr_penjualan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tr_penjualan` (
  `tgl_transaksi` datetime NOT NULL,
  `kode_cabang` varchar(10) NOT NULL,
  `kode_kasir` varchar(10) NOT NULL,
  `kode_item` varchar(7) DEFAULT NULL,
  `kode_produk` varchar(12) NOT NULL,
  `jumlah_pembelian` int DEFAULT NULL,
  UNIQUE KEY `UQ_tgl_transaksi` (`tgl_transaksi`),
  KEY `fk_penjualan_cabang` (`kode_cabang`),
  KEY `fk_penjualan_karyawan` (`kode_kasir`),
  KEY `fk_penjualan_produk` (`kode_produk`),
  CONSTRAINT `fk_penjualan_cabang` FOREIGN KEY (`kode_cabang`) REFERENCES `ms_cabang` (`kode_cabang`),
  CONSTRAINT `fk_penjualan_karyawan` FOREIGN KEY (`kode_kasir`) REFERENCES `ms_karyawan` (`kode_karyawan`),
  CONSTRAINT `fk_penjualan_produk` FOREIGN KEY (`kode_produk`) REFERENCES `ms_produk` (`kode_produk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tr_penjualan`
--

LOCK TABLES `tr_penjualan` WRITE;
/*!40000 ALTER TABLE `tr_penjualan` DISABLE KEYS */;
INSERT INTO `tr_penjualan` VALUES ('2025-10-03 10:14:16','1234567891','00000010',NULL,'000000000001',2);
/*!40000 ALTER TABLE `tr_penjualan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `v_semua_data`
--

DROP TABLE IF EXISTS `v_semua_data`;
/*!50001 DROP VIEW IF EXISTS `v_semua_data`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_semua_data` AS SELECT
 1 AS `kode_provinsi`,
  1 AS `nama_provinsi`,
  1 AS `kode_kota`,
  1 AS `nama_kota`,
  1 AS `kode_cabang`,
  1 AS `nama_cabang`,
  1 AS `kode_karyawan`,
  1 AS `nama_depan`,
  1 AS `nama_belakang`,
  1 AS `jenis_kelamin`,
  1 AS `kode_kategori`,
  1 AS `nama_kategori`,
  1 AS `kode_produk`,
  1 AS `nama_produk`,
  1 AS `unit`,
  1 AS `kode_satuan`,
  1 AS `tgl_transaksi`,
  1 AS `jumlah_pembelian`,
  1 AS `tgl_berlaku`,
  1 AS `harga_berlaku_cabang`,
  1 AS `modal_cabang`,
  1 AS `biaya_cabang` */;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_semua_data`
--

/*!50001 DROP VIEW IF EXISTS `v_semua_data`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`254311011`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `v_semua_data` AS select `prp`.`kode_provinsi` AS `kode_provinsi`,`prp`.`nama_provinsi` AS `nama_provinsi`,`kt`.`kode_kota` AS `kode_kota`,`kt`.`nama_kota` AS `nama_kota`,`cb`.`kode_cabang` AS `kode_cabang`,`cb`.`nama_cabang` AS `nama_cabang`,`kr`.`kode_karyawan` AS `kode_karyawan`,`kr`.`nama_depan` AS `nama_depan`,`kr`.`nama_belakang` AS `nama_belakang`,`kr`.`jenis_kelamin` AS `jenis_kelamin`,`kat`.`kode_kategori` AS `kode_kategori`,`kat`.`nama_kategori` AS `nama_kategori`,`pd`.`kode_produk` AS `kode_produk`,`pd`.`nama_produk` AS `nama_produk`,`pd`.`unit` AS `unit`,`pd`.`kode_satuan` AS `kode_satuan`,`pj`.`tgl_transaksi` AS `tgl_transaksi`,`pj`.`jumlah_pembelian` AS `jumlah_pembelian`,`hh`.`tgl_berlaku` AS `tgl_berlaku`,`hh`.`harga_berlaku_cabang` AS `harga_berlaku_cabang`,`hh`.`modal_cabang` AS `modal_cabang`,`hh`.`biaya_cabang` AS `biaya_cabang` from (((((((`ms_propinsi` `prp` left join `ms_kota` `kt` on((`prp`.`kode_provinsi` = `kt`.`kode_provinsi`))) left join `ms_cabang` `cb` on((`kt`.`kode_kota` = `cb`.`kode_kota`))) left join `ms_karyawan` `kr` on((`cb`.`kode_cabang` = `kr`.`kode_cabang`))) left join `tr_penjualan` `pj` on((`cb`.`kode_cabang` = `pj`.`kode_cabang`))) left join `ms_produk` `pd` on((`pj`.`kode_produk` = `pd`.`kode_produk`))) left join `ms_kategori` `kat` on((`pd`.`kode_kategori` = `kat`.`kode_kategori`))) left join `ms_harga_harian` `hh` on(((`pj`.`kode_produk` = `hh`.`kode_produk`) and (`pj`.`kode_cabang` = `hh`.`kode_cabang`) and (`hh`.`tgl_berlaku` = (`pj`.`tgl_transaksi` + interval 7 day))))) */;
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

-- Dump completed on 2025-10-14 13:08:05
