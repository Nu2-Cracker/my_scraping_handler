
from scraping_part.scraping_ex import scraping_ex

def ex_scraping_handler(keyword):
  """
  エクスショップホームページからタイトル、カラー、説明文を取得
  """
  x = scraping_ex()
  x(keyword)

