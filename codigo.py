import pyautogui
import pandas as pd
import time

time.sleep(5)
# passo a passo

# deixando lento!
#pyautogui.PAUSE = 0.6

# entrar no navegador

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(6)
#pyautogui.hotkey("alt", "x", "space")

pyautogui.click(x=324, y=52)
pyautogui.press("backspace", presses=100)

# entrar no site da empresa
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(4)

# login

pyautogui.click(x=806, y=391)
pyautogui.write("testaai@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhaqualquer")
pyautogui.press("enter")
time.sleep(4)

# importar base de dados!

base = pd.read_csv("produtos.csv")

# cadastrar um produto
for linha in base.index:
    pyautogui.click(x=778, y=271)

    # ['codigo', 'marca', 'tipo', 'categoria', 'preco_unitario', 'custo', 'obs']

    # codigo
    pyautogui.write(base.loc[linha, 'codigo'])
    pyautogui.press("tab")

    # marca  
    pyautogui.write(base.loc[linha, 'marca'])
    pyautogui.press("tab")

    # tipo
    pyautogui.write(base.loc[linha, 'tipo'])
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(base.loc[linha, 'categoria']))
    pyautogui.press("tab")

    # preco_unitario
    pyautogui.write(str(base.loc[linha, 'preco_unitario']))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(base.loc[linha, 'custo']))
    pyautogui.press("tab")

    # obs
    obs = base.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)


# repitir para todos os produtos
