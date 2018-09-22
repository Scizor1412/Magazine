from flask import *
import mlab
from models.db_user import User
from models.db_article import Article
app = Flask(__name__)

mlab.connect()

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
    users = User.objects()
    return render_template('admin.html', users = users)

if __name__ == '__main__':
  app.run(debug=True)