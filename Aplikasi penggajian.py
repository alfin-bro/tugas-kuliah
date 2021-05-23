import os

# membuat wadah untuk menampung data karyawan
daftar_karyawan = []


# kumpulan function
# function untuk mendapatkan data karyawan
def input_data():
    print("="*20)
    print("Silahkan input data!")
    No = int(input('Data ke :'))
    Nip = int(input('Masukkan NIP :'))
    Nama = input('Masukkan nama :')
    KodeJabatan = int(input('Masukkan kode Jabatan (1/2) :'))
    if KodeJabatan == 1:
        Status = input('Masukkan status (M/S)')
        if Status == 'M':
            tunjangan = 200000
        elif Status == 'S':
            tunjangan = 100000
        jabatan = 'Administrasi'
        gajiPokok = 800000
    elif KodeJabatan == 2:
        Status = input('Masukkan status (M/S)')
        if Status == 'M':
            tunjangan = 250000
        elif Status == 'S':
            tunjangan = 150000
        jabatan = 'Oprasional'
        gajiPokok = 850000
    else:
        print('Kode salah')
        
    karyawan = {
        'nama' : Nama,
        'nip' : Nip,
        'no' : No,
        'jabatan' : jabatan,
        'kode_jabatan': KodeJabatan,
        'gaji' : gajiPokok,
        'tunjangan': tunjangan,
        'status': Status,
        'total_gaji' : (gajiPokok + tunjangan)
    }
    return karyawan


# function untuk mencetak slip gaji
def cetak_slip(daftar_karyawan):
    print('\t\t\t\t Daftar Gaji Karyawan')
    print('\t\t\t\t     PT UNIVERSAL')
    print('='*80)
    print('-'*80)
    print(f"Bulan : {Bulan}")
    print('='*80)
    print('No\tNIP\tNama\tJabatan\t\tStatus\tG.pokok\t Tunjangan\tTot.gaji')
    print('='*80)
    for karyawan in daftar_karyawan:
        print(f"{karyawan['no']}\t{karyawan['nip']}\t{karyawan['nama']}\t{karyawan['jabatan']}\t{karyawan['status']}\t{karyawan['gaji']}\t  {karyawan['tunjangan']}\t{karyawan['total_gaji']}")
        print('='*80)
    print(f"\t\t\t\t\t   Total gaji karyawan :    Rp. {sum([gaji['total_gaji'] for gaji in daftar_karyawan])}")
# end function


# perulangan pilihan menu
while True:
    print("======= SELAMAT DATANG DI APLIKASI PENGGAJIAN =====")
    print("1. Tambah data")
    print("2. Cetak slip")
    print("0. Keluar")
    print()
    pilih_menu = int(input("Silahkan pilih menu ..  "))
    if pilih_menu == 0:
        break
    elif pilih_menu == 1:
        os.system('cls')
        daftar_karyawan.append(input_data())
    elif pilih_menu == 2:
        Bulan = input('Masukkan Bulan :')
        os.system('cls')
        cetak_slip(daftar_karyawan)
        print('\n\n\n')

print("Program telah ditutup , jumpa lagi")