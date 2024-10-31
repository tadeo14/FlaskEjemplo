from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#creamos otra ruta
@app.route("/contacto")
def contactar():
    return "<p>Esta es la seccion de contacto</p>"


app.run()