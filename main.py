# ajustar resolução da tela para 1920x1080 e colocar  o navegador maximizado no canto esquerdo
# Caso utilize outro navegador mude o nome para o seu respectivo nome na variável nome_janela
# Antes de rodar o bot, utilize a janela output para alinhar a Região de interesse ( ROI ) um pouco acima dos botões
# Isso irá influenciar diretamente na qualidade do bot
# Caso queia utilizar o bot em outras resoluções, será necessário realizar a região de interesse, você pode fazer isso
# Tirando um screenshot da aba com o guitar flash aberto e encontrando os pixels iniciais e finais

import numpy as np
import cv2 as cv
import win32gui
from PIL import ImageGrab, Image
from pynput.keyboard import Key, Controller

nome_janela = 'mozilla firefox'

x0=275
x1=600

y0=470
y1=520

b1 = True
b2 = True
b3 = True
b4 = True
b5 = True
toplist, winlist = [], []

def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
win32gui.EnumWindows(enum_cb, toplist)

window = [(hwnd, title) for hwnd, title in winlist if nome_janela in title.lower()]

def key_press(button, press):
    if (press):
        keyboard.press(button)
    else:
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
    gray_cutted = gray[y0:y1,x0:x1]
    ret, thresh1 = cv.threshold(gray_cutted,160, 255, cv.THRESH_BINARY)

    pad1 = thresh1[0:30,0:40]
    pad2 = thresh1[0:30,80:120]
    pad3 = thresh1[0:30,130:210]
    pad4 = thresh1[0:30,230:280]
    pad5 = thresh1[0:30,295:330]

    if (cv.countNonZero(pad1)>40):
        key_press("a", True)
    else:
        key_press("a", False)
    if (cv.countNonZero(pad2)>40):
        key_press("s", True)
    else:
        key_press("s", False)
    if (cv.countNonZero(pad3)>40):
        key_press("j", True)
    else:
        key_press("j", False)
    if (cv.countNonZero(pad4)>40):
        key_press("k", True)
    else:
        key_press("k", False)
    if (cv.countNonZero(pad5)>40):
        key_press("l", True)
    else:
        key_press("l", False)

    #cv.imshow("output", thresh1)
    #time.sleep(0.02)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

