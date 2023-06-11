#html code :
<!DOCTYPE html>
<html>
<head>
    <title>Candidat</title>
    <style>
        .i {
            text-align: center;
            font-size: 40px;
            color: rgb(215, 24, 6);
        }
        .a {
            padding: 5px 20px 5px 5px;
            margin-left: 30px;
            display: inline-block;
            width: 200px;
            margin-bottom: 30px;
            background-color:	#FFC0CB;
        }
        .im {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
            margin-left:200px;
        }

        .im img {
            width: 100px;
            height: 60px;
        }

        .v {
            display: inline-block;
            padding: 10px 20px;
            background-color: rgb(215, 24, 6);
            color: #2cf919;
            border: 2px solid #555;
            border-radius: 5px;
            text-decoration: none;
            transition: color 0.3s ease;
            margin-left: 10px;
            border-color: rgb(215, 24, 6);
            cursor:pointer;
        }

        .v:hover {
            background-color: #45a049;
            color: red;
            border-color: #45a049;
        }

        body {
            background-color :rgba(255, 0, 0, 0.2);
        }
    </style>
</head>
<body>
    <div>
        <p class="i">Inscription</p>
    </div>
    <!-- Form elements -->
    <div>
        <label for="nom">Nom:</label>
        <input type="text" id="nom" name="nom" class="a">
    </div>
    <div>
        <label for="prenom">Prenom:</label>
        <input type="text" id="prenom"  name="prenom" class="a">
    </div>
    <div>
        <label for="adresse">adresse:</label>
        <input type="text" id="adresse"  name="adresse" placeholder="Enter your address" class="a">
    </div>
    <div>
        <label class="numtel" for="numtel">num_téléphone:</label>
        <input type="text" id="numtel" name="numtel" class="a" pattern="\d{1,8}" min="0" max="99999999" maxlength="8">
    </div>
    <div class="datenai">
        <label for="datenai">date de naissance:</label>
        <input type="date" id="datenai"  name="datenai" class="a">
    </div>
    <div>
        <label for="pays">Pays :</label>
        <select id="pays" name="pays" class="a">
            <option value="tunisie">Tunisie</option>
            <option value="france">France</option>
            <option value="usa">USA</option>
            <option value="turky">turky</option>
            <option value="japan">japan</option>
            <option value="corée du sud">corée du sud</option>
            <option value="corée du nord">corée du nord</option>
            <option value="pakistan">pakistan</option>
            <option value="india">india</option>
        </select>
    </div>
    <div class="im">
        <img src="https://media.istockphoto.com/id/930420146/vector/finger-icon.jpg?s=612x612&w=0&k=20&c=Xgh2shu_aBqFNJPQkN_ShZVOUHEPYUOoGnnB126OsFA=" alt="My Image">
        <button class="v" onclick="submitForm()">Submit</button>
    </div>
    <script> 
        const audio = new Audio("https://www.fesliyanstudios.com/play-mp3/387");
        const button = document.querySelector(".v");
        button.addEventListener("click", () => {
            audio.play();
        });
    </script>
    <script>
        function submitForm() {
            var nom = document.getElementById('nom').value;
            var prenom = document.getElementById('prenom').value;
            var adresse = document.getElementById('adresse').value;
            var numtel = document.getElementById('numtel').value;
            var datenai = document.getElementById('datenai').value;
            var pays = document.getElementById('pays').value;

            var formData = new FormData();
            formData.append('nom', nom);
            formData.append('prenom', prenom);
            formData.append('adresse', adresse);
            formData.append('numtel', numtel);
            formData.append('datenai', datenai);
            formData.append('pays', pays);

            fetch('/submit', {
                method: 'POST',
                body: formData
            })
                .then(response => {
                    if (response.ok) {
                        console.log('Data inserted successfully!');
                        // Reset the form fields to empty values
                        document.getElementById('nom').value = '';
                        document.getElementById('prenom').value = '';
                        document.getElementById('adresse').value = '';
                        document.getElementById('numtel').value = '';
                        document.getElementById('datenai').value = '';
                        document.getElementById('pays').value = 'tunisie'; // Reset the dropdown to its default value
                    } else {
                        console.log('Error inserting data.');
                    }
                })
                .catch(error => {
                    console.log('Error:', error);
                });
        }
    </script>
</body>
</html>
#python code :
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
 #mysql code 
 create database inscription;
CREATE TABLE condidat (
    nom VARCHAR(30),
    prenom VARCHAR(30),
    datenai DATE,
    adresse VARCHAR(30),
    numtel INT(10),
    pays CHAR(15)
);
select * from condidat;
