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
        if Check_URL.Check_Url(str(self.input_url.get())):
            if self.download == "yes":
                self.listbox.insert(tk.END, '下載{}'.formate(self.input_url.get()) )
                threading.Thread(target=download.download(str(self.input_url.get()),True)).start()
                self.listbox.insert(tk.END, '下載完畢')
            else :
                threading.Thread(target=download.download(str(self.input_url.get()),False)).start()
        else:
            print("請檢察網址是否正確或網路連線是否正常")
            self.no_url()
    def mainloop(self):
        self.window.mainloop()

Main = main()
Main.mainloop()
