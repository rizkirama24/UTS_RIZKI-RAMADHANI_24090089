def hitung_bmi(berat_badan, tinggi_badan):
    """Fungsi untuk menghitung BMI"""
    bmi = berat_badan / (tinggi_badan ** 2)
    return bmi

def rekomendasi_bmi(bmi):
    """Fungsi untuk memberikan rekomendasi berdasarkan nilai BMI"""
    if bmi < 18.5:
        return "Kekurangan berat badan"
    elif 18.5 <= bmi < 24.9:
        return "Berat badan normal"
    elif 25 <= bmi < 29.9:
        return "Kelebihan berat badan"
    else:
        return "Obesitas"

def main():
    try:
        # Meminta input dari pengguna
        berat_badan = float(input("Masukkan berat badan (kg): "))
        tinggi_badan = float(input("Masukkan tinggi badan (m): "))
        
        # Menghitung BMI
        bmi = hitung_bmi(berat_badan, tinggi_badan)
        
        # Menampilkan hasil
        print(f"Nilai BMI Anda: {bmi:.2f}")
        print(rekomendasi_bmi(bmi))

    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

# Memanggil fungsi utama
if __name__ == "__main__":
    main()