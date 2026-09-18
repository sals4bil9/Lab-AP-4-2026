menu = ["kopi susu", "Matcha latte", "Americano",]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]
subttotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]
biaya_operasionaL = 15000
total_seluruh = sum(subttotal_pendapatan)
pendapatan_bersih = total_seluruh - biaya_operasionaL
jumlah_barang_terjual = sum(jumlah)
target_tercapai = total_seluruh > 200000 or jumlah_barang_terjual > 10
print("=== laporan penjualan kopi senja ===")
print(sub_kopi)
print(f"subtotal Matcha latte : Rp{sub_matcha}")
print(f"subtotal Americano : Rp{sub_americano}")
print(f"total pendapatan : Rp{total_seluruh}")
print(f"pendapatan bersih : Rp{pendapatan_bersih}")
print(f"jumlah barang terjual : {jumlah_barang_terjual}")
print(f"target tercapai : {target_tercapai}")   