import pywhatkit as kit
import time

# Meminta input nomor target
nomor_target = input("Masukkan nomor (dalam format internasional, misal +62123456789): ")

# Mengirim pesan spam sebanyak 100 kali
for i in range(100):
    kit.sendwhatmsg(nomor_target, "Ini adalah pesan spam tautkan perangkat.", time.localtime().tm_hour, time.localtime().tm_min + i)
    time.sleep(60)  # Tunggu 60 detik antara pengiriman
