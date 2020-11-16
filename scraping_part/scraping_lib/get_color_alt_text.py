


def get_color_alt_text(element)->str:
  """
  get alt text.
  """
  div = element.find_element_by_class_name("color_img")
  alt = div.find_element_by_tag_name("img").get_attribute("alt")
  return alt