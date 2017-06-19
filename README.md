# コマンドラインベースでtodoリスト管理したくなったヲタク達へ

# コーディング規約
特になし。pep8を参考にしたい(願望)。

# ブランチ
develop追加

# 機能
## 第1目標
* ~~todoリストをMongoDBで記録・管理~~
* MongoDBサーバー建てるのめんどいからsqliteでいいや
* todoの追加・削除・閲覧・編集くらいの機能はほしいよね

## 第2目標
* PyPIに登録してpipでインストールできるようにしたいよね

## 第3目標
* Flask使ってブラウザから閲覧出webアプリケーションも実装したいよね

## 第4目標
* サーバー使ってアカウント管理出来るようにしたいよね
* アカウントでログインすれば複数端末で共有できるみたいな
* 友人のアカウントと連携して、todoリストの共有とかできるといいかもね

## 第5目標
* API造ってアプリケーションからtodolist管理出来るようにしたいよね

## 第6目標
* 造ったAPIを利用してAndroidなりiPhoneなりでアプリケーション作りたいよね

# Usage(理想)
## タスクの追加

```console
$ todolist-py add [-d limit-day] [-p priority] task-title
```
### 実行結果
MongoDBに以下のデータが格納される

DBのスキーマ|格納されるデータ|メモ
:-:|:-:|:-:
id|タスクのid|primary key
title|タスクのタイトル|not null
limit|タスクの期限|日付型とかあれば null ok
priority|タスクの優先度|初期値は3とか
state|タスクの状態|True=完了<br>False=未完<br>初期値はもちろんFalse


### オプションの説明
オプション|説明|取りうる値
:-:|:-:|:-:
-d<br>--day|タスクの期限(日)|0以上の数値
-p<br>--priority|タスクの優先度|1-6までの数値

## タスクの閲覧

```console
$ todolist-py show
```
### 実行結果
タスクの一覧をテーブルにしてガーーーっと

id|title|limit|priority
:-:|:-:|:-:|:-:
1|taskA|あと2日|3
2|taskB||4
3|taskC|明日まで|2

### オプションの説明
とりあえずなし。将来的にソートするオプションとか、抽出するオプションとかあってもいいかも

## タスク管理

```console
$ todolist-py edit id
```

### 実行結果

```console
$todolist-py edit 2
newtitle[taskB]:taskBB
newlimit[]:2
newpriority[4]:

Succsess edit
2 | taskBB  |あと2日| 4
$
```
### オプションの説明
これもとりあえずなし。  
対話形式じゃなくてコマンドベースで変更できた方が楽かも

## タスク削除

```console
$todolist-py delete id
```

### 実行結果

```console
$ todolist-py delete 2

2 | taskBB  |あと2日| 4

Delete this task ?[yes|no]:yes

Succsess delete
$
```
### オプションの説明
-y とかあってもいいかも

## タスク完了

```console
$ todolist-py finish id
```

### 実行結果

```console
$ todolist-py finish 2

2 | taskBB  |あと2日| 4

Finish this task ?[yes|no]:yes

お疲れ様的な何か

$
```
### オプションの説明
-y とかあってもいいかも

# DBのスキーマ
スキーマ名|型|説明
:-:|:-:|:-:
id|int primary key|タスク識別用id
title|str not null|タスクのタイトル
limit|date|タスクの期日
priority|int not null|タスクの優先度<br>デフォルトは3かな
lastedit|date|最終更新日時(まだ使わないと思うけどとりあえず)
