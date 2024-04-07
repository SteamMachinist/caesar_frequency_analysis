english_frequencies = {
    'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2,
    'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.15, 'k': 0.77, 'l': 4.0,
    'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9, 'q': 0.095, 'r': 6.0,
    's': 6.3, 't': 9.1, 'u': 2.8, 'v': 0.98, 'w': 2.4, 'x': 0.15,
    'y': 2.0, 'z': 0.074
}
english_alphabet = list(english_frequencies.keys())
english_frequencies = dict(sorted(english_frequencies.items(), key=lambda item: item[1], reverse=True))
english_alphabet_sorted = list(english_frequencies.keys())

russian_frequencies = {
    'а': 8.01, 'б': 1.59, 'в': 4.54, 'г': 1.70, 'д': 2.98, 'е': 8.45,
    'ё': 0.04, 'ж': 0.94, 'з': 1.65, 'и': 7.35, 'й': 1.21, 'к': 3.49,
    'л': 4.40, 'м': 3.21, 'н': 6.70, 'о': 10.97, 'п': 2.81, 'р': 4.73,
    'с': 5.47, 'т': 6.26, 'у': 2.62, 'ф': 0.26, 'х': 0.97, 'ц': 0.48,
    'ч': 1.44, 'ш': 0.73, 'щ': 0.36, 'ъ': 0.04, 'ы': 1.90, 'ь': 1.74,
    'э': 0.32, 'ю': 0.64, 'я': 2.01
}
russian_alphabet = list(russian_frequencies.keys())
russian_frequencies = dict(sorted(russian_frequencies.items(), key=lambda item: item[1], reverse=True))
russian_alphabet_sorted = list(russian_frequencies.keys())


def calculate_coded_text_frequencies(coded_text, alphabet):
    letters_count = dict.fromkeys(alphabet, 0)
    for char in coded_text:
        if char.isalpha():
            char_lower = char.lower()
            letters_count[char_lower] += 1
    total_letters = sum(letters_count.values())
    return {char: count / total_letters * 100 for char, count in letters_count.items()}


def calculate_shift(coded_text, alphabet, alphabet_sorted):
    coded_text_frequencies = calculate_coded_text_frequencies(coded_text, alphabet)
    coded_text_frequencies_sorted = dict(sorted(coded_text_frequencies.items(), key=lambda item: item[1], reverse=True))
    coded_text_alphabet_sorted = list(coded_text_frequencies_sorted.keys())

    shifts = []
    for coded_letter, letter in zip(coded_text_alphabet_sorted, alphabet_sorted):
        shifts.append((alphabet.index(coded_letter) - alphabet.index(letter)) % len(alphabet))
    return max(set(shifts), key=shifts.count)


def caesar_decipher(coded_text, shift, alphabet):
    deciphered_text = ""
    for char in coded_text:
        if char.isalpha():
            char_lower = char.lower()
            index = alphabet.index(char_lower)
            new_index = (index - shift) % len(alphabet)
            deciphered_char = alphabet[new_index]
            deciphered_char = deciphered_char.upper() if char.isupper() else deciphered_char
            deciphered_text += deciphered_char
        else:
            deciphered_text += char
    return deciphered_text


def frequency_crypto_analysis(coded_text, language):
    if language == 'english':
        alphabet = english_alphabet
        alphabet_sorted = english_alphabet_sorted
    elif language == 'russian':
        alphabet = russian_alphabet
        alphabet_sorted = russian_alphabet_sorted
    else:
        raise ValueError("Unsupported language")

    shift = calculate_shift(coded_text, alphabet, alphabet_sorted)
    deciphered_text = caesar_decipher(coded_text, shift, alphabet)
    return deciphered_text


def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def write_to_file(text):
    with open('decoded.txt', 'w', encoding='utf-8') as file:
        file.write(text)


# decoded = frequency_crypto_analysis(read_from_file('encoded_eng2.txt'), 'english')
decoded = frequency_crypto_analysis(read_from_file('encoded_rus2.txt'), 'russian')
write_to_file(decoded)
