siswa = []

while True:
    nim = int(input('Masukan NIM: '))
    nama = str(input('Masukan Nama: '))
    templet = {'Nama' : nama, 'NIM' : nim}
    siswa.append(templet)
   


    x = input('Ingin tambah lagi(ya/tidak)? ')

    if x == 'ya':
        continue
    else:
        for i in siswa:
         t = 1
         print(f'{t}. {i['Nama']}: {i['NIM']}')
         t += 1
       
        break

