#GUI实现窗口
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from settings import Settings
from stock import Stock
from admin import Admin
from user import User


class Frame:
    def __init__(self, init_window):
        self.settings = Settings()
        self.init_window = init_window
        self.stock = Stock()
        self.admin = Admin()
        self.user = User()
        self.add_type_type = ''

    #主窗口
    def set_init_window(self):
        #基础设置
        self.init_window.title(self.settings.window_name)
        self.init_window.geometry(self.settings.geometry)
        self.init_window.bg_color = self.settings.bg_color
        text = tk.Label(self.init_window, text=self.settings.welcome_text, font=self.settings.welcome_text_font)
        text.pack()

        #主界面按钮
        button_login = tk.Button(self.init_window, text='Login', font=self.settings.botton_text_font,
                               command=self.click_button_login).pack()
        button_register = tk.Button(self.init_window, text='Register', font=self.settings.botton_text_font,
                               command=self.click_button_register).pack()
        button_log_out = tk.Button(self.init_window, text='Logout', font=self.settings.botton_text_font,
                                    command=self.click_button_logout).pack()
        button_admin_login = tk.Button(self.init_window, text='Admin Login', font=self.settings.botton_text_font,
                                    command=self.click_button_admin_login).pack()
        button_admin_logout = tk.Button(self.init_window, text='Admin Logout', font=self.settings.botton_text_font,
                                    command=self.click_button_admin_logout).pack()
        button_view_all_users = tk.Button(self.init_window, text='View_All_Users', font=self.settings.botton_text_font,
                                    command=self.click_button_view_all_users).pack()
        button_view_type = tk.Button(self.init_window, text='View_Type', font=self.settings.botton_text_font,
                                          command=self.click_button_view_type).pack()
        button_view_my_thing = tk.Button(self.init_window, text='View_My_Things', font=self.settings.botton_text_font,
                                    command=self.click_button_view_my_thing).pack()
        button_search_item = tk.Button(self.init_window, text='Search', font=self.settings.botton_text_font,
                                    command=self.click_button_search_item).pack()

    #点击用户登录
    def click_button_login(self):

        #登录
        def log_in(userid, password, window):
            flag = self.user.log_in(userid, password)
            if flag:
                messagebox.showinfo(message=f"Welcome {userid}!")
            else:
                messagebox.showwarning(message="Login Failed")
            window.destroy()

        #新建注册窗口
        login_window = tk.Toplevel()
        login_window.title('Log_In')
        login_window.geometry(self.settings.small_geometry)

        #设置2个动态输入框和标签
        label1 = tk.Label(login_window, text='user_id').pack()
        entry1 = tk.Entry(login_window)
        entry1.pack()
        label2 = tk.Label(login_window, text='password').pack()
        entry2 = tk.Entry(login_window)
        entry2.pack()

        #OK按钮
        button_ok = tk.Button(login_window, text='OK',
                              command=lambda: log_in(entry1.get(), entry2.get(), login_window))
        button_ok.pack()

        #开始循环
        login_window.mainloop()

    #点击注册
    def click_button_register(self):
        def register(userid, password, address, tel, email, window):
            flag = self.user.register(userid, password, address, tel, email)
            if flag:
                messagebox.showinfo(message=f"Succeed! Please wait for the Admin.")
            else:
                messagebox.showwarning(message="Register Failed")
            window.destroy()

        register_window = tk.Toplevel()
        register_window.title('Register')
        register_window.geometry(self.settings.small_geometry)

        label1 = tk.Label(register_window, text='user_id').pack()
        entry1 = tk.Entry(register_window)
        entry1.pack()
        label2 = tk.Label(register_window, text='password').pack()
        entry2 = tk.Entry(register_window)
        entry2.pack()
        label3 = tk.Label(register_window, text='address').pack()
        entry3 = tk.Entry(register_window)
        entry3.pack()
        label4 = tk.Label(register_window, text='tel').pack()
        entry4 = tk.Entry(register_window)
        entry4.pack()
        label5 = tk.Label(register_window, text='email').pack()
        entry5 = tk.Entry(register_window)
        entry5.pack()

        button_ok = tk.Button(register_window, text='OK',
                              command=lambda: register(entry1.get(), entry2.get(), entry3.get(), entry4.get(),
                                                       entry5.get(), register_window))
        button_ok.pack()

        register_window.mainloop()

    def click_button_logout(self):
        self.user.log_out()

    def click_button_view_all_users(self):
        if self.admin.verified == False:
            messagebox.showinfo(message="Please login admin account!")
            return

        view_window = tk.Toplevel()
        view_window.title('View All Users')
        view_window.geometry(self.settings.large_geometry)
        cols = list(self.admin.get_all_users())
        tree = ttk.Treeview(view_window)
        tree.pack()
        tree['columns'] = cols
        for i in cols:
            tree.column(i, anchor='w')
            tree.heading(i, text=i, anchor='w')
        for index, row in self.admin.get_all_users().iterrows():
            tree.insert('', 0, text=index, value=list(row))

        # 创建滚动轴
        scroll_bar_y = tk.Scrollbar(view_window, orient='vertical', command=tree.yview)
        scroll_bar_y.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
        tree.configure(yscrollcommand=scroll_bar_y.set)

        button_activate_users = tk.Button(view_window, text='Activate_Users', font=self.settings.botton_text_font,
                                          command=self.click_button_activate_users).pack()

        # 打开窗口
        view_window.mainloop()

    def click_button_admin_logout(self):
        self.admin.log_out()

    def click_button_admin_login(self):
        def admin_login(password, window):
            flag = self.admin.verify(password)
            if flag == 1:
                messagebox.showinfo(message="Login Succeed!")
            else:
                messagebox.showwarning(message="The password is incorrect!")
            window.destroy()

        admin_login_window = tk.Toplevel()
        admin_login_window.title('Admin Login')
        admin_login_window.geometry(self.settings.small_geometry)

        label1 = tk.Label(admin_login_window, text='password').pack()
        entry1 = tk.Entry(admin_login_window)
        entry1.pack()

        button_ok = tk.Button(admin_login_window, text='OK',
                              command=lambda: admin_login(entry1.get(), admin_login_window))
        button_ok.pack()

        admin_login_window.mainloop()

    def click_button_activate_users(self):
        def activate_user(userid,window):
            self.user.set_id(userid)
            self.user.activate()
            messagebox.showinfo(message=f'the user {userid} has been activated')
            window.destroy()

        activate_user_window = tk.Toplevel()
        activate_user_window.title('Activate User')
        activate_user_window.geometry(self.settings.small_geometry)

        label1 = tk.Label(activate_user_window, text='user id').pack()
        entry1 = tk.Entry(activate_user_window)
        entry1.pack()

        button_ok = tk.Button(activate_user_window, text='OK',
                              command=lambda: activate_user(entry1.get(), activate_user_window))
        button_ok.pack()

        activate_user_window.mainloop()

    def click_button_view_type(self):
        view_window = tk.Toplevel()
        view_window.title('View Types')
        view_window.geometry(self.settings.large_geometry)
        cols = list(self.admin.admin_data)
        tree = ttk.Treeview(view_window)
        tree.pack()
        tree['columns'] = cols
        for i in cols:
            tree.column(i, anchor='w')
            tree.heading(i, text=i, anchor='w')
        for index, row in self.admin.admin_data.iterrows():
            tree.insert('', 0, text=index, value=list(row))

        button_add_type = tk.Button(view_window, text='Add Type', font=self.settings.botton_text_font,
                                     command=self.click_button_add_type).pack()
        button_add_feature = tk.Button(view_window, text='Add Feature', font=self.settings.botton_text_font,
                                     command=self.click_button_add_feature).pack()

        view_window.mainloop()


    def click_button_view_my_thing(self):
        if self.user.if_log_in() == False:
            messagebox.showinfo(message="Please login your account!")
            return

        def set_add_type(type, window):
            self.add_type_type = type

        view_window = tk.Toplevel()
        view_window.title('View My Things')
        view_window.geometry(self.settings.large_geometry)
        data = self.stock.get_my_data(self.user.user_id).dropna(axis=1)
        data = data.drop('item', axis=1)
        data = data.drop('owner', axis=1)
        data = data.drop('type', axis=1)
        cols = list(data)
        tree = ttk.Treeview(view_window)
        tree.pack()
        tree['columns'] = cols
        for i in cols:
            tree.column(i, anchor='w')
            tree.heading(i, text=i, anchor='w')
        for index, row in data.iterrows():
            tree.insert('', 0, text=index, value=list(row))

        label1 = tk.Label(view_window, text='type').pack()
        entry1 = tk.Entry(view_window)
        entry1.pack()
        self.add_type_type = entry1.get()

        button_ok = tk.Button(view_window, text='OK',
                              command=lambda: set_add_type(entry1.get(), view_window))
        button_ok.pack()

        button_add_item = tk.Button(view_window, text='Add Item', font=self.settings.botton_text_font,
                                    command=self.click_button_add_item).pack()
        button_delete_item = tk.Button(view_window, text='Delete Item', font=self.settings.botton_text_font,
                                       command=self.click_button_delete_item).pack()

        view_window.mainloop()

    def click_button_add_type(self):
        if not self.admin.verified:
            messagebox.showwarning(message="Please login admin account!")
            return

        def add_type(type, window):
            self.admin.add_type(type)
            messagebox.showinfo(message=f"The type {type} has been added!")
            window.destroy()

        add_type_window = tk.Toplevel()
        add_type_window.title('Add Type')
        add_type_window.geometry(self.settings.small_geometry)

        label1 = tk.Label(add_type_window, text='type').pack()
        entry1 = tk.Entry(add_type_window)
        entry1.pack()

        button_ok = tk.Button(add_type_window, text='OK',
                              command=lambda: add_type(entry1.get(), add_type_window))
        button_ok.pack()

        add_type_window.mainloop()

    def click_button_add_feature(self):
        if not self.admin.verified:
            messagebox.showwarning(message="Please login admin account!")
            return

        def add_feature(type, feature, window):
            self.admin.add_feature(type, feature)
            messagebox.showinfo(message=f"The feature {feature} of type {type} has been added!")
            window.destroy()

        add_feature_window = tk.Toplevel()
        add_feature_window.title('Add Type')
        add_feature_window.geometry(self.settings.small_geometry)

        label1 = tk.Label(add_feature_window, text='type').pack()
        entry1 = tk.Entry(add_feature_window)
        entry1.pack()
        label2 = tk.Label(add_feature_window, text='feature').pack()
        entry2 = tk.Entry(add_feature_window)
        entry2.pack()

        button_ok = tk.Button(add_feature_window, text='OK',
                              command=lambda: add_feature(entry1.get(), entry2.get(),add_feature_window))
        button_ok.pack()

        add_feature_window.mainloop()

    def click_button_add_item(self):
        if self.add_type_type == '':
            messagebox.showerror(message="Please input type!")
            return

        def add_item(user_id, item_name, type, feature, valid, description, window):
            f = feature
            for i in range(4, -1, -1):
                if len(str(valid[i])) == 0:
                    f[i] = ' '
            print(f)

            if self.stock.add_item(user_id, type, item_name, f, description):
                messagebox.showinfo(message=f"The {item_name} has been added!")
            else:
                messagebox.showerror("Please input correct type!")

        add_item_window = tk.Toplevel()
        add_item_window.title('Add Type')
        add_item_window.geometry(self.settings.small_geometry)

        label1 = tk.Label(add_item_window, text='item_name').pack()
        entry1 = tk.Entry(add_item_window)
        entry1.pack()
        label2 = tk.Label(add_item_window, text='description').pack()
        entry2 = tk.Entry(add_item_window)
        entry2.pack()
        feature_1 = str(self.admin.admin_data['feature_1'][self.admin.admin_data['type'] == self.add_type_type])
        print(feature_1)
        feature_2 = str(self.admin.admin_data['feature_2'][self.admin.admin_data['type'] == self.add_type_type])
        feature_3 = str(self.admin.admin_data['feature_3'][self.admin.admin_data['type'] == self.add_type_type])
        feature_4 = str(self.admin.admin_data['feature_4'][self.admin.admin_data['type'] == self.add_type_type])
        feature_5 = str(self.admin.admin_data['feature_5'][self.admin.admin_data['type'] == self.add_type_type])

        label3 = tk.Label(add_item_window, text=str(feature_1)).pack()
        entry3 = tk.Entry(add_item_window)
        if not len(feature_1) == 0:
            entry3.pack()
        label4 = tk.Label(add_item_window, text=str(feature_2)).pack()
        entry4 = tk.Entry(add_item_window)
        entry4.pack()
        label5 = tk.Label(add_item_window, text=str(feature_3)).pack()
        entry5 = tk.Entry(add_item_window)
        entry5.pack()
        label6 = tk.Label(add_item_window, text=str(feature_4)).pack()
        entry6 = tk.Entry(add_item_window)
        entry6.pack()
        label7 = tk.Label(add_item_window, text=str(feature_5)).pack()
        entry7 = tk.Entry(add_item_window)


        button_ok = tk.Button(add_item_window, text='OK',
                              command=lambda: add_item(self.user.user_id, entry1.get(), self.add_type_type,
                                                       [entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get()],
                                                       [feature_1, feature_2, feature_3, feature_4, feature_5],
                                                       entry2.get(), add_item_window))
        button_ok.pack()

        add_item_window.mainloop()

    def click_button_delete_item(self):
        def delete_item(item, window):
            self.stock.delete_item(self.user.user_id, item)
            messagebox.showinfo(message=f"The item {item} has been deleted!")
            window.destroy()

        delete_item_window = tk.Toplevel()
        delete_item_window.title('Delete_item')
        delete_item_window.geometry(self.settings.small_geometry)

        label1 = tk.Label(delete_item_window, text='item_name').pack()
        entry1 = tk.Entry(delete_item_window)
        entry1.pack()

        button_ok = tk.Button(delete_item_window, text='OK',
                              command=lambda: delete_item(entry1.get(),delete_item_window))
        button_ok.pack()
        delete_item_window.mainloop()

    def click_button_search_item(self):
        def search_item(type, keyword, window):
            data = self.stock.search_item(type, keyword)
            view_window = tk.Toplevel()
            view_window.title('search result')
            view_window.geometry(self.settings.large_geometry)
            data = data.dropna(axis=1)
            data = data.drop('item', axis=1)
            data = data.drop('owner', axis=1)
            data = data.drop('type', axis=1)
            cols = list(data)
            tree = ttk.Treeview(view_window)
            tree.pack()
            tree['columns'] = cols
            for i in cols:
                tree.column(i, anchor='w')
                tree.heading(i, text=i, anchor='w')
            for index, row in data.iterrows():
                tree.insert('', 0, text=index, value=list(row))

        def view_all_item(type, window):
            data = self.stock.get_type_data(type)
            view_window = tk.Toplevel()
            view_window.title(f'All things of the type {type}')
            view_window.geometry(self.settings.large_geometry)
            data = data.dropna(axis=1)
            data = data.drop('item', axis=1)
            data = data.drop('owner', axis=1)
            data = data.drop('type', axis=1)
            cols = list(data)
            tree = ttk.Treeview(view_window)
            tree.pack()
            tree['columns'] = cols
            for i in cols:
                tree.column(i, anchor='w')
                tree.heading(i, text=i, anchor='w')
            for index, row in data.iterrows():
                tree.insert('', 0, text=index, value=list(row))


        search_item_window = tk.Toplevel()
        search_item_window.title('Search Item')
        search_item_window.geometry(self.settings.small_geometry)

        label1 = tk.Label(search_item_window, text='type').pack()
        entry1 = tk.Entry(search_item_window)
        entry1.pack()

        label2 = tk.Label(search_item_window, text='keyword').pack()
        entry2 = tk.Entry(search_item_window)
        entry2.pack()

        button_ok = tk.Button(search_item_window, text='OK',
                              command=lambda: search_item(entry1.get(), entry2.get(), search_item_window))
        button_ok.pack()

        button_view_all = tk.Button(search_item_window, text='view_all_item',
                              command=lambda: view_all_item(entry1.get(),search_item_window))
        button_view_all.pack()

        search_item_window.mainloop()