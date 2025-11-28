DATA_MAHASISWA = []

def tambah():
    """Menambah data nama dan nilai mahasiswa baru."""
    print("\n--- Tambah Data Mahasiswa ---")
    nama = input("Masukkan Nama Mahasiswa: ")
    
    # Validasi input nilai
    while True:
        try:
            nilai = float(input("Masukkan Nilai: "))
            if 0 <= nilai <= 100:
                break
            else:
                print("Nilai harus antara 0 sampai 100.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka untuk Nilai.")

    # Cek duplikasi nama sebelum menambah
    for mahasiswa in DATA_MAHASISWA:
        if mahasiswa['Nama'].lower() == nama.lower():
            print(f"❌ Error: Nama '{nama}' sudah ada dalam daftar. Gunakan fungsi ubah() jika ingin memperbarui.")
            return

    DATA_MAHASISWA.append({
        'Nama': nama,
        'Nilai': nilai
    })
    print(f"✅ Data '{nama}' berhasil ditambahkan.")

def tampilkan():
    """Menampilkan seluruh daftar nilai mahasiswa."""
    print("\n--- Daftar Nilai Mahasiswa ---")
    if not DATA_MAHASISWA:
        print("Daftar mahasiswa kosong.")
        return

    # Urutkan berdasarkan nama agar lebih mudah dibaca
    DATA_MAHASISWA.sort(key=lambda m: m['Nama'])
    
    # Format Tampilan
    print("-" * 35)
    print(f"{'No.':<5}{'Nama':<20}{'Nilai':>10}")
    print("-" * 35)
    
    for i, mahasiswa in enumerate(DATA_MAHASISWA, 1):
        # Format nilai menjadi satu angka di belakang koma (atau sesuai kebutuhan)
        nilai_str = f"{mahasiswa['Nilai']:.1f}" 
        print(f"{i:<5}{mahasiswa['Nama']:<20}{nilai_str:>10}")
    print("-" * 35)

def hapus(nama=None):
    """Menghapus data mahasiswa berdasarkan nama."""
    print("\n--- Hapus Data Mahasiswa ---")
    if not DATA_MAHASISWA:
        print("Daftar mahasiswa kosong, tidak ada yang bisa dihapus.")
        return
        
    nama_cari = nama if nama else input("Masukkan Nama Mahasiswa yang akan dihapus: ")
    nama_cari = nama_cari.strip().lower()

    # Mencari dan menghapus data
    for i, mahasiswa in enumerate(DATA_MAHASISWA):
        if mahasiswa['Nama'].lower() == nama_cari:
            DATA_MAHASISWA.pop(i)
            print(f"🗑️ Data '{mahasiswa['Nama']}' berhasil dihapus.")
            return

    print(f"❌ Error: Nama '{nama_cari}' tidak ditemukan.")

def ubah(nama=None):
    """Mengubah nilai mahasiswa berdasarkan nama."""
    print("\n--- Ubah Nilai Mahasiswa ---")
    if not DATA_MAHASISWA:
        print("Daftar mahasiswa kosong, tidak ada yang bisa diubah.")
        return
        
    nama_cari = nama if nama else input("Masukkan Nama Mahasiswa yang nilainya akan diubah: ")
    nama_cari = nama_cari.strip().lower()

    # Mencari data
    for mahasiswa in DATA_MAHASISWA:
        if mahasiswa['Nama'].lower() == nama_cari:
            print(f"Data ditemukan: Nama: {mahasiswa['Nama']}, Nilai saat ini: {mahasiswa['Nilai']}")
            
            # Validasi input nilai baru
            while True:
                try:
                    nilai_baru = float(input("Masukkan Nilai Baru: "))
                    if 0 <= nilai_baru <= 100:
                        break
                    else:
                        print("Nilai harus antara 0 sampai 100.")
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka untuk Nilai.")
            
            mahasiswa['Nilai'] = nilai_baru
            print(f"✏️ Nilai '{mahasiswa['Nama']}' berhasil diubah menjadi {nilai_baru}.")
            return

    print(f"❌ Error: Nama '{nama_cari}' tidak ditemukan.")


def menu_utama():
    """Menampilkan menu interaktif utama program."""
    while True:
        print("\n" + "=" * 30)
        print("SISTEM MANAJEMEN NILAI (CRUD)")
        print("=" * 30)
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Ubah Nilai (berdasarkan Nama)")
        print("4. Hapus Data (berdasarkan Nama)")
        print("5. Keluar")
        print("-" * 30)

        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            tampilkan()
        elif pilihan == '3':
            ubah()
        elif pilihan == '4':
            hapus()
        elif pilihan == '5':
            print("Terima kasih, program dihentikan.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 1 sampai 5.")

# Memulai program
if __name__ == "__main__":
    menu_utama()