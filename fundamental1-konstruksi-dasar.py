#KONSTRUKSI DASAR PYTHON
#SEQUENTIAL: EKSEKUSI BERURUTAN
print("Hello world")
print("by Kiki")
print("tanggal 08/08/2021")
print("="*20)

print("\n")
#PERCABANGAN: EKSEKUSI TERPILIH
ingin_cepat = True
if ingin_cepat:
    print("jalan lurus aja")
else:
    ("jalan memutar")

print("\n")
#PERULANGAN
nama_anak=['Adi','Dian','Edi','Juned']

for panggil_anak in nama_anak:
    print(f"Halo Anak ku # {panggil_anak}")

print("\n")
jumlah_anak=4

for index_anak in range(1,jumlah_anak+1):
    print(f"Hai anak ke# {index_anak}")