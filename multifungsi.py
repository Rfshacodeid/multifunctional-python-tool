import random
import string
import os
import shutil
from datetime import datetime
import pyfiglet
import math
import calendar
from urllib.request import urlopen
import json
import time
import requests

def display_welcome_message():
    welcome_text = pyfiglet.figlet_format("Created By", font="slant")
    creator_text = pyfiglet.figlet_format("Rafasha Alfiandi", font="slant")
    contact_text = "\nKontak: https://T.me/Rafashaalfian\nSelamat menggunakan fitur yang saya buat ;)\n"

    print(welcome_text)
    time.sleep(1)  
    print(creator_text)
    time.sleep(1)
    print(contact_text)
    time.sleep(1)

def display_menu():
    print("\n=== Multifungsi Python Program ===")
    print("1. Kalkulator")
    print("2. Konversi Mata Uang (USD ke IDR)")
    print("3. Generator Password")
    print("4. Seni ASCII")
    print("5. Informasi Waktu Saat Ini")
    print("6. Hitung Faktorial")
    print("7. Periksa Tahun Kabisat")
    print("8. Kalender Bulanan")
    print("9. Cuaca Saat Ini (API)")
    print("10. Tebak Angka (Game)")
    print("11. Cari Bilangan Prima dalam Rentang")
    print("12. Cek Informasi Nomor HP")
    print("13. Keluar")
    print("===============================")

def cek_informasi_nomor_hp():
    print("\n--- Cek Informasi Nomor HP ---")
    try:
        phone_number = input("Masukkan nomor HP dengan kode negara (contoh: +6281234567890): ").strip()
        api_key = "YOUR_API_KEY_HERE"  # Ganti dengan API key dari numverify.com
        url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code=&format=1"
        
        response = requests.get(url)
        data = response.json()
        
        if data['valid']:
            print(f"Nomor HP: {data['international_format']}")
            print(f"Negara: {data['country_name']} ({data['country_code']})")
            print(f"Operator: {data['carrier']}")
            print(f"Jenis: {'Mobile' if data['line_type'] == 'mobile' else 'Lainnya'}")
            print(f"Lokasi: {data.get('location', 'Tidak tersedia')}")
            print(f"Kode negara: {data.get('country_prefix', 'Tidak tersedia')}")
            print(f"Kode operator: {data.get('carrier', 'Tidak tersedia')}")
            print(f"Format lokal: {data.get('local_format', 'Tidak tersedia')}")
            print(f"Wilayah: {data.get('location', 'Tidak tersedia')}")
            print(f"Kemungkinan pengguna: {data.get('line_type', 'Tidak tersedia')}")
            print(f"Validitas: {'Valid' if data.get('valid') else 'Tidak Valid'}")
            print(f"Timezone: {data.get('location', 'Tidak tersedia')}")
            print(f"Kemungkinan penggunaan bisnis: {'Ya' if 'business' in data.get('carrier', '').lower() else 'Tidak'}")
        else:
            print("Nomor tidak valid.")
    except Exception as e:
        print(f"Error: {e}")

def kalkulator():
    print("\n--- Kalkulator ---")
    try:
        num1 = float(input("Masukkan angka pertama: "))
        operator = input("Masukkan operator (+, -, *, /, **, %): ")
        num2 = float(input("Masukkan angka kedua: "))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        elif operator == "**":
            result = num1 ** num2
        elif operator == "%":
            result = num1 % num2
        else:
            print("Operator tidak valid.")
            return
        
        print(f"Hasil: {result}")
    except Exception as e:
        print(f"Error: {e}")

def konversi_mata_uang():
    print("\n--- Konversi Mata Uang (USD ke IDR) ---")
    try:
        rate = 15000  
        usd = float(input("Masukkan jumlah dalam USD: "))
        idr = usd * rate
        print(f"{usd} USD = {idr:,.2f} IDR")
    except Exception as e:
        print(f"Error: {e}")

def generator_password():
    print("\n--- Generator Password ---")
    try:
        length = int(input("Masukkan panjang password: "))
        if length < 1:
            print("Panjang password harus lebih dari 0.")
            return
        
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"Password yang dihasilkan: {password}")
    except Exception as e:
        print(f"Error: {e}")

def seni_ascii():
    print("\n--- Seni ASCII ---")
    fonts = ["slant", "block", "bubble", "digital", "lean", "script", "standard", "banner"]
    
    print("Pilih model seni ASCII:")
    for i, font in enumerate(fonts, start=1):
        print(f"{i}. {font.capitalize()}")

    try:
        choice = int(input("Masukkan nomor pilihan font (1-8): "))
        if 1 <= choice <= len(fonts):
            font = fonts[choice - 1]
            text = input("Masukkan teks: ")
            ascii_art = pyfiglet.figlet_format(text, font=font)
            print(ascii_art)
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    except Exception as e:
        print(f"Error: {e}")

def waktu_saat_ini():
    print("\n--- Informasi Waktu Saat Ini ---")
    now = datetime.now()
    print("Waktu saat ini:", now.strftime("%Y-%m-%d %H:%M:%S"))

def hitung_faktorial():
    print("\n--- Hitung Faktorial ---")
    try:
        num = int(input("Masukkan angka: "))
        if num < 0:
            print("Faktorial tidak didefinisikan untuk angka negatif.")
            return
        result = math.factorial(num)
        print(f"Faktorial dari {num} adalah {result}")
    except Exception as e:
        print(f"Error: {e}")

def periksa_tahun_kabisat():
    print("\n--- Periksa Tahun Kabisat ---")
    try:
        year = int(input("Masukkan tahun: "))
        if calendar.isleap(year):
            print(f"{year} adalah tahun kabisat.")
        else:
            print(f"{year} bukan tahun kabisat.")
    except Exception as e:
        print(f"Error: {e}")

def kalender_bulanan():
    print("\n--- Kalender Bulanan ---")
    try:
        year = int(input("Masukkan tahun: "))
        month = int(input("Masukkan bulan (1-12): "))
        if 1 <= month <= 12:
            print(calendar.month(year, month))
        else:
            print("Bulan tidak valid.")
    except Exception as e:
        print(f"Error: {e}")

def cuaca_saat_ini():
    print("\n--- Cuaca Saat Ini ---")
    try:
        city = input("Masukkan nama kota: ").strip()
        api_key = "be2fbce957441bd5f28348a8a9ab448e"  # Jangan di ganti kalo gk mau eror
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        response = urlopen(url)
        data = json.loads(response.read())
        
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        print(f"Cuaca di {city}: {weather.capitalize()}, Suhu: {temp}°C")
    except Exception as e:
        print(f"Error: {e}")

def tebak_angka():
    print("\n--- Game Tebak Angka ---")
    try:
        number = random.randint(1, 100)
        attempts = 0
        print("Saya telah memilih angka antara 1 dan 100. Tebak angkanya!")
        
        while True:
            guess = int(input("Masukkan tebakan Anda: "))
            attempts += 1
            
            if guess < number:
                print("Terlalu kecil!")
            elif guess > number:
                print("Terlalu besar!")
            else:
                print(f"Selamat! Anda menebak dengan benar dalam {attempts} percobaan.")
                break
    except Exception as e:
        print(f"Error: {e}")

def cari_prima():
    print("\n--- Cari Bilangan Prima ---")
    try:
        start = int(input("Masukkan awal rentang: "))
        end = int(input("Masukkan akhir rentang: "))
        primes = [num for num in range(start, end + 1) if num > 1 and all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))]
        print(f"Bilangan prima dalam rentang {start} hingga {end}: {primes}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    display_welcome_message()
    while True:
        display_menu()
        choice = input("Pilih opsi (1-13): ").strip()
        
        if choice == "1":
            kalkulator()
        elif choice == "2":
            konversi_mata_uang()
        elif choice == "3":
            generator_password()
        elif choice == "4":
            seni_ascii()
        elif choice == "5":
            waktu_saat_ini()
        elif choice == "6":
            hitung_faktorial()
        elif choice == "7":
            periksa_tahun_kabisat()
        elif choice == "8":
            kalender_bulanan()
        elif choice == "9":
            cuaca_saat_ini()
        elif choice == "10":
            tebak_angka()
        elif choice == "11":
            cari_prima()
        elif choice == "12":
            cek_informasi_nomor_hp()
        elif choice == "13":
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
