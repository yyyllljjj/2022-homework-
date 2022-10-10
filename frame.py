#可视化窗口
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from settings import Settings
from stock import Stock


class MyFrame:

    #初始化
    def __init__(self, init_window):
        self.settings = Settings()
        self.init_window = init_window
        self.data_stock = Stock()

    #设置主窗口
    def set_init_window (self):

        #设置窗口标题、大小、颜色、标签
        self.init_window.title(self.settings.window_name)
        self.init_window.geometry(self.settings.geometry)
        self.init_window.bg_color = self.settings.bg_color
        text = tk.Label(self.init_window, text=self.settings.welcome_text, font=self.settings.welcome_text_font)
        text.pack()

        #设置增加物品、取出物品、查找物品、查看所有物品、保存修改五个按键
        button_add = tk.Button(self.init_window, text='Add Items', font=self.settings.botton_text_font,
                               command=self.click_button_add).pack()
        button_withdraw = tk.Button(self.init_window, text='Withdraw Items', font=self.settings.botton_text_font,
                                    command=self.click_button_withdraw).pack()
        button_search = tk.Button(self.init_window, text='Search Items', font=self.settings.botton_text_font,
                                  command=self.click_button_search).pack()
        button_view_all = tk.Button(self.init_window, text='View All', font=self.settings.botton_text_font,
                                    command=self.click_button_view).pack()
        button_save = tk.Button(self.init_window, text='Save', font=self.settings.botton_text_font,
                                command=self.click_button_save).pack()

   #增加物品事件
    def click_button_add(self):

        #执行增加物品并关闭窗口
        def add_item(name, amount, window):
            self.data_stock.add_item(name, amount)
            messagebox.showinfo(message=f"you have added {amount} {name}")
            window.destroy()

        #新窗口设置
        add_window = tk.Toplevel()
        add_window.title("Add Items")
        add_window.geometry(self.settings.small_geometry)

        #创建物品名称、物品数量的输入框和其标签
        label1 = tk.Label(add_window, text=self.settings.item_label).pack()
        entry1 = tk.Entry(add_window)
        entry1.pack()
        label2 = tk.Label(add_window, text=self.settings.amount_label).pack()
        entry2 = tk.Entry(add_window)
        entry2.pack()

        #设置OK按键
        button_ok = tk.Button(add_window, text='OK', command=lambda:add_item(entry1.get(), entry2.get(), add_window))
        button_ok.pack()

        #打开窗口
        add_window.mainloop()

    #取出物品事件
    def click_button_withdraw(self):

        #执行取出物品并关闭窗口
        def withdraw_item(name, amount, window):
            flag = self.data_stock.withdraw_item(name, amount)
            if flag:
                messagebox.showinfo(message=f"You have withdrawn {amount} {name}")
            else:
                messagebox.showwarning(message=f"Sorry, the {name} is not enough")
            window.destroy()

        #设置新窗口
        withdraw_window = tk.Toplevel()
        withdraw_window.title('Withdraw Items')
        withdraw_window.geometry(self.settings.small_geometry)

        #创建物品名称、物品数量的输入口及其标签
        label1 = tk.Label(withdraw_window, text=self.settings.item_label).pack()
        entry1 = tk.Entry(withdraw_window)
        entry1.pack()
        label2 = tk.Label(withdraw_window, text=self.settings.amount_label).pack()
        entry2 = tk.Entry(withdraw_window)
        entry2.pack()

        #设置OK按键
        button_ok = tk.Button(withdraw_window, text='OK', command=lambda: withdraw_item(entry1.get(), entry2.get(),                                                                      withdraw_window))
        button_ok.pack()

        #打开窗口
        withdraw_window.mainloop()

    #查找物品事件
    def click_button_search(self):

        #完成信息查找并关闭窗口
        def search_item(name, window):
            amount = self.data_stock.search_item(name)
            if amount > 0:
                messagebox.showinfo(message=f'There are {amount} {name}')
            else:
                messagebox.showinfo(message=f'Sorry, there is no {name}')
            window.destroy()

        #设置新窗口
        search_window = tk.Toplevel()
        search_window.title("Search")
        search_window.geometry(self.settings.small_geometry)

        #设置物品名称的输入框及其标签
        label1 = tk.Label(search_window, text=self.settings.item_label).pack()
        entry1 = tk.Entry(search_window)
        entry1.pack()

        #设置OK按键
        button_ok = tk.Button(search_window, text='OK',
                              command=lambda: search_item(entry1.get(), search_window))
        button_ok.pack()

        #打开窗口
        search_window.mainloop()

    #查看所有物品事件
    def click_button_view(self):

        #设置新窗口
        view_window = tk.Toplevel()
        view_window.title('View All')
        view_window.geometry(self.settings.small_geometry)

        #将物品信息从dataframe数据转化为treeview数据
        cols = list(self.data_stock.get_data())
        tree = ttk.Treeview(view_window)
        tree.pack()
        tree['columns'] = cols
        for i in cols:
            tree.column(i, anchor='w')
            tree.heading(i, text=i, anchor='w')
        for index, row in self.data_stock.get_data().iterrows():
            tree.insert('', 0, text=index, value=list(row))

        #创建滚动轴
        scroll_bar = tk.Scrollbar(view_window, orient='vertical', command=tree.yview)
        scroll_bar.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
        tree.configure(yscrollcommand=scroll_bar.set)

        #打开窗口
        view_window.mainloop()

    #保存数据事件
    def click_button_save(self):
        self.data_stock.save_data()
        messagebox.showinfo(message="The changes have been saved")
