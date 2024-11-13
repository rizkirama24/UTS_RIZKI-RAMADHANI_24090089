def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 10 != 0):
        return True
    else:
        return False

# Menerima input dari pengguna
tahun = int(input("Masukkan tahun: "))

# Mengecek apakah tahun itu merupakan tahun kabisat
if is_leap_year(tahun):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukanlah tahun kabisat.")