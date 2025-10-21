-- 1. Create database
CREATE DATABASE a11_perpustakaan;
\c a11_perpustakaan;

-- 2. Create tables and relationships

-- ENUMs must be defined first in PostgreSQL
CREATE TYPE status_anggota_enum AS ENUM ('Mahasiswa', 'Pelajar', 'Masyarakat');
CREATE TYPE keadaan_buku_enum AS ENUM ('Baik', 'Rusak', 'Cacat', 'Hilang');

CREATE TABLE anggota (
    id_anggota VARCHAR(8) PRIMARY KEY,
    nama_anggota VARCHAR(30),
    alamat_anggota TEXT,
    ttl_anggota DATE,
    status_anggota status_anggota_enum
);

CREATE TABLE formulir (
    no_formulir VARCHAR(10) PRIMARY KEY,
    kode_anggota VARCHAR(8),
    no_ktp VARCHAR(9),
    status_anggota status_anggota_enum,
    biaya_formulir INT
);

CREATE TABLE buku (
    kode_buku VARCHAR(9) PRIMARY KEY,
    judul_buku TEXT,
    pengarang_buku VARCHAR(30),
    jumlah_buku INT,
    penerbit_buku VARCHAR(20)
);

CREATE TABLE peminjaman (
    id_anggota VARCHAR(8),
    kd_buku VARCHAR(9),
    tgl_pinjam DATE,
    tgl_kembali DATE,
    lm_pinjam INT,
    keadaan_buku keadaan_buku_enum
);

-- Add foreign key constraints
ALTER TABLE formulir
ADD CONSTRAINT fk_formulir_anggota
FOREIGN KEY (kode_anggota) REFERENCES anggota(id_anggota);

ALTER TABLE peminjaman
ADD CONSTRAINT fk_peminjaman_anggota
FOREIGN KEY (id_anggota) REFERENCES anggota(id_anggota);

ALTER TABLE peminjaman
ADD CONSTRAINT fk_peminjaman_buku
FOREIGN KEY (kd_buku) REFERENCES buku(kode_buku);


-- 3. Insert values

INSERT INTO anggota VALUES
('20100201','Triana selviana','Tanjung priuk','1989-05-13','Mahasiswa'),
('20100202','Ikhwan aris','Kampung banda','1989-03-02','Mahasiswa'),
('20100203','May silvana','Salemba','1995-05-23','Pelajar'),
('20100204','Dinda aprilia','Matraman','1994-07-15','Pelajar'),
('20100205','Muhammad hasan','Pulo gadung','1970-07-06','Masyarakat');

INSERT INTO formulir VALUES
('2009120001','20100201','503020406','Mahasiswa',10000),
('2009120002','20100202','513698752','Mahasiswa',10000),
('2009120003','20100203','523698423','Pelajar',10000),
('2009120004','20100204','503689741','Pelajar',10000),
('2009120005','20100205','365412892','Masyarakat',10000);

INSERT INTO buku VALUES
('101140298','Intermediate akutansi','Zaki Baridwan',150,'Pustaka jaya'),
('112120509','PHP dan MYSQL','Bunafit nugroho',75,'Erlangga'),
('122060590','Detektive Conan','Sakura motto',100,'Pustaka jaya'),
('131080401','Aqidah akhlaq fiqih islam','Ust. Jefry',70,'Pustaka jaya'),
('111250909','Membuat aplikasi akutansi dengan excel 2007','Moh.Taufiq.S.E',150,'Erlangga'),
('113010807','Menjadi dokter virus komputer','Rahnat putra',90,'Pustaka jaya');

INSERT INTO peminjaman VALUES
('20100204','122060590','2010-02-02','2010-02-16',2,'Rusak'),
('20100202','113010807','2010-02-27','2010-03-03',1,'Hilang'),
('20100201','112120509','2010-03-05','2010-03-12',1,'Cacat'),
('20100205','131080401','2010-03-20','2010-04-05',2,'Rusak');


-- 4. Delete last peminjaman (similar to MySQL LIMIT with ctid trick)
DELETE FROM peminjaman
WHERE ctid IN (
  SELECT ctid FROM peminjaman ORDER BY id_anggota DESC LIMIT 1
);


-- 5. Create Views

-- Date formatting in PostgreSQL uses TO_CHAR
CREATE VIEW v_anggota AS
SELECT
  id_anggota,
  nama_anggota,
  alamat_anggota,
  TO_CHAR(ttl_anggota, 'DD Month YYYY') AS ttl_anggota,
  status_anggota
FROM anggota;

CREATE VIEW v_formulir AS
SELECT
  no_formulir,
  kode_anggota,
  no_ktp,
  status_anggota,
  'Rp ' || TO_CHAR(biaya_formulir, 'FM999,999,999') AS biaya_formulir
FROM formulir;

CREATE VIEW v_buku AS
SELECT
  kode_buku,
  judul_buku,
  pengarang_buku,
  jumlah_buku::TEXT || ' buku' AS jumlah_buku,
  penerbit_buku
FROM buku;

CREATE VIEW v_peminjaman AS
SELECT
  id_anggota,
  kd_buku,
  TO_CHAR(tgl_pinjam, 'DD/MM/YYYY') AS tgl_pinjam,
  TO_CHAR(tgl_kembali, 'DD/MM/YYYY') AS tgl_kembali,
  lm_pinjam::TEXT || ' Minggu' AS lm_pinjam,
  keadaan_buku
FROM peminjaman;


-- 6. Show views
SELECT * FROM v_anggota;
SELECT * FROM v_formulir;
SELECT * FROM v_buku;
SELECT * FROM v_peminjaman;
