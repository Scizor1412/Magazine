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
            return render_template('admin.html', userid = session['id'])
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
            session['id'] = str(found_user.id)
            return redirect(url_for('admin'))

@app.route('/detele_user/<user_id>')
def delete_user(user_id):
    delete_user = User.objects.with_id(user_id)
    if delete_user is not None:
        delete_user.delete()
        return redirect(url_for('admin'))
    else:
        return "Not found"

@app.route('/edit_user/<user_id>', methods = ['GET', 'POST'])
def edit_user(user_id):
    edit_user = User.objects.with_id(user_id)
    if edit_user is not None:
        if request.method == 'GET':
            return render_template('edit_user.html', edit_user = edit_user)
        if request.method == 'POST':
            form = request.form
            edit_user = edit_user.update(
                set__fullname = form['fullname'],
                set__yob = form['yob'],
                set__email = form['email']
            )
            return redirect(url_for('admin_user'))
    else:
        return redirect(url_for('admin'))

@app.route('/change_password/<user_id>', methods = ['GET', 'POST'])
def change_password(user_id):
    user_change_password = User.objects.with_id(user_id)
    if user_change_password is not None:
        if request.method == 'GET':
            return render_template ('change_password.html')
        elif request.method == 'POST':
            form = request.form
            current_password = form['current_password']
            new_password = form['new_password']
            password= form['password']
            if current_password == user_change_password['password']:
                if password == new_password:
                    user_change_password = user_change_password.update(
                        set__password = password
                    )
                    return redirect(url_for('login'))
                else:
                    return redirect(url_for('admin'))
            else:
                return redirect(url_for('admin'))
    else:
        return redirect(url_for('admin_user'))

# Sửa thông tin bài viết
@app.route('/delete_article/<article_id>')
def delete_article(article_id):
    delete_article = Article.objects.with_id(article_id)
    if delete_article is not None:
        delete_article.delete()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('admin'))


@app.route('/edit_article/<article_id>', methods =['GET' ,'POST'])
def edit_article(article_id):
    edit_article = Article.objects.with_id(article_id)
    if edit_article is not None:
        if request.method == 'GET':
            return redirect(url_for('edit_article.html', edit_article = edit_article))
        elif request.method == 'POST':
            form = request.form
            edit_article = edit_article.update(
                title = form['title'],
                sapo = form['sapo'],
                thumbnail = form['thumbnail'],
                time = form['time'],
                content = form['content'],
                author = form['author']
            )
            return redirect(url_for('admin_article'))
    else:
        return redirect(url_for('admin'))

@app.route('/article/approval')
def article_approval():
    articles = Article.objects()
    return render_template ('article_approval.html', articles = articles)

@app.route('/article/approve/<article_id>')
def approve_article(article_id):
    approve_article = Article.objects.with_id(article_id)
    if approve_article is not None:
        approve_article = approve_article.update(
            set__level = 1
        )
        return redirect(url_for('article_approval'))
    else:
        return redirect(url_for('article_approval'))

# Phê duyệt người dùng
@app.route('/user/request')
def user_request():
    users= User.objects()
    return render_template ('user_approval.html', users = users)

@app.route('/user/approve/<user_id>')
def approve_user(user_id):
    approve_user = Request.objects.with_id(user_id)
    if approve_user is not None:
        approve_user = approve_user.update(
            set__level = 1,
            set__request = False
        )
        return redirect(url_for('user_request'))
    else:
        return redirect(url_for('user_request'))

        
@app.route('/reject_user/<user_id>')
def reject_user(user_id):
    reject_user = User.objects.with_id(user_id)
    if reject_user is not None:
        reject_user = reject_user.update(
            set__request = False
        )
        return redirect(url_for('user_request'))
    else:
        return redirect(url_for('user_request'))

@app.route('/homepage')
def homepage():
    return render_template("homepage.html")

if __name__ == '__main__':
  app.run(debug=True)