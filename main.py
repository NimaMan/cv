from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('man.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/posts/')
def posts():
    return render_template('posts.html')

if __name__ == '__main__':
    app.run(debug=True)
