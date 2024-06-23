from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Varshini@30'
app.config['MYSQL_DB'] = 'recurit'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/get_recurites', methods=['POST'])
def get_recurites():
    skill = request.form['skill']

    cursor = mysql.connection.cursor()
    query = "SELECT * FROM employes WHERE SKILL_SET LIKE %s"
    cursor.execute(query, ('%' + skill + '%',))
    result = cursor.fetchall()

    if result:
        return render_template('index2.html', em=result)
    else:
        return render_template('index2.html', error='No employees found')

if __name__ == '__main__':
    app.run(debug=True)
