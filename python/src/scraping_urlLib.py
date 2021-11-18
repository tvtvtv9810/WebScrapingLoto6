from bs4 import BeautifulSoup
# from urllib import request
import urllib.parse
import urllib.request

import time
import random
import pandas as pd

# ロト6の当選番号が掲載されているみずほ銀行ページのURL
loto_url_1_460 = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/loto6' # 1～460回目
loto_url_461_1530 = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/detail.html?fromto=' # 461回目以降

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
headers = {'User-Agent': user_agent}
values = {}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')

main_num_list = [] # 本数字6桁を格納するリスト
bonus_num_list = [] # ボーナス数字を格納するリスト

num = 1 
num_to = 460 # 1341 # 461回以降はJavascriptでレンダリングされる為urlLibでは取得できない
while num <= num_to:

  # 第1～460回目までの当選ページのURL
  if num < 461:
    url = loto_url_1_460 + str(num).zfill(4) + '.html'
  # 461回目以降当選ページのURL
  else:
    url = loto_url_461_1530 + str(num) + '_' + str(num+19) + '&type=loto6'

  print(url)
  req = urllib.request.Request(url, data, headers)
  with urllib.request.urlopen(req) as response:
    the_page = response.read()

  soup = BeautifulSoup(the_page, "html.parser")
  print(soup)

  print(soup.title)

  # ロト6の当選番号がのっているテーブルの取得
  table = soup.find_all("table")
  del table[0]

  for i in table:
    # 本数字の取得
    main_num = i.find_all("tr")[2].find("td")
    print(main_num)
    main_num_split = main_num.string.split(" ")
    if main_num_split is not None:
      main_num_list.append(main_num_split)

    # ボーナス数字の取得
    bonus_num = i.find_all("tr")[3].find("td")
    bonus_num_list.append(bonus_num.string)

  num += 20 # 次のページに移動するためにnumに20を追加
  time.sleep(random.uniform(1, 3)) # 1～3秒Dos攻撃にならないようにするためにコードを止める

# csvで出力
df = pd.DataFrame(main_num_list, columns = ['main1', 'main2', 'main3', 'main4', 'main5', 'main6'])
df['bonus'] = bonus_num_list
df.index = df.index + 1
df.to_csv('./loto6.csv')

