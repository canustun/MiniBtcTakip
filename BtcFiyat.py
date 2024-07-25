#Telegram & instagram: @canustun_py
import tkinter as tk
import requests as r
import json

durum = 0
onceki = 0

pencere=tk.Tk()
pencere.title("Btc Fiyat")


def btc_deger():
    global onceki
    veri = r.get("https://api.kucoin.com/api/v1/market/stats?symbol=BTC-USDT").text
    fiyat["text"] = json.loads(veri)["data"]["buy"]
    if onceki == 0:
        pass
    elif float(fiyat.cget("text")) < onceki:
        fiyat["fg"] = "red"
    elif float(fiyat.cget("text")) > onceki:
        fiyat["fg"] = "green"
        
    onceki = float(fiyat.cget("text"))
    pencere.after(2000,btc_deger)

def tik():
    global durum
    durum = not durum
    pencere.attributes('-toolwindow', durum)
    pencere.overrideredirect(durum)
    pencere.wm_attributes("-topmost", durum)
    pencere.geometry("80x20")

tik()
fiyat = tk.Button(pencere, font = ("Consolas",15),fg = "gray",command = tik)

btc_deger()
fiyat.pack()
fiyat.mainloop()

