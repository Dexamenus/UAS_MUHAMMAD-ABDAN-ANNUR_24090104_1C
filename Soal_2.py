import pandas as p
data = p.DataFrame([
    [90,80],
    [50,60],
    [65,70]
],
index=['Mahasiswa 1', 'Mahasiswa 2','Mahasiswa 3'],
columns=['Algoritma dan Struktur Data 2','Matematika Numerik'])

mean = data.mean(axis=0)
rata = data.mean(axis=1)

print (data)
print(mean)
print(rata)