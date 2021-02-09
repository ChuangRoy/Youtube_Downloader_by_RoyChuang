import tkinter as tk
from tkinter import messagebox, ttk

class Window():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Python YouTube Video Downloader 影片下載器")
        self.window.geometry("500x600")
        self.window.resizable(0, 0)
        self.window.wm_attributes("-topmost", 1)
        # self.window.iconbitmap("YouTube_Icon_1.ico") # 更改圖示
        print("製作人:莊鎮宇 s041516@apps.ntpc.edu.tw")
        print("This is a python console這是一個Python主視窗")
        print("You can see all message here 你可以在這看到所有訊息")
        print("Please Don't close this window 請勿關閉此視窗")
        print("=====================================================================================")
        # 顯示YouTube圖片
        self.Icon1 = tk.PhotoImage(file = "YouTube_Icon_1.png")
        self.Image_Lable1 = tk.Label(self.window,image = self.Icon1)
        self.Image_Lable1.pack()
        # 設定網址輸入區域
        self.input_frm = tk.Frame(self.window, width=640, height=50)
        self.input_frm.pack()
        # 設定提示文字
        self.l1 = tk.Label(self.window, text="type URL here", font="none 12 bold")
        self.l1.pack()
        # 設定輸入框
        self.input_url = tk.StringVar()  # 取得輸入的網址
        self.input_et = tk.Entry(self.input_frm, textvariable=self.input_url, width=60)
        self.input_et.place(rely=0.75, relx=0.5, anchor='center')
        # 設定按鈕
        self.btn = tk.Button(self.input_frm, text='Download', command=self.click,
                        bg='orange', fg='Black')
        self.btn.place(rely=0.75, relx=0.9, anchor='center')

        self.choice_frm = tk.Frame(self.window, width=640, height=50)
        self.choice_frm.pack()

        self.lb = tk.Label(self.choice_frm, text='Quality品質 :',
                    fg='black')
        self.lb.place(rely=0.2, relx=0.1)
        self.cbb = ttk.Combobox(self.choice_frm,
                    values=[
                        "720p",
                        "480p",
                        "360p"], state="readonly", width=12)

        self.cbb.place(rely=0.2, relx=0.3)
        self.cbb.current(0)

        self.cbb.bind("<<ComboboxSelected>>", self.callbackFunc)

        self.dl_frm = tk.Frame(self.window, width=640, height=280)
        self.dl_frm.pack()

        self.lb = tk.Label(self.dl_frm, text='Download Message', font="none 12 bold")
        self.lb.place(rely=0.1, relx=0.5, anchor='center')

        self.listbox = tk.Listbox(self.dl_frm, width=65, height=15)
        self.listbox.place(rely=0.6, relx=0.5, anchor='center')
        self.sbar = tk.Scrollbar(self.dl_frm)
        self.sbar.place(rely=0.6, relx=0.87, anchor='center', relheight=0.75)
        self.listbox.config(yscrollcommand=self.sbar.set)

        # l1 = tk.Label(window, text="Made by Roy Chuang ！ s041516@apps.ntpc.edu.tw",  font="none 12 bold")
        # l1.pack()
        self.listbox.insert(tk.END, '製作人:莊鎮宇 ！ s041516@apps.ntpc.edu.tw')
        self.listbox.insert(tk.END, '開發工具:Python,Pyinstaller')
        self.listbox.insert(tk.END, '開發模組:Pytube,tkinter,threading')
        self.listbox.insert(tk.END, '新功能:同時下載多個影片檔')
        self.listbox.insert(tk.END, '注意:影片下載完成前，可能產生不完整(下載到一半)影片檔，請勿開啟')
        self.listbox.insert(tk.END, '注意:如中途網路中斷或關閉程式可能殘留未完成影片檔，將其刪除即可')
        self.listbox.insert(tk.END, '即將推出下載播放清單功能，敬請期待')
        self.listbox.insert(tk.END, '----------------------------------------------------------------------------------')


    def callbackFunc(self, event):
        listbox.insert(tk.END, 'Selected' + cbb.get())
    
    def click(self):
        print("下載影片")

    def mainloop(self):
        self.window.mainloop()

def main():
    gui = Window()
    gui.mainloop()

if __name__ == "__main__":
    main()