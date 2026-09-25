while True:
    input_kursi = input("Masukkan jumlah kursi: ")

    try:
        n_kursi = int(input_kursi)
    except ValueError:
        print("Input jumlah kursi harus berupa angka!")
        continue

    if n_kursi <= 0:
        print("Jumlah kursi harus lebih dari 0!")
        continue

    break

print("\n=== Sistem Reservasi PO BUS Dimulai ===\n")

sisa_kursi = n_kursi
total_pendapatan = 0

while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")

    input_umur = input("Masukkan umur penumpang: ")

    try:
        umur = int(input_umur)
    except ValueError:
        print("Input umur harus berupa angka!\n")
        continue

    if umur < 0:
        print("Umur tidak valid!\n")
        continue

    if 0 <= umur <= 5:
        harga = 0
        print("Kategori: Balita - Tiket Gratis (Rp 0)\n")

    elif 6 <= umur <= 12:
        harga = 50000
        print("Kategori: Anak - Harga: Rp 50.000\n")

    else:
        harga = 100000
        print("Kategori: Dewasa - Harga: Rp 100.000\n")

    total_pendapatan += harga
    sisa_kursi -= 1

print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")