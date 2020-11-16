import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scraping_part.scraping_lib import search_element as elm
import pandas as pd




class selenium_setting:
    def __init__(self):
        op = Options()
        # --headlessだけではOSによって動かない、プロキシが弾かれる、
        # CUI用の省略されたHTMLが帰ってくるなどの障害が出ます。
        # 長いですが、これら6行あって最強かつどんな環境でも動きますので、必ず抜かさないようにしてください。
        op.add_argument("--disable-gpu")
        op.add_argument("--disable-extensions")
        op.add_argument("--proxy-server='direct://'")
        op.add_argument("--proxy-bypass-list=*")
        op.add_argument("--start-maximized")
        op.add_argument("--incognito")
        op.add_argument("--headless")
        op.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(chrome_options=op, executable_path="C:\\Users\\da-uehara\\Desktop\\chromedriver_win32\\chromedriver.exe")


class scraping_ex(selenium_setting):

    def driver_handler(self, keyword):
        self.driver.get("https://www.ex-shop.net/")
        time.sleep(0.5)
        self.driver.find_element_by_id("itemname").send_keys(keyword) #商品名を探す欄に入力
        self.driver.find_element_by_class_name("left-search_btn").click() #商品を検索
        time.sleep(1.2)
        self.driver.get(self.driver.current_url) #ページ遷移
        time.sleep(2.42)

    def create_dict(self):
        datas = {"タイトル": [], "カラー":[],  "説明": []}
        item_list_unit = self.driver.find_element_by_id("item_list_unit")
        unit = item_list_unit.find_elements_by_class_name("list_item")
        for list_item in unit:
            title, color, discription = elm.scraping_element(list_item)
            datas["タイトル"].append(title)
            datas["カラー"].append(color)
            datas["説明"].append(discription)
        return datas

    
    def write_data(self):
        datas = self.create_dict()
        df = pd.DataFrame(datas)
        df.to_csv("scrape_data.csv", index=False)

    def __call__(self, keyword):
        self.driver_handler(keyword)
        self.write_data()
        self.driver.close()



#temp
#pandasのdatatableに入れて、そのままdbに格納 付属のsqliteでいいや。

