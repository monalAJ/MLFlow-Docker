from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <body>
            <form action = "/greed" method = "POST">
                Enter Your Name : <input type = "text" name = "username">
                <input type = "submit" value = "Submit">
            </form>
        </body>
        </html>
    '''

@app.route('/greed', methods = ['POST'])
def greed():
    user_input = request.form['username']
    return f"Hello {user_input}, Welcome to this app for Docker demonstration."

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)