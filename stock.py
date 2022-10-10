#存储物品
from settings import Settings
import pandas as pd


class Stock:

    #初始化
    def __init__(self):
        self.settings = Settings()
        self.data = pd.read_excel(self.settings.filename)
        self.lenth = len(self.data)

    #更新数据
    def update(self):
        self.data = self.data.drop(self.data[self.data['amount'] == 0].index)

    #保存数据
    def save_data(self):
        self.data.to_excel(self.settings.filename, sheet_name='Sheet1', index=False)

    #增加物品
    def add_item(self, name, amount):
        if name in self.data['item'].values:
            self.data['amount'][self.data['item'] == name] += amount
        else:
            self.data.loc[self.lenth] = [name, amount]
            self.lenth += 1
        self.get_data()
        self.update()

    #取出物品，并返回是否成功
    def withdraw_item(self, name, amount):
        if name in self.data['item'].values:
            if int(self.data['amount'][self.data['item'] == name]) >= int(amount):
                self.data['amount'][self.data['item'] == name] = int(self.data['amount'][self.data['item'] == name])
                self.data['amount'][self.data['item'] == name] -= int(amount)
                self.update()
                return True
        return False

    #查找物品，返回物品数量
    def search_item(self, name):
        if name in self.data['item'].values:
            return int(self.data['amount'][self.data['item'] == name])
        else:
            return 0

    #获取所有物品信息
    def get_data(self):
        print(self.data)
        return self.data








