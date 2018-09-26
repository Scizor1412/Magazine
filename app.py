from flask import *
import mlab
from models.db_user import User
from models.db_article import Article
app = Flask(__name__)

mlab.connect()

app.secret_key = "secret key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods = [ 'GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        form = request.form
        new_user = User(
            fullname = form['fullname'],
            yob = form['yob'],
            email = form['email'],
            password = form['password'],
        )
        new_user.save()
        return redirect(url_for('login'))

@app.route('/admin')
def admin():
    if 'loggedin' in session:
        if session['loggedin'] == True:
            return render_template('admin.html')
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/admin/user')
def admin_user():
    users = User.objects()
    return render_template('admin_user.html', users = users)

@app.route('/admin/article')
def admin_article():
    articles = Article.objects()
    return render_template('admin_article.html', articles = articles)

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        email = form['email']
        password = form['password']
        found_user = User.objects.get(email = email, password = password)
        if found_user is not None:
            session['loggedin'] = True
            return redirect(url_for('admin'))

@app.route('/homepage')
def homepage():
    return render_template("homepage.html")

if __name__ == '__main__':
  app.run(debug=True)