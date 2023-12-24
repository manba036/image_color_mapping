# image_color_mapping

HSVのHS空間上に似たような色味の画像が近くに配置されるようにマッピング表示する

----
## ■ 使い方

### 1) 必要なモジュールをインストール

```bash
$ pip3 install -r requirements.txt
```

【補足】環境によっては `pip` に読み替え

### 2) マッピングしたい画像を用意

`images`フォルダにマッピングしたい画像ファイルをコピー

【補足1】拡張子が `jpg`, `JPG`, `jpeg` の画像ファイルが対象  
【補足2】画像ファイルはフォルダ分けされていても構わない

### 3) 必要なファイル(json)を生成

```bash
$ python3 generate_nodes_array_json.py
```

【補足】環境によっては `python` に読み替え

### 4) htmlをブラウザで開く

`color_mapping.html` をブラウザで開く

【補足1】動作確認は `Chrome` で実施  
【補足2】CDNでjQueryライブラリ等を読み込むためインターネット環境が必要

----
## ■ 参考にしたサイト／記事

| # | タイトル(Link) | 参考にした点 |
|:-:|:--|:--|
| 1 | [ネットワーク型（ノード型、二分木型、ツリー型）のデータをブラウザで描画する (vis.js)](https://qiita.com/oyahiroki/items/16d883d8a6d45ec03d68) | [JavaScript] vis.js Networkの基本的な使い方 |
| 2 | [vis.js Network公式](https://visjs.github.io/vis-network/docs/network/) | [JavaScript] vis.js Networkの各種オプション |
| 3 | [JavaScriptでJSONファイルをローカルから読み込みするには](https://pisuke-code.com/javascript-load-local-json-file/) | [JavaScript] ローカルjsonを読み込む |
| 4 | [【サンプルコードあり】クリップボードへのコピー機能をjQueryで実装！](https://ungifted.tech/blog/copy-to-clipboard/) | [JavaScript] クリップボードに任意の文字列をコピー |
| 5 | [colorsysでライブラリ不要でRGB→HSV変換をする](https://blog.shikoan.com/colorsys/) | [Python] RGB→HSV変換 |

----
## 以上
