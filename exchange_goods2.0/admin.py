#设置管理员
import pandas as pd
from settings import Settings
from user import User


class Admin(User):
    def __init__(self):
        self.settings = Settings()
        self.admin_data = pd.read_excel(self.settings.admin_datapath)
        self.user_data = pd.read_excel(self.settings.user_datapath)
        self.verified = False

    #验证管理员身份
    def verify(self, password):
        if str(password) == self.settings.admin_password:
            self.verified = True
            return 1
        else:
            return 0

    #返回所有用户信息
    def get_all_users(self):
        self.user_data = pd.read_excel(self.settings.user_datapath)
        return self.user_data

    #保存数据更改
    def save(self):
        self.admin_data.to_excel(self.settings.admin_datapath, sheet_name='Sheet1', index=False)

    #增加分类
    def add_type(self, type):
        if str(type) not in self.admin_data['type'].values:
            self.admin_data.loc[len(self.admin_data)] = [type,0,'','','','','']
            self.save()

    #增加某一分类的特征
    def add_feature(self, type, feature):
        if str(type) in self.admin_data['type'].values:
            col = 'feature_' + str(int(self.admin_data['feature_amount'][self.admin_data['type'] == str(type)])+1)
            self.admin_data[str(col)][self.admin_data['type'] == str(type)] = feature
            self.admin_data['feature_amount'][self.admin_data['type'] == str(type)] = int(self.admin_data['feature_amount'][self.admin_data['type'] == str(type)])+1
            self.save()
            return True
        else:
            return False

    #管理员登出
    def log_out(self):
        self.verified = False