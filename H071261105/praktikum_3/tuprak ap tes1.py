# print("--- Rekapitulasi Transaksi Dins Store ---")
# print("Ketik '0' untuk menutup toko dan mengakhiri sesi.\n")

# while True:
#     input_user = input("Masukkan jumlah item: ")

#     try:
#         jumlah = int(input_user)
#     except ValueError:
#         print("Input harus berupa angka!\n")
#         continue  
    
#     if jumlah == 0:
#         print("Toko ditutup. Sesi rekap selesai.")
#         break  
    
#     if jumlah < 0:
#         print("Jumlah tidak boleh negatif\n")
#         continue


#     if jumlah > 100:
#         print("Maksimal 100 item per transaksi!\n")
#         continue

#     print(f"Transaksi {jumlah} item berhasil!\n")
    
# print("---Rekapitulasi Transaksi Dins Store---")
# print("ketik '0' untuk menutup toko dan mengakhiri sesi.\n")

for i in range(1,10):
    if i % 2 == 0:
        break
    else:
        print("ini ganjil")
    print(i)
