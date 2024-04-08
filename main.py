from wordfreq import tokenize
from wordfreq import top_n_list

# частотность букв в английском тексте с википедии
english_frequencies = {
    'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2,
    'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.15, 'k': 0.77, 'l': 4.0,
    'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9, 'q': 0.095, 'r': 6.0,
    's': 6.3, 't': 9.1, 'u': 2.8, 'v': 0.98, 'w': 2.4, 'x': 0.15,
    'y': 2.0, 'z': 0.074
}

english_alphabet = list(english_frequencies.keys())
english_frequencies = dict(sorted(english_frequencies.items(),
                                  key=lambda item: item[1],
                                  reverse=True))
english_alphabet_sorted = list(english_frequencies.keys())

top_en_n_grams_1 = [i for i in top_n_list('en', 100) if len(i) == 1 and i.isalpha()][:10]
top_en_n_grams_2 = [i for i in top_n_list('en', 100) if len(i) == 2 and i.isalpha()][:10]
top_en_n_grams_3 = [i for i in top_n_list('en', 100) if len(i) == 3 and i.isalpha()][:10]
top_en_n_grams_4 = [i for i in top_n_list('en', 100) if len(i) == 4 and i.isalpha()][:10]

# частотность букв в русском тексте с википедии
russian_frequencies = {
    'а': 8.01, 'б': 1.59, 'в': 4.54, 'г': 1.70, 'д': 2.98, 'е': 8.45,
    'ё': 0.04, 'ж': 0.94, 'з': 1.65, 'и': 7.35, 'й': 1.21, 'к': 3.49,
    'л': 4.40, 'м': 3.21, 'н': 6.70, 'о': 10.97, 'п': 2.81, 'р': 4.73,
    'с': 5.47, 'т': 6.26, 'у': 2.62, 'ф': 0.26, 'х': 0.97, 'ц': 0.48,
    'ч': 1.44, 'ш': 0.73, 'щ': 0.36, 'ъ': 0.04, 'ы': 1.90, 'ь': 1.74,
    'э': 0.32, 'ю': 0.64, 'я': 2.01
}
russian_alphabet = list(russian_frequencies.keys())
russian_frequencies = dict(sorted(russian_frequencies.items(),
                                  key=lambda item: item[1],
                                  reverse=True))
russian_alphabet_sorted = list(russian_frequencies.keys())

top_ru_n_grams_1 = [i for i in top_n_list('ru', 100) if len(i) == 1 and i.isalpha()][:10]
top_ru_n_grams_2 = [i for i in top_n_list('ru', 100) if len(i) == 2 and i.isalpha()][:10]
top_ru_n_grams_3 = [i for i in top_n_list('ru', 100) if len(i) == 3 and i.isalpha()][:10]
top_ru_n_grams_4 = [i for i in top_n_list('ru', 100) if len(i) == 4 and i.isalpha()][:10]


def calculate_letter_frequencies(text, alphabet):
    letters_count = dict.fromkeys(alphabet, 0)
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            letters_count[char_lower] += 1
    total_letters = sum(letters_count.values())
    return {char: count / total_letters * 100 for char, count in letters_count.items()}


def calculate_shift_letters_freq(coded_text, alphabet, alphabet_sorted):
    coded_text_frequencies = calculate_letter_frequencies(coded_text, alphabet)

    coded_text_frequencies_sorted = dict(
        sorted(coded_text_frequencies.items(),
               key=lambda item: item[1],
               reverse=True))

    coded_text_alphabet_sorted = list(coded_text_frequencies_sorted.keys())

    print(f"Алфавит языка, отсортированный по частоте: \n{alphabet_sorted}")
    print(f"Алфавит текста, отсортированный по частоте: \n{coded_text_alphabet_sorted}")

    shifts = {}
    for coded_letter, letter in zip(coded_text_alphabet_sorted, alphabet_sorted):
        shifts[coded_letter] = ((alphabet.index(coded_letter) - alphabet.index(letter)) % len(alphabet))

    print(f"\nСдвиги букв: \n{shifts}")
    most_common_shift = max(set(shifts.values()),
                            key=list(shifts.values()).count)

    print(f"\nСамый распространненный сдвиг: {most_common_shift}")

    return dict.fromkeys(alphabet, most_common_shift)


def frequency_crypto_analysis_letters_freq(coded_text, language):
    print("\n\nПо частоте букв:")
    if language == 'en':
        alphabet = english_alphabet
        alphabet_sorted = english_alphabet_sorted
    elif language == 'ru':
        alphabet = russian_alphabet
        alphabet_sorted = russian_alphabet_sorted
    else:
        raise ValueError("Unsupported language")

    shifts = calculate_shift_letters_freq(coded_text, alphabet, alphabet_sorted)
    deciphered_text = caesar_decipher(coded_text, shifts, alphabet)
    return deciphered_text


def count_words_count(words):
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
    return dict(sorted(words_count.items(),
                       key=lambda item: item[1],
                       reverse=True))


def get_top_n_grams(words_count):
    return ([k for k, v in words_count.items() if len(k) == i] for i in range(1, 5))


def calculate_shift_n_grams_freq(coded_text, lang, alphabet, alphabet_sorted,
                                 top_n_grams_1, top_n_grams_2, top_n_grams_3, top_n_grams_4):
    coded_text_frequencies = calculate_letter_frequencies(coded_text, alphabet)

    coded_text_frequencies_sorted = dict(
        sorted(coded_text_frequencies.items(),
               key=lambda item: item[1],
               reverse=True))

    coded_text_alphabet_sorted = list(coded_text_frequencies_sorted.keys())

    print(f"Алфавит языка, отсортированный по частоте: \n{alphabet_sorted}")
    print(f"Алфавит текста, отсортированный по частоте: \n{coded_text_alphabet_sorted}")
    print("\n")

    words = tokenize(coded_text, lang)

    words_count = count_words_count(words)

    coded_top_n_grams_1, coded_top_n_grams_2, coded_top_n_grams_3, coded_top_n_grams_4 \
        = get_top_n_grams(words_count)

    print(f"Топ n-грамм языка 1 букв.: {top_n_grams_1}")
    print(f"Топ n-грамм языка 2 букв.: {top_n_grams_2}")
    print(f"Топ n-грамм языка 3 букв.: {top_n_grams_3}")
    print(f"Топ n-грамм языка 4 букв.: {top_n_grams_4}")
    print("")
    print(f"Топ n-грамм текста 1 букв.: {coded_top_n_grams_1}")
    print(f"Топ n-грамм текста 2 букв.: {coded_top_n_grams_2}")
    print(f"Топ n-грамм текста 3 букв.: {coded_top_n_grams_3}")
    print(f"Топ n-грамм текста 4 букв.: {coded_top_n_grams_4}")

    replace_dict_for_encoded_ru_txt = {
        'э': 'и',
        'е': 'з',
        'м': 'а',
        'ъ': 'н',
        'и': 'к',
        'я': 'д',
        'д': 'е',
        'ж': 'м',
        'у': 'ш',
        'ц': 'о',
        'ь': 'л',
        'с': 'р',
        'з': 'п',
        'л': 'ж',
        'н': 'я',
        'в': 'щ',
        'б': 'ы',
        'й': 'с',
        'п': 'б',
        'ю': 'т',
        'к': 'й',
        'щ': 'в',
        'а': 'ч',
        'ы': 'у',
        'ф': 'г',
        'ш': 'ц',
        'о': 'х',
        'г': 'э',
        'ч': 'ь',
        'т': 'ю',
        'х': 'ъ',
        'р': 'ф',
    }
    print("\n")
    print(f"Выведенный ручным подбором словарь замены букв для текста файла encoded_ru.txt: \n"
          f"{replace_dict_for_encoded_ru_txt}")

    shifts = {}
    for letter, replace in replace_dict_for_encoded_ru_txt.items():
        shifts[letter] = ((alphabet.index(letter) - alphabet.index(replace)) % len(alphabet))
    print("")
    print(f"Полученные сдвиги: \n{shifts}")

    return shifts


def frequency_crypto_analysis_n_grams(coded_text, language):
    print("\n\nПо частоте n-грамм:")
    if language == 'en':
        alphabet = english_alphabet
        alphabet_sorted = english_alphabet_sorted
        top_n_grams_1, top_n_grams_2, top_n_grams_3, top_n_grams_4 \
            = top_en_n_grams_1, top_en_n_grams_2, top_en_n_grams_3, top_en_n_grams_4
    elif language == 'ru':
        alphabet = russian_alphabet
        alphabet_sorted = russian_alphabet_sorted
        top_n_grams_1, top_n_grams_2, top_n_grams_3, top_n_grams_4 \
            = top_ru_n_grams_1, top_ru_n_grams_2, top_ru_n_grams_3, top_ru_n_grams_4
    else:
        raise ValueError("Unsupported language")

    shifts = calculate_shift_n_grams_freq(coded_text, language, alphabet, alphabet_sorted,
                                          top_n_grams_1, top_n_grams_2, top_n_grams_3, top_n_grams_4)
    deciphered_text = caesar_decipher(coded_text, shifts, alphabet)
    return deciphered_text


def caesar_decipher(coded_text, shifts, alphabet):
    deciphered_text = ""
    for char in coded_text:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in shifts:
                shift = shifts[char_lower]
                index = alphabet.index(char_lower)
                new_index = (index - shift) % len(alphabet)
                deciphered_char = alphabet[new_index]
                deciphered_char = deciphered_char.upper() if char.isupper() else deciphered_char
                deciphered_text += deciphered_char
            else:
                deciphered_text += char
        else:
            deciphered_text += char
    return deciphered_text


def read_from_file(filename):
    print(f"Чтение файла {filename}")
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def write_to_file(text, i):
    with open('decoded' + str(i) + '.txt', 'w', encoding='utf-8') as file:
        file.write(text)


# decoded1 = frequency_crypto_analysis_letters_freq(read_from_file('encoded_ru3.txt'), 'ru')
# write_to_file(decoded1, '_letter_freq')

# decoded2 = frequency_crypto_analysis_letters_freq(read_from_file('encoded_en2.txt'), 'en')
# write_to_file(decoded2, '_letter_freq')

decoded3 = frequency_crypto_analysis_n_grams(read_from_file('encoded_ru.txt'), 'ru')
write_to_file(decoded3, '_n_grams_freq')
