#  Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
#  Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 

# Считываю исходный текс из файла
with open('Original_text.txt', 'r') as data:
    my_text = data.read()
print ("Оригинальный текст")   
print("")
print(my_text) 

# Кодирую его
def encoding(text):
    str_code = ''
    prev_char = ''
    count = 1
    prev_char = ''
    
    for s in text:
        if s != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = s
        else:
            count += 1
    else:
        str_code += str(count) + prev_char
        return str_code

encod = encoding(my_text)
print ("Закодированный текст")   
print("")
print(encod) 

# Записываю закодированный текс в другой файл
with open('Compressed_text.txt','w') as data:
    data.write(str(encod)) 
 

def decoding(text):
    result = ''
    count = ''
    for s in text:
        if s.isdigit():
            count += s
        else:
            result += s * int(count)
            count = ''
    return result

decode = decoding(encod)


# Читаю закодированный файл и раскодирую его (правда как-то кривовато он его раскодирует)
print ("Раскодированный текст")   
print("")
 
with open('Compressed_text.txt', 'r') as data:
    my_text2 = data.read()
print(decoding(my_text2))



