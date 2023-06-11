from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL database connection configuration
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inscription'

# Initialize MySQL
mysql = MySQL(app)

# Route for displaying the HTML form
@app.route('/')
def index():
    return render_template('inscription.html')

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit():
    nom = request.form['nom']
    prenom = request.form['prenom']
    adresse = request.form['adresse']
    numtel = request.form['numtel']
    datenai = request.form['datenai']
    pays = request.form['pays']

    # Connect to the database
    conn = mysql.connection
    cursor = conn.cursor()

    # Insert the form data into the database
    query = "INSERT INTO condidat (nom, prenom, adresse, numtel, datenai, pays) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (nom, prenom, adresse, numtel, datenai, pays)
    cursor.execute(query, values)
    conn.commit()

    # Close the database connection
    cursor.close()

    flash('Data inserted successfully!')
    return 'Data inserted successfully!'

if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.run(debug=True)