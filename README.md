# フィッグボックス説明

Figboxシステムは何かというと、API管理システムです。(AMS?!😋)<br/>
すべての（サーバー上の）サービスを創作、管理できるシステムです。

## 原理

インターネットのすべてのサービスはAPIの集まりと言ってもいい。（キーワード：Restful、API）<br/>
ということで、APIの管理をうまくできれば、サービスも簡単に作成、管理できるでしょう。<br/>
この考え方でこのシステムを作らせていただきました。（CMSに似ている）

## CMSとは

> CMSとはネット上の文章やページ（コンテンツ）を作成、管理するシステムです。

## CMSとの違い

CMSの機能は文章やコンテンツを管理する。<br/>
だが「文章やコンテンツやページなど」もサービスの一つと考えれば、いっそうサービスを管理すればではないか。<br/>
この考えでFigboxのようなシステムはCMSとして使ってもいいし、他のサービスを開発してもいいの自由なシステムである。

## Figboxの優れたところ

1. サービスをダウンロードして使える。（モジュール化）
1. CMSとして使える。
1. FastapiとPythonを使っているので、開発がものすごく速い。
1. データベースの選択は自由にできる（SQLAlchemyのおかげ）
1. ユーザ管理できる（権限管理は開発中）
1. などなど

> サービスをダウンロードできるのは事前にコードを書いてgithubに保存して置くと、このシステムでそれを使いたい時に自動的ダウンロードして使える。

使い方

```
git clone https://github.com/fig-box-project/fig_box
cd fig_box
screen -S figbox (or you can use tumx)
python3 -m venv ( --without-pip ) venv
source venv/bin/activate
pip3 install -r requirements.txt
uvicorn app.main:app --port 8080 --host 0.0.0.0 --reload
```





