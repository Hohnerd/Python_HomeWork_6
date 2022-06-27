# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью ROT13 . Если в строку включены числа или специальные символы, 
# они должны быть возвращены как есть. Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

str = input ("Введите слово или фразу для шифрования: ")

def encoding (coding_string):
    encrypted_string = ''
    for i in coding_string.upper():
        if i in alphabet:
            encrypted_string += alphabet[(alphabet.find(i) + 13) % len(alphabet)]
        else:
            encrypted_string += i
    return encrypted_string

print("В зашифрованном виде это - ",encoding(str))

str = input ("Введите слово или фразу в зашифрованном виде: ")
def decoding (decoding_string):
    decrypted_string = ''
    for i in decoding_string.upper():
        if i in alphabet:
            decrypted_string += alphabet[(alphabet.find(i) - 13) % len(alphabet)]
        else:
            decrypted_string += i
    return decrypted_string

print("Расшифровка - ",decoding(str))

