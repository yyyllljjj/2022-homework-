import pandas as pd
from user import User
from admin import Admin
from stock import Stock
from frame import Frame
import tkinter as tk
import warnings


#物品交换
def exchange_start():
    #打开主窗口
    init_window = tk.Tk()
    window = Frame(init_window)
    window.set_init_window()
    init_window.mainloop()

if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    exchange_start()
