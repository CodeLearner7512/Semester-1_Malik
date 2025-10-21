-- 1. Buat database Perpustakaan
create database a11_perpustakaan;
use a11_perpustakaan;

-- 2. Buat tabel dan relasi

create table ANGGOTA (
id_anggota varchar(8) primary key,
Nama_anggota varchar(30),
Alamat_anggota text,
Ttl_anggota date,
Status_anggota enum('Mahasiswa','Pelajar','Masyarakat')
);
create table FORMULIR (
No_formulir varchar(10) primary key,
Nama_anggota varchar(30),
Kode_anggota varchar(8),
No_ktp varchar(9),
Status_anggota enum('Mahasiswa','Pelajar','Masyarakat'),
Biaya_formulir int(10)
);
create table BUKU (
Kode_buku varchar(9) primary key,
Judul_buku text,
Pengarang_buku varchar(30),
Jumlah_buku int,
Penerbit_buku varchar(20)
);
create table PEMINJAMAN (
id_anggota varchar(8),
Nm_anggota varchar(30),
Kd_buku varchar(9),
Tgl_pinjam date,
Tgl_kembali date,
Lm_pinjam int,
Keadaan_buku enum('Baik','Rusak','Cacat','Hilang')
);

alter table FORMULIR
add constraint fk_formulir_anggota foreign key
(Kode_anggota) references ANGGOTA(id_anggota);
alter table PEMINJAMAN
add constraint fk_peminjaman_anggota foreign key
(id_anggota) references ANGGOTA(id_anggota);
alter table PEMINJAMAN
add constraint fk_peminjaman_buku foreign key
(Kd_buku) references BUKU(Kode_buku);


-- Insert Values

Insert into ANGGOTA values
('20100201','Triana selviana','Tanjung priuk','1989-05-13',1),
('20100202','Ikhwan aris','Kampung banda','1989-03-02',1),
('20100203','May silvana','Salemba','1995-05-23',2),
('20100204','Dinda aprilia','Matraman','1994-07-15',2),
('20100205','Muhammad hasan','Pulo gadung','1970-07-06',3);

Insert into FORMULIR values
('2009120001','Triana selviana','20100201','503020406',1,10000),
('2009120002','Ikhwan aris','20100202','513698752',1,10000),
('2009120003','May silvana','20100203','523698423',2,10000),
('2009120004','Dinda aprilia','20100204','503689741',2,10000),
('2009120005','Muhammad hasan','20100205','365412892',3,10000);

insert into BUKU values
('101140298','Intermediate akutansi','Zaki Baridwan',150,'Pustaka jaya'),
('112120509','PHP dan MYSQL','Bunafit nugroho',75,'Erlangga'),
('122060590','Detektive Conan','Sakura motto',100,'Pustaka jaya'),
('131080401','Aqidah akhlaq fiqih islam','Ust. Jefry',70,'Pustaka jaya'),
('111250909','Membuat aplikasi akutansi dengan excel 2007','Moh.Taufiq.S.E',150,'Erlangga'),
('113010807','Menjadi dokter virus komputer','Rahnat putra',90,'Pustaka jaya');

insert into PEMINJAMAN values
('20100204','Dinda aprilia','122060590','2010-02-02','2010-02-16',2,2),
('20100202','Ikhwan aris','113010807','2010-02-27','2010-03-03',1,4),
('20100201','Triana selviana','112120509','2010-03-05','2010-03-12',1,3),
('20100205','Muhammad hasan','131080401','2010-03-20','2010-04-05',2,2);


-- 3. Hapus kolom Nm_anggota pada tabel PEMINJAMAN
alter table PEMINJAMAN
drop column Nm_anggota;


-- 4.Hapus kolom Nama_anggota pada tabel FORMULIR 
alter table FORMULIR
drop column Nama_anggota;


-- 5. Tampilkan isi tabel buku
select * from BUKU;


-- 6. Hapus satu data PEMINJAMAN
delete from PEMINJAMAN order by id_anggota desc limit 1;


-- Bonus : Membuat View sesuai skema tabel

create VIEW v_anggota as
select id_anggota,
Nama_anggota,
Alamat_anggota,date_format(Ttl_anggota,'%d %M %Y') as Ttl_anggota,Status_anggota
from ANGGOTA;

create VIEW v_formulir as
select No_formulir,
Kode_anggota,
No_ktp,Status_anggota,
concat('Rp  ',replace(format(Biaya_formulir, 0), ',', '.')) as Biaya_formulir
from FORMULIR;

create VIEW v_buku as
select Kode_buku,
Judul_buku,
Pengarang_buku,
concat(Jumlah_buku, ' buku') as Jumlah_buku,
Penerbit_buku
from BUKU;

create VIEW v_peminjaman as
select id_anggota,
Kd_buku,
date_format(Tgl_pinjam,'%d/%m/%Y') as Tgl_pinjam,
date_format(Tgl_kembali,'%d/%m/%Y') as Tgl_kembali,
concat(Lm_pinjam, ' Minggu') as Lm_pinjam,Keadaan_buku
from PEMINJAMAN;


-- Bonus : Tampilkan View
select * from v_anggota;
select * from v_formulir;
select * from v_buku;
select * from v_peminjaman;
