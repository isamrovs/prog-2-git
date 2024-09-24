def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            number_chars = len(content)
            first_char = content[0] if number_chars > 0 else 'Tukšs fails'
            last_char = content[-1] if number_chars > 0 else 'Tukšs fails'
            first_ten_chars = content[:10] if number_chars >= 10 else content

            print(f"Simbolu skaits failā: {number_chars}")
            print(f"Pirmais simbols: {first_char}")
            print(f"Pēdējais simbols: {last_char}")
            print(f"Pirmie desmit simboli: {first_ten_chars}")
    except FileNotFoundError:
        print("Fails nav atrasts.")
    except Exception as e:
        print(f"Notikusi kļūda: {e}")

file_path = input("Ievadiet faila ceļu (txt formāts): ")
analyze_file(file_path)
