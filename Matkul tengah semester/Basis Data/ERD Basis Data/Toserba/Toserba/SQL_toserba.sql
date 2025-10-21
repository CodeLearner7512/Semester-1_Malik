-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema toserba
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema toserba
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `toserba` DEFAULT CHARACTER SET utf8mb4 ;
USE `toserba` ;

-- -----------------------------------------------------
-- Table `toserba`.`supplier`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `toserba`.`supplier` (
  `id_supplier` INT(11) NOT NULL,
  `nama_perusahaan` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id_supplier`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `toserba`.`produk`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `toserba`.`produk` (
  `id_produk` INT(11) NOT NULL,
  `nama_produk` VARCHAR(45) NULL DEFAULT NULL,
  `harga` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id_produk`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `toserba`.`pemilik_usaha`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `toserba`.`pemilik_usaha` (
  `id_pemilik` INT(11) NOT NULL,
  `nama` VARCHAR(45) NULL DEFAULT NULL,
  `jabatan` VARCHAR(45) NULL DEFAULT NULL,
  `id_supplier` INT(11) NOT NULL,
  PRIMARY KEY (`id_pemilik`),
  CONSTRAINT `fk_pemilik_usaha_supplier`
    FOREIGN KEY (`id_supplier`)
    REFERENCES `toserba`.`supplier` (`id_supplier`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE INDEX `fk_pemilik_usaha_supplier_idx` ON `toserba`.`pemilik_usaha` (`id_supplier` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `toserba`.`detail_transaksi`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `toserba`.`detail_transaksi` (
  `jumlah` INT(11) NULL DEFAULT NULL,
  `tanggal&waktu` VARCHAR(45) NULL DEFAULT NULL,
  `no_antrian` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`no_antrian`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `toserba`.`mengambil`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `toserba`.`mengambil` (
  `no_antrian` INT(11) NOT NULL,
  `jumlah` VARCHAR(45) NULL DEFAULT NULL,
  `tanggal&waktu` VARCHAR(45) NULL DEFAULT NULL,
  `pemilik_usaha_id_pemilik` INT(11) NOT NULL,
  `produk_id_produk` INT(11) NOT NULL,
  `detail_transaksi_no_antrian` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`no_antrian`, `detail_transaksi_no_antrian`),
  CONSTRAINT `fk_mengambil_pemilik_usaha1`
    FOREIGN KEY (`pemilik_usaha_id_pemilik`)
    REFERENCES `toserba`.`pemilik_usaha` (`id_pemilik`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mengambil_produk1`
    FOREIGN KEY (`produk_id_produk`)
    REFERENCES `toserba`.`produk` (`id_produk`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mengambil_detail_transaksi1`
    FOREIGN KEY (`detail_transaksi_no_antrian`)
    REFERENCES `toserba`.`detail_transaksi` (`no_antrian`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE INDEX `fk_mengambil_pemilik_usaha1_idx` ON `toserba`.`mengambil` (`pemilik_usaha_id_pemilik` ASC) VISIBLE;

CREATE INDEX `fk_mengambil_produk1_idx` ON `toserba`.`mengambil` (`produk_id_produk` ASC) VISIBLE;

CREATE INDEX `fk_mengambil_detail_transaksi1_idx` ON `toserba`.`mengambil` (`detail_transaksi_no_antrian` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `toserba`.`invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `toserba`.`invoice` (
  `nominal` INT(11) NOT NULL,
  `no_antrian` VARCHAR(3) NOT NULL,
  `mengambil_no_antrian` INT(11) NOT NULL,
  `mengambil_detail_transaksi_no_antrian` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`no_antrian`, `mengambil_no_antrian`, `mengambil_detail_transaksi_no_antrian`),
  CONSTRAINT `fk_invoice_mengambil1`
    FOREIGN KEY (`mengambil_no_antrian` , `mengambil_detail_transaksi_no_antrian`)
    REFERENCES `toserba`.`mengambil` (`no_antrian` , `detail_transaksi_no_antrian`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE INDEX `fk_invoice_mengambil1_idx` ON `toserba`.`invoice` (`mengambil_no_antrian` ASC, `mengambil_detail_transaksi_no_antrian` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `toserba`.`detail_pembayaran`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `toserba`.`detail_pembayaran` (
  `tanggal&waktu` DATETIME NOT NULL,
  `no_antrian` INT(11) NOT NULL,
  `invoice_no_antrian` VARCHAR(3) NOT NULL,
  `invoice_mengambil_no_antrian` INT(11) NOT NULL,
  `invoice_mengambil_detail_transaksi_no_antrian` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`no_antrian`, `invoice_no_antrian`, `invoice_mengambil_no_antrian`, `invoice_mengambil_detail_transaksi_no_antrian`),
  CONSTRAINT `fk_detail_pembayaran_invoice1`
    FOREIGN KEY (`invoice_no_antrian` , `invoice_mengambil_no_antrian` , `invoice_mengambil_detail_transaksi_no_antrian`)
    REFERENCES `toserba`.`invoice` (`no_antrian` , `mengambil_no_antrian` , `mengambil_detail_transaksi_no_antrian`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE INDEX `fk_detail_pembayaran_invoice1_idx` ON `toserba`.`detail_pembayaran` (`invoice_no_antrian` ASC, `invoice_mengambil_no_antrian` ASC, `invoice_mengambil_detail_transaksi_no_antrian` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
