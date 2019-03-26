from flask import Flask, request, render_template

# 使用flask快速开发webapp ，先创建出对象，使用装饰模式构建
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signform():
    return render_template('signin.html', message='123')


@app.route('/signin_result', methods=['POST'])
def signin():
    # request.form['username'] 可以拿到表单中给的数据
    username = request.form['username']
    password = request.form['password']
    return render_template('signin_result.html', username=username, password=password)


if __name__ == '__main__':
    app.run()
