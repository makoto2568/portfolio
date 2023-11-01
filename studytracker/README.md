# ここはベースディレクトリです。

<br>

## 本プロジェクトでは， 以下のようなディレクトリ構造になります。

<br>

studytracker/
|
|-- apps/ <-- (ルートアプリケーションディレクトリ)
| |-- accounts/ <-- (アカウントアプリケーションディレクトリ)
| |-- studytracker/ <-- (タスク管理アプリケーションディレクトリ)
|
|-- config/ <-- (設定ディレクトリ)
|-- static/ <-- (静的ディレクトリ)
|-- templates/ <-- (テンプレートのデフォルトディレクトリ)
|-- manage.py
|-- README.md <-- (現ファイル)

<br>
コンテナ作成、実行の際には以下のコマンドを参照してください
<br>
1.Dockerイメージの構築、コンテナ作成
<br>
docker-compose up
<br>
→このコマンドを実行するとサーバが立ちます。
<br>
2.コンテナの停止 docker-compose stop
3.コンテナの再起 docker-compose restart
4.アプリケーションを作成する時 docker-compose run web python manage.py startapp app名
<br>

## commit する際のルール

コミットメッセージは頭に以下のワードを追加する。

- add
- fix
- create
- remove

<br>
上記の意味として，add は追加，fix は修正，create は作成，remove は削除とする。
<br>

ex)

1. `git commit -m "fix チーム管理機能のxxの部分の修正"`
2. `git commit -m "create xxのmodelを作成"`
