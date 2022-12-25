from settings import Settings
import pandas as pd


#物品仓库
class Stock:
    def __init__(self):
        self.settings = Settings()
        self.stock_data = pd.read_excel(self.settings.stock_datapath)
        self.user_data = pd.read_excel(self.settings.user_datapath)
        self.len = len(self.stock_data)

    #保存更新数据
    def save(self):
        self.stock_data = self.stock_data.drop(self.stock_data[self.stock_data['exist'] == 0].index)
        self.user_data = pd.read_excel(self.settings.user_datapath)
        self.stock_data.to_excel(self.settings.stock_datapath, sheet_name='Sheet1', index=False)

    #增加物品
    def add_item(self, user_id, type, item_name, feature, description):

        item_owner = item_name + '_' + user_id
        user_data = pd.read_excel(self.settings.user_datapath)
        type_data = pd.read_excel(self.settings.admin_datapath)

        if str(type) not in type_data['type'].values:
            return False

        owner_email = user_data['email'][user_data['name'] == user_id]
        owner_address = user_data['address'][user_data['name'] == user_id]
        owner_tel = user_data['tel'][user_data['name'] == user_id]
        feature_1 = feature[0]
        feature_2 = feature[1]
        feature_3 = feature[2]
        feature_4 = feature[3]
        feature_5 = feature[4]
        self.stock_data.loc[len(self.stock_data)] = [item_owner, item_name, user_id, feature_1, feature_2, feature_3,
                                                     feature_4, feature_5, type, owner_tel, owner_email, owner_address,
                                                     description, 1]
        self.save()
        return True

    #删除物品
    def delete_item(self, user_id, item_name):
        item_owner = item_name + '_' + user_id
        self.stock_data['exist'][self.stock_data['item_owner'] == item_owner] = 0
        self.save()

    #获得所有物品数据
    def get_all_data(self):
        return self.stock_data

    #获得自己的物品数据
    def get_my_data(self, userid):
        return self.stock_data[self.stock_data['owner'] == userid]

   #获得指定种类所有物品的信息
    def get_type_data(self, type):
        return self.stock_data[self.stock_data['type'] == type]

    #查找物品
    def search_item(self, type, key_word):
        self.stock_data = pd.read_excel(self.settings.stock_datapath)
        data1 = self.get_type_data(type)
        print(data1)
        return data1[data1['item'] == key_word]
