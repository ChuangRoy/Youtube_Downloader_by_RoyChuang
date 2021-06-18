import GUI
import download
import Check_URL
import threading
# import subprocess as sp


# threading.active_count() #查看thread總數量
# threading.enumerate() #列出所有thread name
# threading.current_thread() #查看目前進入哪個thread
# Ref:https://medium.com/@jennifer840719/python-tkinter-%E6%B2%92%E6%9C%89%E5%9B%9E%E6%87%89-814f5144488d
# ---------------------
# import threading
# class Threader(threading.Thread):
# def __init__(self, *args, **kwargs):

#         threading.Thread.__init__(self, *args, **kwargs)
#         self.daemon = True
#         self.start()
# def run(self):
#         .............. #要執行的task
# ----------------------

class main(GUI.Window):
    def __init__(self):
        super().__init__()
        print("Started!")
        super().mainloop()

    def click(self):
        threading.Thread(target = main.download_video())
        
    def download_video(self):
        # Check URL
        self.url = str(self.input_url.get())
        url = self.url
        URL_Exist = Check_URL.Check_Url(url)
        if URL_Exist == True:
            # 詢問是否下載播放清單
            dlplaylist = self.download_ask()
            self.insert_text("")
            self.insert_text(f'下載{url}')
            threading.Thread(download.download(url, dlplaylist == "yes"))
            self.insert_text(f'{url}下載完畢')
            print("")
            print(f'{url}下載完畢')
            print(
                "=====================================================================================")
        else:
            print("請檢察網址是否正確或網路連線是否正常")
            GUI.Window.no_url()


# class Threader(threading.Thread):
#     def __init__(self, Main, *args, **kwargs):

#             threading.Thread.__init__(self, *args, **kwargs)
#             self.daemon = True
#             self.start()
#     def run(self):
#             self.Main = Main
#         while True :
#             # self.Main.window.update()
#             # self.Main.window.update_idletasks()
#             # time.sleep(0.01)
#             self.Main.window.mainloop()
Main = main()


# threading.Thread(target=Threader(Main))
