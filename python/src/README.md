# 概要
- LOTO6の当選番号のデータをスクレイピング

## 使用ライブラリ：パッケージ
## urllib 
- https://docs.python.org/ja/3.7/howto/urllib2.html

## BeautifulSoup
- HTMLおよびXMLドキュメントを解析するためのPythonパッケージ




# LOTO6のURLについて
## （過去）
### 1-460回
- 0001-0020回 : https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/loto60001.html
- 0021-0040回 : https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/loto60021.html
- ...
- 0441-0460回 : https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/loto60441.html

### 461-1530回
- 0461-0480回 : https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/detail.html?fromto=461_480&type=loto6
- ...
- 1521-1530回 : https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/detail.html?fromto=1521_1530&type=loto6
- ...
- 1641-1651回 : https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/detail.html?fromto=1641_1651&type=loto6

### 備考
- 2023.01.26 時点では、過去は、1530回まで（最新はまた別ページ）


# 参考にしたサイト
## 今更Webスクレイピングを試してロト６のデータを取得
- https://qiita.com/Kis3_/items/1057af45d32617376a67

## スクレイピングで403 Forbidden：You don’t have permission to access on this serverが出た際の対処法
- https://non-dimension.com/solution-403forbidden/

## JavascriptでレンダリングされるWebページを、スクレイピングする
- https://www.yoheim.net/blog.php?q=20170302

