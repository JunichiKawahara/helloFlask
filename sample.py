# ウェブアプリケーションフレームワークFlaskを使ってみる
# https://qiita.com/ynakayama/items/2cc0b1d3cf1a2da612e4

from flask import Flask, render_template, request, redirect, url_for
import numpy as np

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)


# メッセージをランダムに表示するメソッド
def picked_up():
    messages = [
        "こんにちは、あなたの名前を入力してください",
        "やあ！お名前は何ですか？",
        "あなたの名前を教えてね"
    ]
    return np.random.choice(messages)


# ここからウェブアプリケーション用のルーティングを記述する
# index にアクセスした時の処理
@app.route('/')
def index():
    title = 'ようこそ'
    message = picked_up()
    # index.html をレンダリングする
    return render_template('index.html',
                           message=message, title=title)


# /post にアクセスした時の処理
@app.route('/post', methods=['GET', 'POST'])
def post():
    title = 'こんにちは'
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html',
                               name=name, title=title)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
