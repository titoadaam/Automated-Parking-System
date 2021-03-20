from datetime import datetime as dtm
tgl1 = dtm(year = 1945, month = 8, day = 17)
tgl2 = dtm.today()
selisih = tgl2 - tgl1
print('Indonesia sudah merdeka selama =', selisih.days, ' hari')

hari1 = waktu_masuk
hari2 = waktu_keluar
total_hari = hari2 - hari1
hari = total_hari.days