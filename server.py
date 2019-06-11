from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route("/")
def index():
    mysql = connectToMySQL('animals')
    pets = mysql.query_db('SELECT * FROM pets;')
    # print(pets)
    return render_template("index.html", all_pets = pets)

@app.route("/create_pet", methods=["POST"])
def add_pet_to_db():
    # mysql = connectToMySQL("pets")
    print(request.form)
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(nm)s, %(ty)s, NOW(), NOW());"

    data = {
        "nm": request.form["names"],
        "ty": request.form["types"]
    }
    db = connectToMySQL('animals')
    db.query_db(query, data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

