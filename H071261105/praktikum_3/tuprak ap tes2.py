print("=== Setup Denah Bioskop NontonYuk ===")

while True:
    input_baris = input("Masukkan jumlah baris: ")

    try:
        n_baris = int(input_baris)
    except ValueError:
        print("Input baris harus berupa angka!\n")
        continue

    if n_baris <= 0:
        print("Jumlah baris harus lebih dari 0!\n")
        continue

    break

while True:
    input_kursi = input("Masukkan jumlah kursi per baris: ")

    try:
        m_kursi = int(input_kursi)
    except ValueError:
        print("Input kursi harus berupa angka!\n")
        continue

    if m_kursi <= 0:
        print("Jumlah kursi harus lebih dari 0!\n")
        continue

    break

print("\n=== Daftar Kursi Tersedia ===")

for baris in range(1, n_baris + 1):
    for kursi in range(1, m_kursi + 1):

        if kursi == 13:
            continue

        if baris == 1:
            if kursi % 2 == 1:
                print(f"Baris {baris} - Kursi {kursi}")

        else:
            print(f"Baris {baris} - Kursi {kursi}")