import speech_recognition
import os
import random
import customtkinter
import playsound
import webbrowser
import platform
import win10toast
import win11toast
from translate import Translator
import requests
import pyautogui
import threading

if not (requests.get('http://ya.ru').ok):
    print('Извините, но Кира не любит оставаться в стороне от сети интернет')
    raise Exception

Version = 0

INOES = []
MUSS = []
PROGS = []

numbi = {
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
    'десять': 10,
    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятьнадцать': 15,
    'шестьнадцать': 16,
    'семьнадцать': 17,
    'восемьнадцать': 18,
    'девятьнадцать': 19,
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90,
    'сто': 100,
}

if platform.win32_ver()[0] == '10':
    Version = 10
if platform.win32_ver()[0] == '11':
    Version = 11

if os.name != 'nt':
    print('Извините, но Кира наиболее предпочитает ОС Windows')
    raise Exception
############################################################################################

'''A=[['rtf kpk','hfy hfj'],['lkj ytr lkm']]
if 'rtf' in A[0][0]:
    print(1)
else:
    print(0)'''

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
try:
    relationship = open('Kira/Saves/relationship.txt', mode='r')
    relationship = relationship.read()
except:
    print('')
try:
    INOE = open('Kira/Saves/inoe.txt', mode='r', encoding='utf8')
    INOE = INOE.readlines()
    for i in INOE:
        INOET = i.split(',')
        INOES.append(INOET)
    for i in range(len(INOES) - 1):
        if '\n' in INOES[i][2]:
            INOES[i][2] = INOES[i][2].replace('\n', '')

except:
    print('')
try:
    MUS = open('Kira/Saves/music.txt', mode='r', encoding='utf8')
    MUS = MUS.readlines()
    for i in MUS:
        MUST = i.split(',')
        MUSS.append(MUST)
        for i in range(len(MUSS) - 1):
            if '\n' in MUSS[i][2]:
                MUSS[i][2] = MUSS[i][2].replace('\n', '')

except:
    print('')

try:
    PROG = open('Kira/Saves/programs.txt', mode='r', encoding='utf8')
    PROG = PROG.readlines()
    for i in PROG:
        PROGT = i.split(',')
        PROGS.append(PROGT)
        for i in range(len(PROGS) - 1):
            if '\n' in PROGS[i][2]:
                PROGS[i][2] = PROGS[i][2].replace('\n', '')

except:
    print('')
kira = ['kia', 'kira', 'кира', 'киа', 'ira', 'ира', 'терра', 'hero', 'тира', 'киров', '_']
vkl = ['включи', 'запусти', 'проиграй', 'открой', '_', '_', '_', '_', '_']
mus = ['музыку', 'плейлист', 'плейлисты', '_', '_', '_', '_']
olleh = ['привет', 'здравствуй', '_', '_', '_', '_', '_', '_']
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


############################################################################################

def toast(glav, message, durat):
    if Version == 10:
        toas = win10toast.ToastNotifier()
        toas.show_toast(title=glav, msg=message, duration=durat)
    if Version == 11:
        win11toast.toast(message)


'''def button_function_prog():
    information1 = entryyy1.get()
    information2 = entryyy2.get()
    information3 = entryyy3.get()
    print(information1,information2,information3)
    information3 = information3.split(',')
    information3 = ' '.join(information3)
    information = information1 + ',' + information2 + ',' + information3
    print(information)
    infor = PROGS
    if len(infor)>0:
        infor.pop(int(information1)-1)
    infor.insert(int(information1) - 1,information)
    print(infor)
    file = open('Kira/Saves/programs.txt', mode='w')
    for i in infor:
        i=''.join(i)
        file.write(i)
        file.write('\n')
    file.close()
    app.destroy()

def inoebut():
    try:
        global entry1
        global entry2
        global entry3
        global appp
        appp = customtkinter.CTk()
        appp.geometry("1024x512")
        appp.title("Настройки прочего")
        appp.resizable(False, False)
        textbox1 = customtkinter.CTkTextbox(master=appp, width=800, height=40, corner_radius=0)
        textbox1.pack(pady=30, padx=20)
        textbox1.insert("0.0","Введите номер ячейки, путь до файла(с расшерением) и через запятую названия с которым к нему можно обратиться.\nПример: 2 C:/Users/Kirill/txt/lmao.txt lmao,лмао,смех,ту самую штуку")
        entry1 = customtkinter.CTkEntry(master=appp, width=58, height=30, placeholder_text="Ячейка")
        entry1.place(relx=0.1, rely=0.4, anchor=customtkinter.CENTER)
        entry2 = customtkinter.CTkEntry(master=appp, width=370, height=30, placeholder_text="Путь(с расширением)")
        entry2.place(relx=0.35, rely=0.4, anchor=customtkinter.CENTER)
        entry3 = customtkinter.CTkEntry(master=appp, width=370, height=30, placeholder_text="Имена")
        entry3.place(relx=0.75, rely=0.4, anchor=customtkinter.CENTER)
        button = customtkinter.CTkButton(master=appp, width=200, height=30, text="Сохранить прочее",command=button_function_ino)
        button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        appp.mainloop()
    except Exception:
        print('')


def musicbut():
    try:
        global entryy1
        global entryy2
        global entryy3
        global appp
        appp = customtkinter.CTk()
        appp.geometry("1024x512")
        appp.title("Настройки музыки")
        appp.resizable(False, False)
        textbox1 = customtkinter.CTkTextbox(master=appp, width=800, height=40, corner_radius=0)
        textbox1.pack(pady=30, padx=20)
        textbox1.insert("0.0","Введите номер ячейки, путь до файла(с расшерением) и через запятую названия с которым к нему можно обратиться.\nПример: 2 C:/Users/Kirill/music/music.zpl classic,классика,для расслабона,моцарт")
        entryy1 = customtkinter.CTkEntry(master=appp, width=58, height=30, placeholder_text="Ячейка")
        entryy1.place(relx=0.1, rely=0.4, anchor=customtkinter.CENTER)
        entryy2 = customtkinter.CTkEntry(master=appp, width=370, height=30, placeholder_text="Путь(с расширением)")
        entryy2.place(relx=0.35, rely=0.4, anchor=customtkinter.CENTER)
        entryy3 = customtkinter.CTkEntry(master=appp, width=370, height=30, placeholder_text="Имена")
        entryy3.place(relx=0.75, rely=0.4, anchor=customtkinter.CENTER)
        button = customtkinter.CTkButton(master=appp, width=200, height=30, text="Сохранить плейлист",command=button_function_mus)
        button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        appp.mainloop()
    except Exception:
        print('')


def programmbut():
    try:
        global entryyy1
        global entryyy2
        global entryyy3
        global appp
        appp = customtkinter.CTk()
        appp.geometry("1024x512")
        appp.title("Настройки программ")
        appp.resizable(False, False)
        textbox1 = customtkinter.CTkTextbox(master=appp, width=800, height=40, corner_radius=0)
        textbox1.pack(pady=30, padx=20)
        textbox1.insert("0.0","Введите номер ячейки, путь до файла(с расшерением) и через запятую названия с которым к нему можно обратиться.\nПример: 2 C:/Users/Kirill/games/amongus.exe amongus,амонгас,амогус,амогуса")
        entryyy1 = customtkinter.CTkEntry(master=appp, width=58, height=30, placeholder_text="Ячейка")
        entryyy1.place(relx=0.1, rely=0.4, anchor=customtkinter.CENTER)
        entryyy2 = customtkinter.CTkEntry(master=appp, width=370, height=30, placeholder_text="Путь(с расширением)")
        entryyy2.place(relx=0.35, rely=0.4, anchor=customtkinter.CENTER)
        entryyy3 = customtkinter.CTkEntry(master=appp, width=370, height=30, placeholder_text="Имена")
        entryyy3.place(relx=0.75, rely=0.4, anchor=customtkinter.CENTER)
        button = customtkinter.CTkButton(master=appp, width=200, height=30, text="Сохранить программу",command=button_function_prog)
        button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        appp.mainloop()
    except Exception:
        print('')'''


def otv():
    ran = random.randint(0, 4)
    if ran == 0:
        playsound.playsound('Kira/Sounds/otv1.mp3')
    if ran == 1:
        playsound.playsound('Kira/Sounds/otv2.mp3')
    if ran == 2:
        playsound.playsound('Kira/Sounds/otv3.mp3')
    if ran == 3:
        playsound.playsound('Kira/Sounds/otv4.mp3')


def Find(x, y):
    for i in x:
        if i in y:
            return True
    else:
        return False


def FindW(x, y):
    for i in range(len(y) - 1):
        if x in y[i][2]:
            return i


def wtn(h):
    sumn = 0
    for i in h:
        if i in numbi:
            sumn += numbi[i]
    if sumn != 0:
        return sumn
    else:
        return '-2t56'


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def hello():
    return playsound.playsound('Kira/Sounds/privet.mp3')


def listen():
    global djaga
    djaga = 1
    while True:
        a = listen_command()
        if a == 'стоп':
            break
    djaga = 0


############################################################################################

'''def mineworld():
    os.system('C:/Users/Кирилл/Documents/Kira/Mineworld/MineWorld.bat')
    os.system('G:/Pictures/ABlueStacks/.minecraft/TLauncher.exe')'''


def stepik():
    threading.Thread(target=otv).start()
    webbrowser.open('https://stepik.org', new=2)


def autoclicker(jaka):
    # 1 - пкм
    # 2 - лкм
    # t(тиках) - скорость
    global djaga
    ind31 = jaka.index('на')
    mode = jaka[ind31 - 1]
    speed = jaka[ind31 + 1]
    if mode == 'лкм':
        playsound.playsound('Kira/Sounds/stop.mp3')
        print("скажите стоп чтобы остановить")
        b, c = pyautogui.position()
        print("Начальная позиция курсора:", b, c)
        djaga = threading.Thread(target=listen).start()
        while djaga != 0:
            pyautogui.PAUSE = int(speed) / 40
            pyautogui.leftClick()
    if mode == 'пкм':
        playsound.playsound('Kira/Sounds/stop.mp3')
        print("скажите стоп чтобы остановить")
        b, c = pyautogui.position()
        print("Начальная позиция курсора:", b, c)
        djaga = threading.Thread(target=listen).start()
        while djaga != 0:
            pyautogui.PAUSE = int(speed) / 40
            pyautogui.rightClick()


def luckygame():
    chisel = random.randint(1, 101)
    playsound.playsound('Kira/Sounds/kone.mp3')
    playsound.playsound('Kira/Sounds/vibor.mp3')
    while True:
        chisol = listen_command()
        if chisol == 'не распознано :/':
            continue
        if chisol == 'выход':
            break
        if 'число' in chisol:
            chisol = chisol.replace('число', '', 1)
        if 'цифра' in chisol:
            chisol = chisol.replace('цифра', '', 1)
        if is_number(chisol):
            chisol = int(chisol)
            if chisol == chisel:
                playsound.playsound('Kira/Sounds/ugad.mp3')
                break
            if chisol > chisel:
                playsound.playsound('Kira/Sounds/men.mp3')
            if chisol < chisel:
                playsound.playsound('Kira/Sounds/bol.mp3')
        else:
            chisol = wtn(chisol.split())
            if chisol == '-2t56':
                playsound.playsound('Kira/Sounds/osh.mp3')
                playsound.playsound('Kira/Sounds/kone.mp3')
            elif chisol == chisel:
                playsound.playsound('Kira/Sounds/ugad.mp3')
                break
            elif chisol > chisel:
                playsound.playsound('Kira/Sounds/men.mp3')
            elif chisol < chisel:
                playsound.playsound('Kira/Sounds/bol.mp3')


def googling(zapros):
    threading.Thread(target=otv).start()
    webbrowser.open('www.google.ru/search?q={}'.format(str(zapros)), new=2)


def ytgoogling(zapros):
    threading.Thread(target=otv).start()
    webbrowser.open('https://www.youtube.com/results?search_query={}'.format(str(zapros)), new=2)


def yout():
    threading.Thread(target=otv).start()
    if Find(qwer, 'shorts') or Find(qwer, 'шортс') or Find(qwer, 'шортсы') or Find(qwer, 'шорты'):
        webbrowser.open('https://www.youtube.com/shorts', new=2)
    else:
        webbrowser.open('https://youtube.com', new=2)


def trans(text):
    threading.Thread(target=otv).start()
    ind21 = 0
    ind22 = 0
    for x in qwer:
        if 'рус' in x:
            ind21 = qwer.index(x)
            break
    for x in qwer:
        if 'англ' in x:
            ind22 = qwer.index(x)
            break
    if ind21 > ind22:
        translate = Translator(from_lang="en", to_lang="ru")
        trana = translate.translate(text)
        toast('Переводчик', trana, 5)

    if ind22 > ind21:
        translate = Translator(from_lang="ru", to_lang="en")
        trana = translate.translate(text)
        toast('Переводчик', trana, 5)


def music(mus):
    threading.Thread(target=otv).start()
    musi = FindW(mus, MUSS)
    pathmus = MUSS[musi][1]
    os.system(f'{pathmus}')


def program(prog):
    threading.Thread(target=otv).start()
    progi = FindW(prog, PROGS)
    pathprog = PROGS[progi][1]
    os.system(f'{pathprog}')


def inoe(ino):
    threading.Thread(target=otv).start()
    inoi = FindW(ino, INOES)
    pathino = INOES[inoi][1]
    os.system(f'{pathino}')


'''def prop():
    try:
        global entry
        global app
        app = customtkinter.CTk()
        app.geometry("400x280")
        app.title("Настройки")
        app.resizable(False, False)
        textbox1 = customtkinter.CTkTextbox(master=app, width=400, height=20, corner_radius=0)
        textbox1.pack(pady=20, padx=20)
        textbox1.insert("0.0", "Выберите категорию которую хотите изменить.")
        buttonnn = customtkinter.CTkButton(master=app, text="Программы", command=programmbut)
        buttonnn.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
        buttonn = customtkinter.CTkButton(master=app, text="Музыка", command=musicbut)
        buttonn.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
        button = customtkinter.CTkButton(master=app, text="Прочее", command=inoebut)
        button.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
        app.mainloop()
    except Exception:
        print('')'''


############################################################################################

def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            print('/////', query)
        return query
    except speech_recognition.UnknownValueError:
        return 'не распознано :/'


############################################################################################

def main():
    Flag1112=0
    twer = ''

    while 'пожалуйста' in qwer:
        ind1 = qwer.index('пожалуйста')
        qwer.pop(ind1)

    if Find(qwer, olleh):
        hello()
        Flag1112=1

    elif 'найди' in qwer and 'видео' in qwer:
        ind11 = qwer.index('найди')
        ind12 = qwer.index('видео')
        if ind11 + 1 == ind12:
            if 'про' in qwer:
                ind = qwer.index('про')
                twer = qwer[ind - 1:]
            else:
                ind = qwer.index('видео')
                twer = qwer[ind + 1:]
            twer = ' '.join(twer)
            ytgoogling(twer)
        Flag1112=1

    elif 'найди' in qwer or 'запрос' in qwer:
        if 'видео' in qwer:
            ind11 = qwer.index('найди')
            ind12 = qwer.index('видео')
            if ind11 + 1 != ind12:
                if 'найди' in qwer:
                    ind = qwer.index('найди')
                    twer = qwer[ind + 1:]
                if 'запрос' in qwer:
                    ind = qwer.index('запрос')
                    twer = qwer[ind + 1:]
                twer = ' '.join(twer)
                googling(twer)
        else:
            if 'найди' in qwer:
                ind = qwer.index('найди')
                twer = qwer[ind + 1:]
            if 'запрос' in qwer:
                ind = qwer.index('запрос')
                twer = qwer[ind + 1:]
            twer = ' '.join(twer)
            googling(twer)
        Flag1112=1

    if Find(qwer, mus):
        try:
            if 'плейлист' in qwer or 'плейлисты' in qwer or 'музыку' in qwer:
                qwr = qwer
                if 'плейлист' in qwr:
                    ind51 = qwr.index('плейлист')
                    qwr = qwr[ind51 + 1:]
                if 'плейлисты' in qwr:
                    ind51 = qwr.index('плейлисты')
                    qwr = qwr[ind51 + 1:]
                if 'музыку' in qwr:
                    ind51 = qwr.index('музыку')
                    qwr = qwr[ind51 + 1:]
                qwr = ' '.join(qwr)
                music(qwr)
        except:
            print('нет плейлиста')

    elif Find(qwer, vkl):
        try:
            if 'stepik' in qwer or 'степик' in qwer or 'стэпик' in qwer:
                stepik()
            '''if 'настройки' in qwer:
                prop()'''
            Flag113 = 0
            Flag112 = 0
            qwr = qwer
            if 'файл' in qwr and 'открой' in qwr:
                if qwr.index('открой') == qwr.index('файл') - 1:
                    ind61 = qwr.index('файл')
                    qwr = qwr[ind61 + 1:]
                    qwr = ' '.join(qwr)
                    inoe(qwr)
                    Flag113 = 1
            if Flag113 == 0:
                for i in vkl:
                    if i in qwr:
                        ind62 = qwr.index(i)
                        qwr = qwr[ind62 + 1:]
                qwr = ' '.join(qwr)
                program(qwr)
        except:
            print('элемент не найден')

        if 'youtube' in qwer or 'ютуб' in qwer or 'ютуба' in qwer:
            yout()

    elif 'переведи' in qwer:
        ind31 = 0
        ind32 = 0
        for x in qwer:
            if 'англ' in x:
                ind31 = qwer.index(x)
                break
        for x in qwer:
            if 'рус' in x:
                ind32 = qwer.index(x)
                break
        if ind31 != 0 and ind32 != 0:
            if ind31 > ind32:
                tex = qwer[ind31 + 1:]
                tex = ' '.join(tex)
                trans(tex)
            elif ind32 > ind31:
                tex = qwer[ind32 + 1:]
                tex = ' '.join(tex)
                trans(tex)

    elif 'подкинь' in qwer and ('монетку' in qwer or 'монету' in qwer):
        coin = random.randint(0, 2)
        if coin == 0:
            playsound.playsound('Kira/Sounds/orel.mp3')
        if coin == 1:
            playsound.playsound('Kira/Sounds/reshka.mp3')

    elif ('игру' in qwer or 'игра' in qwer) and 'удачу' in qwer:
        luckygame()

    elif 'автокликер' in qwer and 'на' in qwer:
        autoclicker(qwer)

    else:
        if Flag1112 == 0:
            playsound.playsound('Kira/Sounds/izvin.mp3')


############################################################################################

try:
    while True:
        quer = listen_command()
        qwer = quer.split()

        if Find(qwer, kira):
            if __name__ == '__main__':
                print('')
                main()
        else:
            print('.')
            continue
except:
    print('Ошибка')

############################################################################################
