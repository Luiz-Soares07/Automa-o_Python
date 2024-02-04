import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")


link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=690, y=512)
pyautogui.write("abc@gmail.com")

pyautogui.press("tab")
pyautogui.write("ntvuotnua")

pyautogui.press("tab")
pyautogui.press("enter")   

time.sleep(2)

import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
  pyautogui.click(x=719, y=363)
  codigo = tabela.loc[linha, "codigo"]
  pyautogui.write(str(codigo))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha,"marca"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha,"tipo"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha,"categoria"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha,"custo"]))
  pyautogui.press("tab")
  obs = tabela.loc[linha,"obs"]
  if not pd.isna(obs):
    pyautogui.write(obs)
  pyautogui.doubleClick(x=854, y=692)
  pyautogui.scroll(5000)



