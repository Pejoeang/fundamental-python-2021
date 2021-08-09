print('TIPE DATA SKALAR > TIPE DATA SEDERHANA')
anak1= 'EKO'
anak2= 'DWI'
anak3= 'TRI'
anak4= 'CATUR'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\nMENAMBAHKAN DATA ANAK PANCA' )
anak=['EKO','DWI','TRI','CATUR']
print(anak)
anak.append('PANCA')
print(anak)

print('\nSAPA ANAK KE DUA')
print(f"Hai Aanak ke #2 ={anak[1]}")

print('\nSAPA ANAK CARA RUMIT')
for a in range(0,len(anak)):
    print(f"{a+1}. Hai {anak[a]}")