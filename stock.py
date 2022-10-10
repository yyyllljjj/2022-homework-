#存储物品
from settings import Settings
import pandas as pd


class Stock:

    #初始化
    def __init__(self):
        self.settings = Settings()
        self.data = pd.read_excel(self.settings.filename)
        self.lenth = len(self.data)

    #更新数据，移除数量为0的物品
    def update(self):
        self.data = self.data.drop(self.data[self.data['amount'] == 0].index)

    #将数据保存到excel文件
    def save_data(self):
        self.data.to_excel(self.settings.filename, sheet_name='Sheet1', index=False)

    #增加物品
    def add_item(self, name, amount):
        if name in self.data['item'].values:  #检查物品是否存在
            self.data['amount'][self.data['item'] == name] += amount  #增加相应数量
        else:
            self.data.loc[self.lenth] = [name, amount]  #创建新物品
            self.lenth += 1
        self.update()

    #取出物品，并返回是否成功
    def withdraw_item(self, name, amount):
        if name in self.data['item'].values:  #检查物品是否存在
            if int(self.data['amount'][self.data['item'] == name]) >= int(amount):  #检查数量是否足够
                self.data['amount'][self.data['item'] == name] = int(self.data['amount'][self.data['item'] == name])  #更改数据类型
                self.data['amount'][self.data['item'] == name] -= int(amount)  #减少相应数量
                self.update()
                return True
        return False

    #查找物品，返回物品数量
    def search_item(self, name):
        if name in self.data['item'].values:  #检查物品是否存在
            return int(self.data['amount'][self.data['item'] == name])
        else:
            return 0

    #返回所有物品信息
    def get_data(self):
        return self.data








