import json
import tkinter as tk
from tkinter import filedialog

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            print(f"Datnes garums: {len(data)}")

            for key in data.keys():
                print(key)

            for value in data.values():
                print(value)

            search_key = input("Ievadiet atslēgu, kuru vēlāties pārbaudīt: ")
            if search_key in data:
                print(f"Atslēgai {search_key} vērtība ir: {data[search_key]}")
            else:
                print(f"Nav tādas atslēgas vārdnīcā.")
    except Exception as e:
        print(f'Notikusi kļuda: {e}')


def open_file():
    """Atver faila izvēles logu un apstrādā izvēlēto JSON failu."""
    root = tk.Tk()
    root.withdraw()  # Paslēpj tkinter galveno logu

    # Atver faila izvēles logu, ierobežots uz JSON failiem
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    
    # Ja fails ir izvēlēts, analizējam to
    if file_path:
        analyze_file(file_path)
    else:
        print("Fails netika izvēlēts.")

# Izsauc funkciju faila izvēlei un apstrādei
open_file()


