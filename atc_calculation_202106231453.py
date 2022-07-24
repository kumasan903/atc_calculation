import tkinter as tk

# ボタンを押したときの処理 --- (*1)
def calc_time():
    # かかる時間を計算
    spd = float(apchSpeed.get())
    nm = float(finalnm.get())
    time = round(nm / spd * 60,1) #時間の計算式(分)
    # 結果をラベルに表示
    s = "滑走路端到達までの予想時間：" + str(time) + "分"
    labelResult['text'] = s

# ウィンドウを作成 --- (*2)
win = tk.Tk()
win.title("到着時間予測")
win.geometry("500x250")

# 部品を作成 --- (*3)
labelHeight = tk.Label(win, text=u'速度(kt)')
labelHeight.pack()

apchSpeed = tk.Entry(win)
apchSpeed.insert(tk.END, '160')
apchSpeed.pack()

labelWeight = tk.Label(win, text=u'距離(nm)')
labelWeight.pack()

finalnm = tk.Entry(win)
finalnm.insert(tk.END, '15')
finalnm.pack()

labelResult = tk.Label(win, text=u'---')
labelResult.pack()

calcButton = tk.Button(win, text=u'計算')
calcButton["command"] = calc_time
calcButton.pack()

# ウィンドウを動かす
win.mainloop()