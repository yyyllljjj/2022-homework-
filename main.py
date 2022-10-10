import warnings
import tkinter as tk
from frame import MyFrame


#物品交换
def exchange_start():
    init_window = tk.Tk()
    window = MyFrame(init_window)
    window.set_init_window()
    init_window.mainloop()


if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    exchange_start()




