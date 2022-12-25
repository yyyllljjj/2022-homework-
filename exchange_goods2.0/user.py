from settings import Settings
import pandas as pd


#设置普通用户
class User:
    def __init__(self, userid=''):
        self.settings = Settings()
        self.user_data = pd.read_excel(self.settings.user_datapath)
        self.user_id = userid

    #检查用户id是否存在
    def id_exist(self, userid):
        if str(userid) in self.user_data['name'].values:
            return True
        else:
            return False

    #保存数据更改
    def save(self):
        self.user_data.to_excel(self.settings.user_datapath, sheet_name='Sheet1', index=False)
        self.user_data = pd.read_excel(self.settings.user_datapath)

    #注册
    def register(self, userid, password, address, tel, email):
        if not self.id_exist(userid):
            self.user_data.loc[len(self.user_data)] = [userid, password, address, tel, email, 0]
            self.save()
            return True
        else:
            return False

    #激活
    def activate(self):
        self.user_data['activation'][self.user_data['name'] == self.user_id] = 1
        self.user_id = ''
        self.save()

    #登录
    def log_in(self, userid, password):
        self.user_data = pd.read_excel(self.settings.user_datapath)
        if not self.id_exist(userid):
            return False
        elif int(self.user_data['password'][self.user_data['name'] == userid]) == int(password):
            if int(self.user_data['activation'][self.user_data['name'] == userid]) == 1:
                self.user_id = userid
                return True
            else:
                return False
        else:
            return False

    #登出
    def log_out(self):
        self.user_id = ''

    #检查是否登录
    def if_log_in(self):
        return not self.user_id == ''

    #设置用户id（激活专用）
    def set_id(self, userid):
        self.user_id = str(userid)



