# oshin-django
## DjangoによるWebアプリケーション開発の検証

## 必要環境

- docker version 20.10.x 以上

## セットアップ・実行方法

```console
# build
$ docker compose build --no-cache

# Blackによるコード整形
$ docker compose run --rm yomilog black black_sample.py

# Ruffによるリンター修正
$ docker compose run --rm yomilog ruff ruff_sample.py --fix

# mypyによる静的型チェック
$ docker compose run --rm yomilog mypy mypy_sample.py

# pdbによるデバッグ
# インタープリタで「s」を入力すると1行ずつステップ実行する
# その時の変数の中身を確認するときは「p 変数名」と入力する
$ docker compose run --rm yomilog python debug.py

# boost
$ docker compose up
```
