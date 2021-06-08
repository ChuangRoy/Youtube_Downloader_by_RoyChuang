import GUI
import download
import Check_URL
import threading
import tkinter as tk
from tkinter import messagebox, ttk
import time

# threading.active_count() #查看thread總數量
# threading.enumerate() #列出所有thread name
# threading.current_thread() #查看目前進入哪個thread

class main(GUI.Window):
    def __init__(self):
        super().__init__()
        print("Started!")
    def click(self):
        # Check URL
        self.url = str(self.input_url.get())
        url = self.url
        URL_Exist=Check_URL.Check_Url(url)
        if URL_Exist == True:
            # 詢問是否下載播放清單
            dlplaylist=self.download_ask()
            if dlplaylist == "yes":
                self.insert_text("")
                self.insert_text(f'下載{url}')
                download.download(url,True)
                self.insert_text(f'{url}下載完畢')
                print("")
                print(f'{url}下載完畢')
                print(
                    "=====================================================================================")
            else:
                self.insert_text(f'下載{self.input_url.get()}')
                download.download(url,False)
                main.insert_text(f'{url}下載完畢')
                print("")
                print(f'{url}下載完畢')
                print(
                    "=====================================================================================")
        else:
            print("請檢察網址是否正確或網路連線是否正常")
            GUI.Window.no_url(1)


def mainloop():
    while True :
        Main.window.update()
        Main.window.update_idletasks()
        time.sleep(0.01)

Main = main()
try:
    threading.Thread(target=mainloop())
except:
    raise
