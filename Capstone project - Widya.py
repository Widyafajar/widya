
#Input data nilai siswa
#NIS adalah Nomor Induk Siswa
#uts adalah nilai Ujian tengah semester
#uas adalah nilai Ujian akhir semester

nis = []
nama = []
kelas = []
uts = []
uas = []



pilihan = 1
while pilihan !=0:
    print('1.Masukkan data Anda')
    print('2.Tampilkan data Anda')
    print('3.Hapus data yang muncul')
    print('0.Selesai')
    
    pilihan = int(input('Masukkan pilihan Anda :'))
    print('')
    if pilihan == 1:
        ulang=3
        for i in range(ulang):
            print('Data siswa ke -' + str(i+1))
            inputnis = input('Masukkan NIS Anda : ')
            nis.append({'NIS':inputnis})
            inputnama = input('Masukkan Nama Anda : ')
            nama.append({'Nama':inputnama})
            inputkelas = input('Masukkan kelas Anda :')
            kelas.append({'Kelas':inputkelas})
            inpututs = int(input('Masukkan Nilai UTS Anda : '))
            uts.append({'UTS':inpututs})
            inputuas = int(input('Masukkan Nilai UAS Anda : '))
            uas.append({'UAS':inputuas})
            
    elif pilihan == 2:
        print('===================================================')
        print('NIS     Nama   Kelas UTS    UAS')
        print('===================================================')
        for i in range(ulang):
            print(nis[i]['NIS'], '\t',nama[i]['Nama'],   '\t', kelas[i]['Kelas'], '\t', uts[i]['UTS'], '\t', uas[i]['UAS'])

    elif pilihan == 3:
         for i in range (len(nis)):
             print('')
             del nis[i]
             del nama[i]
             del kelas[i]
             del uts[i]
             del uas[i]
             break
print('')
        