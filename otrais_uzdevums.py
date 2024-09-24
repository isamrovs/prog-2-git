import csv
import tkinter as tk
from tkinter import filedialog

def read_csv(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            return data
    except Exception as e:
        print(f"Rādās kļūda: {e}")
        return None
    
def analyze_csv(data):
    if data:
        print(f"Masīva garums: {len(data)}")

        if len(data) > 0:
            print(f"Datnes pirmais elements: {data[0]}")

        if len(data) >= 5:
            print(f"Datnes pirmie 5 elementi: {data[:5]}")  # Pareizs sagriezuma diapazons
        else:
            print(f"Datnes pirmie {len(data)} elementi: {data}")
    else:
        print("Masīvs ir tukšs vai radās kļūda.")

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

open_file()


