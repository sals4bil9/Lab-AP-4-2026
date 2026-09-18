nilai = int(input("Masukkan nilai: "))
pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))

if nilai >= 80:
    print("lolos ke tahap wawancara")
elif nilai >= 65 and pengalaman >= 2:
    print("lolos bersyarat")
else:
    print("tidak lolos")