-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema a11_siakad
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema a11_siakad
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `a11_siakad` DEFAULT CHARACTER SET utf8 ;
USE `a11_siakad` ;

-- -----------------------------------------------------
-- Table `a11_siakad`.`mahasiswa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `a11_siakad`.`mahasiswa` (
  `NIM` INT(10) NOT NULL,
  `Nama` VARCHAR(45) NULL,
  `Alamat` TEXT NULL,
  PRIMARY KEY (`NIM`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `a11_siakad`.`log_mahasiswa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `a11_siakad`.`log_mahasiswa` (
  `id_log` INT NOT NULL AUTO_INCREMENT,
  `nim` INT(10) NULL,
  `alamat_baru` TEXT NULL,
  `alamat_lama` TEXT NULL,
  `waktu` DATE NULL,
  PRIMARY KEY (`id_log`))
ENGINE = InnoDB;

USE `a11_siakad` ;

-- -----------------------------------------------------
-- procedure jumlah_mahasiswa
-- -----------------------------------------------------

DELIMITER $$
USE `a11_siakad`$$
CREATE PROCEDURE `jumlah_mahasiswa` (out jumlah int)
BEGIN
select count(NIM) into jumlah from mahasiswa;
END$$

DELIMITER ;
USE `a11_siakad`;

DELIMITER $$
USE `a11_siakad`$$
CREATE DEFINER = CURRENT_USER TRIGGER `a11_siakad`.`mahasiswa_AFTER_INSERT` AFTER INSERT ON `mahasiswa` FOR EACH ROW
BEGIN
insert into log_mahasiswa
set nim= new.nim,
alamat_baru= new.alamat,
waktu=now();
END$$

USE `a11_siakad`$$
CREATE DEFINER = CURRENT_USER TRIGGER `a11_siakad`.`mahasiswa_BEFORE_UPDATE` BEFORE UPDATE ON `mahasiswa` FOR EACH ROW
BEGIN
	insert into log_mahasiswa
	set nim = old.nim,
		alamat_lama= old.alamat,
        alamat_baru= new.alamat,
		waktu = now();
END$$

USE `a11_siakad`$$
CREATE DEFINER = CURRENT_USER TRIGGER `a11_siakad`.`mahasiswa_AFTER_DELETE` AFTER DELETE ON `mahasiswa` FOR EACH ROW
BEGIN
insert into log_mahasiswa
set nim= old.nim,
alamat_lama= old.alamat,
waktu=now();
END$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
