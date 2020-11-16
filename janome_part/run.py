import os
from word_get import word_create



#janpme_data_set内からtxtファイルのパスを取得
path_list = [entry.path for entry in os.scandir("janpme_data_set") if os.path.isfile(entry.path)]

#各ファイルに形態素解析を実行,データ出力
list(map(word_create, path_list))
print('successed!!')
