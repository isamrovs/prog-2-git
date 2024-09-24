import csv
import tkinter as tk
from tkinter import filedialog

# Funkcija CSV datnes lasīšanai un pārveidošanai par masīvu
def read_csv(file_path):
    try:
        # Izmantojam pareizu nosaukumu csvfile, nevis cvsfile
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            return data
    except Exception as e:
        print(f"Radās kļūda: {e}")
        return None

# Funkcija, lai parādītu datnes analīzes rezultātus
def analyze_csv(data):
    if data:
        # 1. Izvadi masīva garumu
        print(f"Masīva garums: {len(data)}")

        # 2. Izvadi pirmo elementu (rindu) no masīva
        if len(data) > 0:
            print(f"Datnes pirmais elements: {data[0]}")

        # 3. Izvadi pirmos 5 elementus (vai mazāk, ja nav tik daudz elementu)
        if len(data) >= 5:
            print(f"Datnes pirmie 5 elementi: {data[:5]}")  # Pareizs sagriezuma diapazons
        else:
            print(f"Datnes pirmie {len(data)} elementi: {data}")
    else:
        print("Masīvs ir tukšs vai radās kļūda.")

# Izmantojam tkinter, lai atvērtu faila izvēles dialogu
def open_file():
    root = tk.Tk()
    root.withdraw()  # Paslēpjam tkinter logu

    # Atveram faila izvēles logu, ierobežojam līdz CSV failiem
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    # Ja fails ir izvēlēts, analizējam to
    if file_path:
        data = read_csv(file_path)
        analyze_csv(data)
    else:
        print("Fails netika izvēlēts.")

# Izsaucam funkciju faila izvēlei un apstrādei
open_file()
