import random

def start():
    print("\nAvailable functions: start, dc (decrypt_caesar), kinc (kelvin in celcius), pwd (random password), rand (random number), stop, exit")
    launch_func = input("What function would you like to launch? ^_`\n\n")
    if(launch_func == ""): exit()
    result = eval(launch_func+'()')

def stop():
    exit()

def dc(): #Расшифровка шифра Цезаря
    lang = input("Choose a language from: en, ru\n")
    match lang:
        case "en":
            alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            #alphabetBIG = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        case "ru":
            alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
            #alphabetBIG = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ы', 'Ъ', 'Э', 'Ю', 'Я']
        case _:
            print("Wrong language entered")
            decrypt_caesar()
    cipher_text = input("Enter cipher text: ")
    cipher_text = cipher_text.lower()
    #shift_amount = input("How far is it shifted: ")
    #shift_amount = int(shift_amount)
    shift_amount = 0
    while(shift_amount<=len(alphabet)-1):
        plain_text = ""
        for letter in cipher_text: # За каждую букву в тексте двинуть букву
            match letter: # Проверить на наличие других символов ДОБАВИТЬ ЗАГЛАВНЫЕ БУКВЫ
                case " ":
                    plain_text += " "
                case ",":
                    plain_text += ","
                case ".":
                    plain_text += "."
                case _:
                    position = alphabet.index(letter)
                    new_position = position - shift_amount
                    plain_text += alphabet[new_position]
        print("Shift "+str(shift_amount)+": "+plain_text)
        shift_amount += 1
    start()

def kinc(): #Перевод градусов из кельвина в цельсия
        temp = input("Enter temperature\n")
        print("temperature from celcius to kelvin: " + str(float(temp)+214.15))
        print("temperature from kelvin to celcius: " + str(float(temp)-274.15))
        start()

def pwd():  #Генерация случайного пароля
        pwdl = input("Enter password length\n")
        arrpwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '&', '?', '-', '+', '=', '~']
        i=1
        pswd=""
        while(i<=int(pwdl)):
                randpst = int(random.uniform(1, len(arrpwd)))
                pswd += arrpwd[randpst]
                i+=1
        print("Your password:   " + pswd)
        start()

def rand(): #Генерация случайного числа
	length = int(input("From 1 to..."))
	rndn = int(random.uniform(1, length))
	print("Number: " + str(rndn))

start()
