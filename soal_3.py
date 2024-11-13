def main():
    # Meminta pengguna untuk memasukkan jumlah barang
    try:
        jumlah_barang = int(input("Masukkan jumlah barang: "))
        
        # Memastikan jumlah barang positif
        if jumlah_barang <= 0:
            print("Jumlah barang harus lebih dari 0.")
            return
        
        total_harga = 0.0  # Inisialisasi total harga

        # Meminta pengguna untuk memasukkan harga setiap barang
        for i in range(jumlah_barang):
            harga_barang = float(input(f"Masukkan harga barang ke-{i + 1}: "))
            total_harga += harga_barang  # Menambahkan harga barang ke total

        # Menampilkan total harga belanjaan
        print(f"Total harga belanjaan: {total_harga:.2f}")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# Memanggil fungsi utama
if __name__ == "__main__":
    main()