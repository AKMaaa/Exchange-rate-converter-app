import tkinter as tk
from currency_converter import CurrencyConverter
import csv


# 関数を書く場所 --- (*1)
def calc_rate():
    # 為替
    c = CurrencyConverter()
    header = ['country', 'rate']
    jp_y=float(textHeight.get())
    usd_m = "{:.03}".format(c.convert(jp_y, 'JPY', 'USD'))
    cnd_m = "{:.03}".format(c.convert(jp_y, 'JPY', 'CAD'))
    inr_m = "{:.03}".format(c.convert(jp_y, 'JPY', 'INR'))
    thb_m = "{:.03}".format(c.convert(jp_y, 'JPY', 'THB'))
    aed_m = "{:.03}".format(jp_y*0.03)
    sek_m = "{:.03}".format(c.convert(jp_y, 'JPY', 'SEK'))
    myr_m = "{:.03}".format(c.convert(jp_y, 'JPY', 'MYR'))
    egp_m = "{:.03}".format(jp_y*0.14)
    xeu_m = "{:.03}".format(jp_y*0.01)
    aud_m = "{:.03}".format(c.convert(jp_y, 'JPY', 'AUD'))
    brl_m = "{:.03}".format(c.convert(jp_y, 'JPY', 'BRL'))
    krw_m = "{:.05}".format(c.convert(jp_y, 'JPY', 'KRW'))
    sar_m = "{:.03}".format(jp_y*0.03)
    body = [
        ['usd',usd_m],
        ['cad',cnd_m],
        ['inr',inr_m],
        ['thb',thb_m],
        ['aed',aed_m],
        ['sek',sek_m],
        ['myr',myr_m],
        ['egp',egp_m],
        ['xeu',xeu_m],
        ['aud',aud_m],
        ['brl',brl_m],
        ['krw',krw_m],
        ['sar',sar_m],
        ]
    with open('rate.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(body)
    f.close()
    labelResult['text'] = "csvファイルを保存しました"

# ウィンドウを作成 --- (*2)
win = tk.Tk()
win.title("レート表示")
win.geometry("500x100")

# 部品を作成 --- (*3)

labelHeight = tk.Label(win, text='日本円を入力')
labelHeight.pack()

textHeight = tk.Entry(win)
textHeight.insert(tk.END, '160')
textHeight.pack()

labelResult = tk.Label(win, text='---')
labelResult.pack()

calcButton = tk.Button(win, text='計算')
calcButton["command"] = calc_rate
calcButton.pack()

# ウィンドウを動かす
win.mainloop()