"""TIPE DATA DICTIONARY SEKEDAR MENGHUBUNGKAN KEY DAN VALUE KEY
KVP= KEY VALUE PAIR
Dictionary=KAMUS"""

kamus_ind_in_eng = {}
kamus_ind_in_eng['ayah']='father'
kamus_ind_in_eng['ibu']='mother'
kamus_ind_in_eng['istri']='wive'
kamus_ind_in_eng['anak']='son'

print(kamus_ind_in_eng)
print(kamus_ind_in_eng['ayah'])
print(kamus_ind_in_eng['ibu'])
print(kamus_ind_in_eng['istri'])


print('\nDATA INI DIKIRIMKAN OLEH SERVER GOJEK, UNTUK MENGINFOKAN DRIVER DISEKITAR PEMAKAI APLIKASI')

server_gojek={
    'tanggal':'09-08-2021',
    'driver':[{'nama':'eko','jarak':'10'},{'nama':'dwi','jarak':'20'},{'nama':'tri','jarak':'30'},{'nama':'catur','jarak':'100'}]

}
print(f"data driver disekitar: {server_gojek['driver']}")

print(f"data driver disekitar terdekat: {server_gojek['driver'][0]}")
print(f"data driver disekitar no#3: {server_gojek['driver'][2]}")
print(f"data driver disekitar no#4: {server_gojek['driver'][3]}")
print(f"data jarak terdekat: {server_gojek['driver'][0]['jarak']} meter")

