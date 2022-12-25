class Settings:
    def __init__(self):
        #管理员密码
        self.admin_password = 'q'

        #数据存储路径
        self.admin_datapath = './data/admin.xlsx'
        self.stock_datapath = './data/stock.xlsx'
        self.user_datapath = './data/user.xlsx'

        #窗口信息
        self.geometry = '1068x681+10+10'
        self.bg_color = (230, 230, 230)
        self.window_name = 'exchange platform'
        self.small_geometry = '600x400'
        self.large_geometry = '1600x800'

        #欢迎文字设置
        self.welcome_text = 'Welcome to Goods Exchange Platform'
        self.welcome_text_font = ('Times', 30, 'bold italic')
        self.botton_text_font = ('Times', 20, 'bold')
