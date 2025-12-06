delimiter $$
create function func_jumlah_mahasiswa ()
returns int(10)
deterministic
reads sql data
	begin
		declare jumlah int;
		set jumlah=0;
		select count(NIM) into jumlah from mahasiswa;
		return jumlah;
	end$$
delimiter ;
