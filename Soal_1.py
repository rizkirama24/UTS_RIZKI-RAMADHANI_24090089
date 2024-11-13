# Program Operasi Penjumlahan dan Pengurangan

def main():
    try:
        a = float(input("Masukkan nilai a: "))  # Input nilai a
        b = float(input("Masukkan nilai b: "))  # Input nilai b
        
        jumlah = a + b  # Hasil penjumlahan
        selisih = a - b  # Hasil pengurangan
        
        print(f"Hasil penjumlahan (a + b): {jumlah}")  # Tampilkan hasil penjumlahan
        print(f"Hasil pengurangan (a - b): {selisih}")  # Tampilkan hasil pengurangan

    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

if __name__ == "__main__":
    main()