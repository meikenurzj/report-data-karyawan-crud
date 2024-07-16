#Data Karyawan
DataKaryawan =[
    {
        'NoID':101,
        'Nama': 'Hayya Sekar',
        'TTL' : 'Jakarta, 26 April 1998',
        'Jenis_Kelamin' : 'Perempuan',
        'Divisi' : 'Marketing',
        'Posisi' : 'Staf',
        'Status' : 'PKWT',
    },
    {
        'NoID':102,
        'Nama': 'Muhammad',
        'TTL' : 'Bandung, 01 Juni 1993',
        'Jenis_Kelamin': 'Pria',
        'Divisi' : 'PPIC',
        'Posisi' : 'Staf',
        'Status' : 'PKWT',
    },
    {
        'NoID':103,
        'Nama': 'Jack',
        'TTL' : 'Surabaya, 21 Juni 1989',
        'Jenis_Kelamin' : 'Pria',
        'Divisi' : 'Operasional',
        'Posisi' : 'Manager',
        'Status' : 'Kartap' ,
    },
    {
        'NoID':104,
        'Nama': 'Ammirah',
        'TTL' : 'Semarang, 12 Januari 1996',
        'Jenis_Kelamin': 'Perempuan',
        'Divisi' : 'Data',
        'Posisi' : 'Lead',
        'Status' : 'Kartap',
    }
]

def pembatas():
    print(125*'-')
def pembatas2():
    print(125*'=')

#Read Data
def ReadData():
     while True:
        pembatas2()
        print('Menu Report Data Karyawan'.center(125,"-"))
        pembatas2()
        print('1. Report Data Karyawan')
        print('2. Mencari Data Karyawan')
        print('3. Kembali Ke Menu Awal')
        submenu = int(input('Silahkan Pilih Sub Menu Report Data Karyawan [1-3]: '))
        if submenu == 1:
            if len(DataKaryawan) != 0:
                print(125*'=')
                print('Report Data Karyawan'.center(125,"-"))
                print(125*'=')
                print("No", "NoID".center(8), 'Nama'.center(20), 'TTL'.center(30), 'Jenis Kelamin'.center(25), 'Divisi'.center(10), 'Posisi'.center(10), 'Status'.center(10))
                for i in range (len(DataKaryawan)):
                    print('{:<2} | {:<6}| {:<20} | {:<30} | {:<15}| {:<12} | {:<10} | {:<15}'.format(i+1, DataKaryawan[i]['NoID'], DataKaryawan[i]['Nama'], DataKaryawan[i]['TTL'],DataKaryawan[i]['Jenis_Kelamin'], DataKaryawan[i]['Divisi'], DataKaryawan[i]['Posisi'], DataKaryawan[i]['Status']))
                pembatas2()
            else:
                print('Tidak Ada Data Karyawan Dalam Database'.center(125,"-"))
        elif submenu == 2: 
            if len(DataKaryawan) != 0:
                data = int(input('Masukan Nomor ID Karyawan: '))
                print(f'Data Karyawan Dengan Nomor ID {data}:')
                for i in range (len(DataKaryawan)):
                    if data == DataKaryawan[i]['NoID']:
                        pembatas()
                        print('Data Karyawan Sebagai Berikut: '.center(125, '-'))
                        pembatas()
                        print("No", "NoID".center(8), 'Nama'.center(20), 'TTL'.center(30), 'Jenis Kelamin'.center(25), 'Divisi'.center(10), 'Posisi'.center(10), 'Status'.center(10))
                        print('{:<2} | {:<8}| {:<20} | {:<30} | {:<15}| {:<12} | {:<10} | {:<15}'.format(i+1, DataKaryawan[i]['NoID'], DataKaryawan[i]['Nama'], DataKaryawan[i]['TTL'],DataKaryawan[i]['Jenis_Kelamin'], DataKaryawan[i]['Divisi'], DataKaryawan[i]['Posisi'], DataKaryawan[i]['Status']))
                        pembatas2()
                        break
                else: 
                    pembatas2()
                    print(f'Tidak Ada Data Karyawan Dengan NoID {data} Dalam Database'.center(125, '-'))
                    pembatas2()
            continue
        elif submenu == 3:
             return
        else:
            print("Pilihan yang Anda masukkan salah, silahkan pilih menu yang sesuai [1-3]")


# Create Menu Data
def CreateData():
    while True:
        print('Menu Tambahkan Data Karyawan'.center(120,"-"))
        print('1. Tambahkan Data Karyawan')
        print('2. Kembali Ke Menu Awal')
        tambahdata = int(input('Silahkan Pilih Sub Menu Tambah Data Karyawan [1-2]: '))
        if tambahdata == 1:
            input_nomor = int(input('Masukan Nomor ID Karyawan:'))
            for i in range(len(DataKaryawan)):
                if input_nomor == DataKaryawan[i]['NoID']:
                    print(f'Nomor ID {input_nomor} Sudah Ada Dalam Database'.center(120,'-'))
                    print('Silahkan Masukan Nomor ID Baru'.center(120,'-'))
                    break
                
            else:
                nama_baru = input('Masukan Nama Karyawan: ').capitalize()
                ttl_baru = input('Masukan Tempat Tanggal Lahir Karyawan: ').capitalize()
                gender = input('Masukan Jenis_Kelamin Karyawan: ').capitalize()
                div_baru = input('Masukan Divisi Karyawan: ').capitalize()
                posisi_baru = input('Masukan Posisi Karyawan: ').capitalize()
                status_baru = input('Masukan Status Karyawan: ').capitalize()
                pilihan = input('Apakah Anda Ingin Menambahkan Data Karyawan Tersebut [Y/N]: ').upper()
                if pilihan == 'Y':
                    DataKaryawan.append({
                            'NoID' : int(input_nomor),
                            'Nama' : nama_baru,
                            'TTL' : ttl_baru,
                            'Jenis_Kelamin'  :gender,
                            'Divisi' : div_baru,
                            'Posisi' : posisi_baru,
                            'Status' : status_baru, })
                    pembatas2()
                    print(f'Data Karyawan Baru Sudah Tersimpan Dalam Database'.center(120,'-'))
                elif pilihan == 'N':
                    pembatas2()
                    print(f'Data Karyawan Gagal Tersimpan Dalam Database'.center(120,'-'))
                    pembatas2()
                        
                else:
                    (f'Pilihan Yang Anda Masukan Salah, Silahkan Masukan Pilih Menu Yang Benar [Y/N]: '.center(120,'-'))
                
        elif tambahdata == 2:
             return
        else:
             print(f'Pilihan Yang Anda Masukan Salah, Silahkan Masukan Pilih Menu Yang Benar [1-2]: '.center(120,'-'))

# Update Menu Data
def UpdateData():
    while True:
        pembatas2()
        print('Menu Update Data Karyawan'.center(125,"-"))
        pembatas2()
        print('1. Update Data Karyawan')
        print('2. Kembali Ke Menu Awal')
        update = int(input('Silahkan Pilih Sub Menu Tambah Data Karyawan [1-2]: '))

        if update == 1:
            cari_noid = int(input('Masukan Nomor ID Yang Akan Di Update: '))
            karyawan = False
            for i in range(len(DataKaryawan)):
                if DataKaryawan[i]['NoID'] == cari_noid:
                    karyawan = True
                    print(f'Berikut Adalah Data Karyawan Dengan NoID {cari_noid}'.center(125, '-'))
                    print("No", "NoID".center(8), 'Nama'.center(20), 'TTL'.center(30), 'Jenis Kelamin'.center(25), 'Divisi'.center(10), 'Posisi'.center(10), 'Status'.center(10))
                    print('{:<2} | {:<8}| {:<20} | {:<30} | {:<15}| {:<12} | {:<10} | {:<15}'.format(i+1, DataKaryawan[i]['NoID'], DataKaryawan[i]['Nama'], DataKaryawan[i]['TTL'],DataKaryawan[i]['Jenis_Kelamin'], DataKaryawan[i]['Divisi'], DataKaryawan[i]['Posisi'], DataKaryawan[i]['Status']))
                   
                    nama_baru = input('Masukan Nama Karyawan (atau tekan Enter untuk tidak mengubah): ').capitalize()
                    ttl_baru = input('Masukan Tempat Tanggal Lahir (atau tekan Enter untuk tidak mengubah): ').capitalize()
                    gender_baru = input('Masukan Jenis Kelamin (atau tekan Enter untuk tidak mengubah): ').capitalize()
                    posisi_baru = input('Masukan Posisi Karyawan (atau tekan Enter untuk tidak mengubah): ').capitalize()
                    divisi_baru = input('Masukan Divisi Karyawan (atau tekan Enter untuk tidak mengubah): ').capitalize()
                    status_baru = input('Masukan Status Karyawan(atau tekan Enter untuk tidak mengubah): ').capitalize()

                    pilihan = input('Apakah Data Akan Update Data Karyawan Tersebut [Y/N]:').upper()
                    if pilihan == 'Y':
                        pembatas2()
                        
                        if nama_baru:
                            DataKaryawan[i]['Nama'] = nama_baru
                        if ttl_baru:
                            DataKaryawan[i]['TTL'] = ttl_baru
                        if  gender_baru:
                            DataKaryawan[i]['Jenis_Kelamin'] = gender_baru
                        if divisi_baru:
                            DataKaryawan[i]['Divisi'] = divisi_baru
                        if posisi_baru:
                           DataKaryawan[i]['Posisi'] = posisi_baru
                        if status_baru:
                            DataKaryawan[i]['Status'] = status_baru
                        print('Data Anda Berhasil Terupdate!'.center(125,'-'))
                        pembatas2()

                    elif pilihan == 'N':
                        pembatas2()
                        print('Data Anda Tidak Berhasil Terupdate'.center(125,'-'))
                    else:
                        print(f'Pilihan Yang Anda Masukan Salah, Silahkan Masukan Pilih Menu Yang Benar [Y/N]: '.center(125,'-'))
                    break
            if not karyawan:
                print('Nomor ID Yang Anda Masukan Tidak Ada Dalam Database'.center(125,'-'))

        elif update == 2:
            return
        else:
            print("Pilihan yang Anda masukkan salah, silahkan pilih menu yang sesuai [1-2]".center(125, '-'))

# Delete Menu Data
def DeleteData():
    while True:
        pembatas()
        print('Menu Hapus Data Karyawan'.center(125, "-"))
        pembatas()
        print('1. Hapus Data Karyawan')
        print('2. Kembali Ke Menu Awal')
        hapusdata = int(input('Silahkan Pilih Sub Menu Tambah Data Karyawan [1-2]: '))
        if hapusdata == 1:
            noid = int(input('Masukan Nomor ID Karyawan Yang Akan Di Hapus: '))
            karyawan_ditemukan = False
            for i in range(len(DataKaryawan)):
                if DataKaryawan[i]['NoID'] == noid:
                    pembatas2()
                    print("Data Karyawan Yang Akan Dihapus:".center(125, '-'))
                    print("No", "NoID".center(8), 'Nama'.center(20), 'TTL'.center(30), 'Jenis Kelamin'.center(25), 'Divisi'.center(10), 'Posisi'.center(10), 'Status'.center(10))
                    print('{:<2} | {:<8}| {:<20} | {:<30} | {:<15}| {:<12} | {:<10} | {:<15}'.format(i+1, DataKaryawan[i]['NoID'], DataKaryawan[i]['Nama'], DataKaryawan[i]['TTL'],DataKaryawan[i]['Jenis_Kelamin'], DataKaryawan[i]['Divisi'], DataKaryawan[i]['Posisi'], DataKaryawan[i]['Status']))
                    pilihan = input('Apakah Anda yakin ingin menghapus data karyawan tersebut [Y/N]').strip().upper()
                    if pilihan == 'Y':
                        DataKaryawan.pop(i)
                        pembatas2()
                        print('Data Karyawan Telah Dihapus Dari Database!'.center(125, '='))
                    else:
                        pembatas2()
                        print('Penghapusan Data Karyawan Dibatalkan'.center(125, '-'))
                    karyawan_ditemukan = True
                    break

            if not karyawan_ditemukan:
                pembatas2()
                print('Nomor ID Karyawan Yang Akan Di Hapus Tidak Ada Di Database'.center(125, '='))
                pembatas2()
        elif hapusdata == 2:
            return
        else:
            print("Pilihan yang Anda masukkan salah, silahkan pilih menu yang sesuai [1-2]".center(125, '-'))
#Main Menu

def main_menu():
    print('='*125)
    print('PT ABC MAJU JAYA'.center(125,'-'))
    print('='*125)
    print('1. Report Data Karyawan')
    print('2. Tambahkan Data Karyawan')
    print('3. Mengupdate Data Karyawan')
    print('4. Menghapus Data Karyawan')
    print('5. Exit')

#Menu
def menu():
    while True:
            pembatas2()
            print('REPORT DATA KARYAWAN'.center(125,'-'))
            main_menu()
            Opsi = input('Silahkan Masukan Pilihan Pada Main Menu [1-5]:')
            if Opsi=='1':
                 ReadData()
            elif Opsi== '2':
                 CreateData()
            elif Opsi == '3':
                 UpdateData()
            elif Opsi == '4':
                 DeleteData()
            elif Opsi == '5':
                 pembatas2()
                 print('Terimakasih Telah Mengunjungi Report Data Karyawan'.center(125, '-'))
                 print('PT ABC MAJU JAYA'.center(125,'-'))
                 pembatas2()
                 break
            else:
                 print('Pilihan Yang Anda Masukan Salah, Silahkan Pilih Menu Yang Sesuai [1-5]')
menu()