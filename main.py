# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datos_cliente.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creación de una base de datos
db = SQLAlchemy(app)
class Datos(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(10),nullable=False)
    comentario=db.Column(db.String(70),nullable=False)
    
    def __repr__(self):
        return f'<Datos {self.id}>'
# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get("button_discord")
    button_db = request.form.get("button_db")
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_db=button_db)

@app.route("/form_datos",methods=["POST"])
def datos():
    email = request.form.get("email")
    text = request.form.get("text")
    mis_datos = Datos(email=email,comentario=text)
    db.session.add(mis_datos)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5010)
