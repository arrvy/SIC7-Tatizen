# =========================
# utils.py
# Modul fungsi matematika
# =========================
import math

def validate_number(prompt):
    """Meminta input angka dengan validasi."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Input tidak valid! Masukkan angka saja.")

def tambah(a, b):
    """Menjumlahkan dua angka."""
    return a + b

def kurang(a, b):
    """Mengurangi dua angka."""
    return a - b

def kali(a, b):
    """Mengalikan dua angka."""
    return a * b

def bagi(a, b):
    """Membagi dua angka. Tangani pembagian nol."""
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    return a / b

def modulus(a, b):
    """Mengambil sisa bagi dua angka."""
    if b == 0:
        return "Error: Modulus dengan nol tidak diperbolehkan."
    return a % b

def pangkat(a, b):
    """Memangkatkan angka a dengan b."""
    return a ** b

def rata_rata(*args):
    """Menghitung rata-rata dari sekumpulan angka."""
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

def akar_kuadrat(a):
    return math.sqrt(a) if a >= 0 else "❌ Error: Akar dari bilangan negatif"

def nilai_mutlak(a):
    return abs(a)

def nilai_maksimum(a, b):
    return max(a, b)

def nilai_minimum(a, b):
    return min(a, b)