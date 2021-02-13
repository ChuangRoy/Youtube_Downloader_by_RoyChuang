import GUI
import download
import Check_URL
import threading
import tkinter as tk
from tkinter import messagebox, ttk

class main(GUI.Window):
    def __init__(self):
        print("Started!")
        threading.Thread(target=super().__init__()).start()
    def click(self):
        URL_Exist = Check_URL.Check_Url(str(self.input_url.get()))
        if URL_Exist == True:
            playlist = self.download()
            if playlist == "yes":
                self.insert_text(f'下載{self.input_url.get()}' )
                threading.Thread(target=download.download(str(self.input_url.get()),True)).start()
                self.insert_text('下載完畢')
                print("")
                print('下載完畢')
            else :
                self.insert_text(f'下載{self.input_url.get()}' )
                threading.Thread(target=download.download(str(self.input_url.get()),False)).start()
                self.insert_text('下載完畢')
                print("")
                print('下載完畢')
        else:
            print("請檢察網址是否正確或網路連線是否正常")
            self.no_url()
    def mainloop(self):
        self.window.mainloop()

Main = main()
Main.mainloop()
