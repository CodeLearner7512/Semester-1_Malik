create table tr_penjualan (
	tgl_transaksi datetime not null,
	kode_cabang varchar(10) not null,
	kode_kasir varchar(10) not null,
	kode_item varchar(7),
	kode_produk varchar(12) not null,
	jumlah_pembelian int(11));


create table ms_karyawan(
	kode_cabang varchar(10),
	kode_karyawan varchar(10) primary key not null,
	nama_depan varchar(8),
	nama_belakang varchar(9),
	jenis_kelamin varchar(1) check (jenis_kelamin in ('L','P')));
	
create table ms_produk (
	kode_item varchar(7),
	kode_produk varchar(12) primary key not null,
	kode_kategori varchar(7),
	nama_produk varchar(100),
	unit int(11),
	kode_satuan varchar(4));
	
create table ms_harga_harian (
	kode_produk varchar(12) not null,
	tgl_berlaku datetime not null,
	kode_cabang varchar(10) not null,
	harga_berlaku_cabang int(11),
	modal_cabang int(11),
	biaya_cabang int(11),
	primary key (kode_produk,tgl_berlaku,kode_cabang)
	);
	
create table ms_cabang (
	kode_cabang varchar(10) primary key not null,
	nama_cabang varchar(100),
	kode_kota varchar(8)
	);
	
create table ms_kota (
	kode_kota varchar(8) primary key not null,
	nama_kota varchar(16),
	kode_provinsi varchar(3)
	);
	
create table ms_propinsi (
	kode_provinsi varchar(3) primary key not null,
	nama_provinsi varchar(25)
	);
	
create table ms_kategori (
	kode_kategori varchar(7) primary key not null,
	nama_kategori varchar(17)
	);
	

--ALTER

alter table tr_penjualan 
add CONSTRAINT fk_penjualan_cabang FOREIGN key (kode_cabang) REFERENCES ms_cabang(kode_cabang),
add CONSTRAINT fk_penjualan_karyawan FOREIGN key (kode_kasir) REFERENCES ms_karyawan(kode_karyawan),
add CONSTRAINT fk_penjualan_produk FOREIGN key (kode_produk) REFERENCES ms_produk(kode_produk)
;

alter table ms_kota
add CONSTRAINT fk_kota_propinsi FOREIGN key (kode_provinsi) REFERENCES ms_propinsi(kode_provinsi);

alter table ms_cabang
add CONSTRAINT fk_cabang_kota FOREIGN key (kode_kota) REFERENCES ms_kota(kode_kota);

alter table ms_produk
add CONSTRAINT fk_produk_kategori FOREIGN key (kode_kategori) REFERENCES ms_kategori(kode_kategori);


--tbl penjualan-harga_harian
alter table tr_penjualan
add CONSTRAINT UQ_tgl_transaksi UNIQUE (tgl_transaksi);

alter table ms_harga_harian
add CONSTRAINT fk_harga_harian_penjualan FOREIGN key (tgl_berlaku) REFERENCES tr_penjualan(tgl_transaksi);

--desc all table
desc tr_penjualan;
desc ms_karyawan;
desc ms_produk;
desc ms_harga_harian;
desc ms_cabang;
desc ms_kota;
desc ms_propinsi;
desc ms_kategori;



--PROCEDURE

DELIMITER $$
CREATE PROCEDURE insert_propinsi (
    IN p_kode_provinsi VARCHAR(3),
    IN p_nama_provinsi VARCHAR(25)
)
BEGIN
    INSERT INTO ms_propinsi (kode_provinsi, nama_provinsi)
    VALUES (p_kode_provinsi, p_nama_provinsi);
END$$
DELIMITER ;



DELIMITER $$
CREATE PROCEDURE insert_kota (
    IN p_kode_kota VARCHAR(8),
    IN p_nama_kota VARCHAR(16),
    IN p_kode_provinsi VARCHAR(3)
)
BEGIN
    INSERT INTO ms_kota (kode_kota, nama_kota, kode_provinsi)
    VALUES (p_kode_kota, p_nama_kota, p_kode_provinsi);
END$$
DELIMITER ;



DELIMITER $$
CREATE PROCEDURE insert_cabang (
    IN p_kode_cabang VARCHAR(10),
    IN p_nama_cabang VARCHAR(100),
    IN p_kode_kota VARCHAR(8)
)
BEGIN
    INSERT INTO ms_cabang (kode_cabang, nama_cabang, kode_kota)
    VALUES (p_kode_cabang, p_nama_cabang, p_kode_kota);
END$$
DELIMITER ;



DELIMITER $$
CREATE PROCEDURE insert_karyawan (
    IN p_kode_karyawan VARCHAR(10),
    IN p_nama_depan VARCHAR(8),
    IN p_nama_belakang VARCHAR(9),
    IN p_jenis_kelamin VARCHAR(1),
    IN p_kode_cabang VARCHAR(10)
)
BEGIN
    INSERT INTO ms_karyawan (kode_karyawan, nama_depan, nama_belakang, jenis_kelamin, kode_cabang)
    VALUES (p_kode_karyawan, p_nama_depan, p_nama_belakang, p_jenis_kelamin, p_kode_cabang);
END$$
DELIMITER ;



DELIMITER $$
CREATE PROCEDURE insert_kategori (
    IN p_kode_kategori VARCHAR(7),
    IN p_nama_kategori VARCHAR(17)
)
BEGIN
    INSERT INTO ms_kategori (kode_kategori, nama_kategori)
    VALUES (p_kode_kategori, p_nama_kategori);
END$$
DELIMITER ;



DELIMITER $$
CREATE PROCEDURE insert_produk (
    IN p_kode_produk VARCHAR(12),
    IN p_nama_produk VARCHAR(100),
    IN p_kode_kategori VARCHAR(7),
    IN p_kode_item VARCHAR(7),
    IN p_unit INT,
    IN p_kode_satuan VARCHAR(4)
)
BEGIN
    INSERT INTO ms_produk (kode_produk, nama_produk, kode_kategori, kode_item, unit, kode_satuan)
    VALUES (p_kode_produk, p_nama_produk, p_kode_kategori, p_kode_item, p_unit, p_kode_satuan);
END$$
DELIMITER ;



DELIMITER $$
CREATE PROCEDURE insert_penjualan (
    IN p_kode_cabang VARCHAR(10),
    IN p_kode_kasir VARCHAR(10),
    IN p_kode_produk VARCHAR(12),
    IN p_jumlah_pembelian INT
)
BEGIN
    DECLARE v_now DATETIME;
    SET v_now = NOW();

    INSERT INTO tr_penjualan (tgl_transaksi, kode_cabang, kode_kasir, kode_produk, jumlah_pembelian)
    VALUES (v_now, p_kode_cabang, p_kode_kasir, p_kode_produk, p_jumlah_pembelian);

    -- auto insert harga harian
    INSERT INTO ms_harga_harian (kode_produk, tgl_berlaku, kode_cabang)
    VALUES (p_kode_produk, DATE_ADD(v_now, INTERVAL 7 DAY), p_kode_cabang);
END$$
DELIMITER ;


--show procedure
select routine_name 
from information_schema.routines 
where routine_type = 'PROCEDURE' 
and routine_schema = 'a11_dbminimarket';




-- Transaction with PROCEDURE
START TRANSACTION;

CALL insert_propinsi('001', 'Jawa Timur');
CALL insert_kota('00000001', 'Madiun', '001');
CALL insert_cabang('1234567891', 'Cabang Madiun', '00000001');
CALL insert_karyawan('00000010', 'Andi', 'Saputra', 'L', '1234567891');
CALL insert_kategori('0000001', 'Alat');
CALL insert_produk('000000000001', 'Thinkpad', '0000001', '0000001', 5, 'PCS');
CALL insert_penjualan('1234567891', '00000010', '000000000001', 2);

COMMIT;



 

--View semua data

CREATE OR REPLACE VIEW v_semua_data AS
SELECT
    prp.kode_provinsi,
    prp.nama_provinsi,

    kt.kode_kota,
    kt.nama_kota,

    cb.kode_cabang,
    cb.nama_cabang,

    kr.kode_karyawan,
    kr.nama_depan,
    kr.nama_belakang,
    kr.jenis_kelamin,

    kat.kode_kategori,
    kat.nama_kategori,

    pd.kode_produk,
    pd.nama_produk,
    pd.unit,
    pd.kode_satuan,

    pj.tgl_transaksi,
    pj.jumlah_pembelian,

    hh.tgl_berlaku,
    hh.harga_berlaku_cabang,
    hh.modal_cabang,
    hh.biaya_cabang

FROM ms_propinsi prp
LEFT JOIN ms_kota kt       ON prp.kode_provinsi = kt.kode_provinsi
LEFT JOIN ms_cabang cb     ON kt.kode_kota = cb.kode_kota
LEFT JOIN ms_karyawan kr   ON cb.kode_cabang = kr.kode_cabang
LEFT JOIN tr_penjualan pj  ON cb.kode_cabang = pj.kode_cabang
LEFT JOIN ms_produk pd     ON pj.kode_produk = pd.kode_produk
LEFT JOIN ms_kategori kat  ON pd.kode_kategori = kat.kode_kategori
LEFT JOIN ms_harga_harian hh
       ON pj.kode_produk = hh.kode_produk
      AND pj.kode_cabang = hh.kode_cabang
      AND hh.tgl_berlaku = DATE_ADD(pj.tgl_transaksi, INTERVAL 7 DAY);




--clear all data
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE ms_harga_harian;
TRUNCATE TABLE tr_penjualan;
TRUNCATE TABLE ms_produk;
TRUNCATE TABLE ms_kategori;
TRUNCATE TABLE ms_karyawan;
TRUNCATE TABLE ms_cabang;
TRUNCATE TABLE ms_kota;
TRUNCATE TABLE ms_propinsi;

SET FOREIGN_KEY_CHECKS = 1;
