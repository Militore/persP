import random
from datetime import datetime
import webbrowser
from crossref.restful import Works
import json

def start():
    print("\nAvailable functions: \nstart, \ndc (decrypt_caesar), \nkinc (kelvin in celcius), \npwd (random password), \nrand (random number), \ndoi (open doi link), \nstop, exit")
    launch_func = input("What function would you like to launch? ^_`\n\n")
    if(launch_func == ""): exit()
    else: result = eval(launch_func+'()')

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

def doi():
    works = Works()

    doi = input("Введите дои\n")
    final = works.doi(doi)
    def authors(final):
        if(final['type']=='book'):
            authors = final['editor']
        else:
            authors = final['author']
        am=0
        i=0
        while(i<len(authors)):
            if('given' in authors[i]):
                print('Автор: '+authors[i]['given']+' '+authors[i]['family'])
                am=am+1
                i=i+1
            else:
                i=i+1
        print('Количество авторов: '+str(am))
    print('\n')
    authors(final)   
    print('Название: '+''.join(final['title']))
    print('Журнал: '+''.join(final['container-title']))
    print('Год: '+''.join(str(final['created']['date-parts'][0][0])))
    print('Том: ', end="")
    if('volume' in final):
        print(''.join(final['volume']), end="")
    print('')
    print('Номер: ', end="")
    if('issue' in final): 
        print(''.join(final['issue']), end="")
    print('')
    print('Страница: ', end="")
    if('page' in final):
        print(''.join(final['page']), end="")
    print('')
    print('Издатель: ', end="")
    if('publisher' in final):
        print(''.join(final['publisher']), end="")
    print('')
    if('publisher-location' in final):
        print('Местоположение: '+''.join(final['publisher-location']))
    print('DOI: '+''.join(final['DOI']))
    print('Тип: '+''.join(final['type']))
    print('\n')
    start()

start()
