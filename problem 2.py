from datetime import datetime as dtm
saat_ini = dtm.now() # tgl dan jam saat ini
masuk_str1 = dtm.strftime(saat_ini,'%d-%b-%Y %H:%M:%S')

print(masuk_str1,type(masuk_str1))

tgl_text = (masuk_str1)
tgl_date = dtm.strptime(tgl_text,'%d-%b-%Y %H:%M:%S') # konversi string ke date dengan format tertentu
print(tgl_date, type(tgl_date)) # tipe data datetime.datetime

print(tgl_date.day)
