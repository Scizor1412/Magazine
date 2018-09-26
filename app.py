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
# Sửa thông tin người dùng
@app.route('/detele_user/<user_id>')
def delete_user(user_id):
    delete_user = User.objects.with_id(user_id)
    if delete_user is not None:
        delete_user.delete()
        return redirect(url_for('admin'))
    else:
        return "Not found"

@app.route('/edit_user/<user_id>')
def edit_user(user_id):
    edit_user = User.objects.with_id(user_id)
    if edit_user is not None:
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('admin'))

# Sửa thông tin bài viết
@app.route('/delete_article/<article_id>')
def delete_article(article_id):
    delete_article = Article.objects.with_id(article_id)
    if delete_article is not None:
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('admin'))


@app.route('/edit_article/<article_id>')
def edit_article(article_id):
    edit_article = Article.objects.with_id(article_id)
    if edit_article is not None:
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('admin'))

# phê duyệt bài viết
@app.route('/approval_article/<article_id>')
def approval_article(article_id):
    approval_article = Article.objects.with_id(article_id)
    if approval_article is not None:
        return redirect(url_for('admin'))
    else:
        approval_article = Article.objects.with_id(article_id)
# Phê duyệt người dùng
@app.route('/approval_user/<user_id>')
def approval_user(user_id):
    user_id = User.objects.with_id(user_id)
    if user_id is not None:
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('admin'))
        
@app.route('/reject_user/<user_id>')
def reject_user(user_id):
    user_id = User.objects.with_id(user_id)
    if user_id is not None:
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('admin'))

@app.route('/homepage')
def homepage():
    return render_template("homepage.html")

if __name__ == '__main__':
  app.run(debug=True)