from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo
    b = ["""
'########:'##::::'##:'####:'##::: ##:
 ##.....:: ###::'###:. ##:: ###:: ##:
 ##::::::: ####'####:: ##:: ####: ##:
 ######::: ## ### ##:: ##:: ## ## ##:
 ##...:::: ##. #: ##:: ##:: ##. ####:
 ##::::::: ##:.:: ##:: ##:: ##:. ###:
 ########: ##:::: ##:'####: ##::. ##:
........::..:::::..::....::..::::..::
    """]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    #print('=============SON OF GENISYS==============')
    print(f'   Versiya: 1.2 | Müəllif: Emin{n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] Yeni hesablar əlavə edin'+n)
    print(lg+'[2] Bütün qadağan edilmiş hesabları süzün'+n)
    print(lg+'[3] Xüsusi hesabları silin'+n)
    print(lg+'[4] Yeniləməni yoxlayin'+n)
    print(lg+'[5] Çıx'+n)
    a = int(input('\nSeçiminizi daxil edin: '))
    if a == 1:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg} [~] Əlavə ediləcək hesabların sayını daxil edin: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg} [~] Telefon nömrəsini daxil edin: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [i] Bütün hesablar saxlanıldı vars.txt')
            clr()
            print(f'\n{lg} [*] Yeni hesablardan giriş\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                c.start(number)
                print(f'{lg}[+] Uğurlu giriş')
                c.disconnect()
            input(f'\n Əsas menyuya keçmək üçün enter düyməsini basın...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] Hesab yoxdur! Zəhmət olmasa bir az əlavə edin və yenidən cəhd edin')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{lg}[+] {phone} Qadağan edilmir{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' Qadağandır!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Təbriklər! Qadağan edilmiş hesab yoxdur')
                input('\nƏsas menyuya keçmək üçün enter düyməsini basın...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] Bütün qadağan edilmiş hesablar silindi'+n)
                input('\nƏsas menyuya keçmək üçün enter düyməsini basın...')

    elif a == 3:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[i] Silmək üçün bir hesab seçin\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Seçim daxil edin: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Hesab Silindi{n}')
        input(f'\nƏsas menyuya keçmək üçün enter düyməsini basın...')
        f.close()
    elif a == 4:
        # thanks to github.com/th3unkn0n for the snippet below
        print(f'\n{lg}[i] Yeniləmələr yoxlanılır...')
        try:
            # https://raw.githubusercontent.com/Cryptonian007/Astra/main/version.txt
            version = requests.get('https://raw.githubusercontent.com/emin4516/eminuye/main/version.txt')
        except:
            print(f'{r} İnternetə bağlı deyilsiniz')
            print(f'{r} Zəhmət olmasa internetə qoşulun və yenidən cəhd edin')
            exit()
        if float(version.text) > 1.1:
            prompt = str(input(f'{lg}[~] Yeniləmə mövcuddur[Versiya {version.text}]. Yüklənsin?[y/n]: {r}'))
            if prompt == 'y' or prompt == 'yes' or prompt == 'Y':
                print(f'{lg}[i] Yeniləmələr endirilir...')
                if os.name == 'nt':
                    os.system('del add.py')
                    os.system('del manager.py')
                else:
                    os.system('rm add.py')
                    os.system('rm manager.py')
                #os.system('del scraper.py')
                os.system('curl -l -O https://raw.githubusercontent.com/emin4516/eminuye/main/add.py')
                os.system('curl -l -O https://raw.githubusercontent.com/emin4516/eminuye/main/manager.py')
                print(f'{lg}[*] Updated to version: {version.text}')
                input('Çıxmaq üçün enter düyməsini basın...')
                exit()
            else:
                print(f'{lg}[!] Güncəlləmə ləğv edildi.')
                input('Əsas menyuya keçmək üçün enter düyməsini basın...')
        else:
            print(f'{lg}[i] Versiya artıq yenidir')
            input('Əsas menyuya keçmək üçün enter düyməsini basın...')
    elif a == 5:
        clr()
        banner()
        exit()
