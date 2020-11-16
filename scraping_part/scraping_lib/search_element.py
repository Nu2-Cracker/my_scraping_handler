import numpy as np
import time
from scraping_part.scraping_lib.get_color_alt_text import get_color_alt_text



def scraping_element(list_item):
  """
  list_ite is draiver or elemnt.
  This module role is search and get specific text, such as title, alt, discription 
  """
  try:
    div_name = list_item.find_element_by_class_name("item_name")
    title = div_name.find_element_by_class_name("name")
  except:
    title = np.nan

  try:
    color = list_item.find_element_by_css_selector("ul.color.clearfix")
    ul = color.find_elements_by_tag_name("li")
    alt = [get_color_alt_text(li) for li in ul]
    color = " ".join(alt)
  except:
    color = np.nan

  try:
    discription = list_item.find_element_by_class_name("description")
  except:
    discription = np.nan

  time.sleep(1)
  return title.text, color, discription.text
