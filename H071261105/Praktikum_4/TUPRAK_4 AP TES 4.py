def konversi(suhu, asal: str, tujuan: str):
    
    if asal == "C":
        if tujuan == "F":
            return (suhu * 9 / 5) + 32
        elif tujuan == "K":
            return suhu + 273.15
        elif tujuan == "C":
            return suhu

    elif asal == "F":
        if tujuan == "C":
            return (suhu - 32) * 5 / 9
        elif tujuan == "K":
            return (suhu - 32) * 5 / 9 + 273.15
        elif tujuan == "F":
            return suhu

    elif asal == "K":
        if tujuan == "C":
            return suhu - 273.15
        elif tujuan == "F":
            return (suhu - 273.15) * 9 / 5 + 32
        elif tujuan == "K":
            return suhu

    return None


print("=== Konversi Suhu ===")

while True:
    masukkan_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

    if masukkan_suhu.lower() == "selesai":
        print("Program selesai.")
        break

    try:
        suhu = float(masukkan_suhu)
    except ValueError:
        print("Suhu harus berupa angka!")
        continue

    asal = input("Skala asal (C/F/K): ").upper()
    tujuan = input("Skala tujuan (C/F/K): ").upper()

    if asal not in ["C", "F", "K"] or tujuan not in ["C", "F", "K"]:
        print("Error: Skala suhu tidak dikenali.")
        continue

    hasil = konversi(suhu, asal, tujuan)

    print(f"Hasil konversi: {hasil:.2f}°{tujuan}")