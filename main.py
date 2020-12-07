# ajustar resolução da tela para 1920x1080 e colocar  o navegador maximizado no canto esquerdo
# Caso utilize outro navegador mude o nome para o seu respectivo nome na variável nome_janela
# Antes de rodar o bot, utilize a janela output para alinhar a Região de interesse ( ROI ) um pouco acima dos botões
# Isso irá influenciar diretamente na qualidade do bot
# Caso queia utilizar o bot em outras resoluções, será necessário realizar a região de interesse, você pode fazer isso
# Tirando um screenshot da aba com o guitar flash aberto e encontrando os pixels iniciais e finais

import numpy as np
import cv2 as cv
import win32gui
import time
from PIL import ImageGrab, Image
from pynput.keyboard import Key, Controller
import threading

nome_janela = 'mozilla firefox'

x0=275
x1=650

y0=470
y1=520

toplist, winlist = [], []

def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
win32gui.EnumWindows(enum_cb, toplist)

window = [(hwnd, title) for hwnd, title in winlist if nome_janela in title.lower()]

def key_press(button):
    keyboard.press(button)
    time.sleep(0.08)
    keyboard.release(button)
try:
    window = window[0]
    hwnd = window[0]
except:
    print ("Janela Não Encontrada")
    exit(0)

win32gui.SetForegroundWindow(hwnd)
keyboard = Controller()

while True:

    bbox = win32gui.GetWindowRect(hwnd)
    screenshot_game = ImageGrab.grab(bbox)
    screenshot_game = np.array(screenshot_game)
    screenshot_game = screenshot_game[:, :, ::-1].copy()
    gray = cv.cvtColor(screenshot_game, cv.COLOR_BGR2GRAY)
    ret, thresh1 = cv.threshold(gray, 180, 255, cv.THRESH_BINARY)
    binary = thresh1[y0:y1,x0:x1]

    pad1 = binary[0:30,0:50]
    pad2 = binary[0:30,70:110]
    pad3 = binary[0:30,130:210]
    pad4 = binary[0:30,230:280]
    pad5 = binary[0:30,300:345]

    if (cv.countNonZero(pad1)>40):
        t = threading.Thread(target=key_press, args=("a",))
        t.start()
    if (cv.countNonZero(pad2)>40):
        t = threading.Thread(target=key_press, args=("s",))
        t.start()

    if (cv.countNonZero(pad3)>40):
        t = threading.Thread(target=key_press, args=("j",))
        t.start()

    if (cv.countNonZero(pad4)>40):
        t = threading.Thread(target=key_press, args=("k",))
        t.start()

    if (cv.countNonZero(pad5)>40):
        t = threading.Thread(target=key_press, args=("l",))
        t.start()
    cv.imshow("output", binary)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

