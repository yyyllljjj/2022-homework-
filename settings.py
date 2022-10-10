#设置

class Settings:

    def __init__(self):

        #窗口设置#
        self.geometry = '1068x681+10+10'
        self.bg_color = (230, 230, 230)
        self.window_name = 'exchange platform'
        self.small_geometry = '600x400'

        #标签设置
        self.welcome_text = 'Welcome to Goods Exchange Platform'
        self.welcome_text_font = ('Times', 30, 'bold italic')
        self.botton_text_font = ('Times', 20, 'bold')
        self.item_label = 'item:'
        self.amount_label = 'amount:'

        #表格设置
        self.filename = 'data/item1.xlsx'
