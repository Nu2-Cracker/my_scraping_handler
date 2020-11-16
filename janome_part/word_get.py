from janome.tokenizer import Tokenizer
import os
from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter, TokenCountFilter


class word_get:

  def __init__(self):
    token_filters = [POSKeepFilter(['名詞,固有名詞','名詞,一般']), TokenCountFilter()]
    self.a = Analyzer(token_filters=token_filters)

  def open_text(self, path):
    with open(path, mode="r", encoding="utf-8", newline='') as f:
      sentence = str(f.read())
      self.list_= [token[0]+"\n" for token in self.a.analyze(sentence)]

  def writer_text(self, path):
    with open(path, mode="w", encoding="utf-8", newline='') as f:
      list(map(f.write, self.list_))

  def __call__(self, path):
    #pathからシリーズ名（ファイル名のみ抜き出す）
    series_name = os.path.splitext(os.path.basename(path))[0]
    output_path = os.path.join(os.path.dirname(path),"output", series_name + ".csv")
    self.open_text(path)
    self.writer_text(output_path)
    


def word_create(path):
  x = word_get()
  x(path)


