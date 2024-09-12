import json

file_input = 'state_capitals.json'
letters_output = 'letters.json'
cities_output = 'cities.json'

def letter_magic(capitals):
    counts = {}
    cities = {}

    # Create counts dictionary from A to Z (Z + 1 to include Z), and set count to 0
    for i in range(ord('A'), ord('Z') + 1):
        counts[chr(i)] = 0
        cities.setdefault(chr(i), [])

    # If city begins with letter, update counts and add city to cities dictionary
    for value in capitals.values():
        first_letter = value[0].upper()
        counts[first_letter] += 1
        cities[first_letter].append(value)

    # Removing letters from cities dictionary if no city begins with that letter
    empty_keys = [k for k,v in cities.items() if not v]
    for k in empty_keys:
        del cities[k]

    # Sort counts dictionary by most commonly used beginning letter (ascending)
    sorted_by_letter = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
    
    # Sort cities dictionary by starting letter
    sorted_by_city = {}
    for k, v in cities.items():
        sorted_by_city[k] = sorted(v)

    convert_to_json(sorted_by_letter, sorted_by_city)

def convert_to_json(sorted_by_letter, sorted_by_city):
    print(f'Printing to {letters_output}...')
    with open(letters_output, 'w', encoding='utf-8') as file:
        json.dump(sorted_by_letter, file, ensure_ascii=False, indent=4)
    print(f'Printing to {cities_output}...')
    with open(cities_output, 'w', encoding='utf-8') as file:
        json.dump(sorted_by_city, file, ensure_ascii=False, indent=4)


with open(file_input, 'r') as file:
    letter_magic(json.load(file))