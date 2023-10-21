# -*- coding: utf-8 -*-

from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
from requests import get
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()

from sms import SendSms
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)
            
while 1:
    system("cls||clear")
    print("""{}
   _____ __  __  _____   ____   ____  __  __ ____  ______ _____  
  / ____|  \/  |/ ____| |  _ \ / __ \|  \/  |  _ \|  ____|  __ \ 
 | (___ | \  / | (___   | |_) | |  | | \  / | |_) | |__  | |__) |
  \___ \| |\/| |\___ \  |  _ <| |  | | |\/| |  _ <|  __| |  _  / 
  ____) | |  | |____) | | |_) | |__| | |  | | |_) | |____| | \ \ 
 |_____/|_|  |_|_____/  |____/ \____/|_|  |_|____/|______|_|  \_\
                                                                                           
                  {}by {}@Lexer<3\n  
    """.format(Fore.LIGHTCYAN_EX, Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = (input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gonder\n 2- İletisim\n 3- cikis\n\n" + Fore.LIGHTYELLOW_EX + " Secim: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatali giris yaptin. Tekrar deneyiniz.")
        sleep(3)
        continue

    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasini basinda '+90' olmadan yaziniz (Birden coksa 'enter' tusuna basiniz): "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numaralarinin kayitli oldugu dosyanin dizinini yaziniz: "+ Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatali dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tusuna basiniz)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatali telefon numarasi. Tekrar deneyiniz.") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsaniz 'enter' tusuna basin): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatali mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kac adet SMS gondermek istiyorsun {sonsuz}: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere: # Made By Lexer
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatali giris yaptin. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kac saniye aralikla gondermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatali giris yaptin. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail) # Made by Lexer
            if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.adet == kere:
                                        break
                                    exec("sms."+attribute+"()")
                                    sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenuye donmek icin 'enter' tusuna basiniz..")
        input()

    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTWHITE_EX + "Discord: yildirimlord\nTelegram: yildirimlord")
        sleep(12)
    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "cikis yapiliyor...")
        break
