import warnings
import tkinter as tk
from frame import MyFrame


#物品交换
def exchange_start():
    #打开主窗口
    init_window = tk.Tk()
    window = MyFrame(init_window)
    window.set_init_window()
    init_window.mainloop()


if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    exchange_start()




