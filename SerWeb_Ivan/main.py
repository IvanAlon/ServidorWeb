from flask import Flask, render_template
import platform, os, socket, subprocess

app = Flask(__name__)
mensaje=[]


@app.route("/")
def index():
    return render_template('index.html',mensaje=['Opciones del Sistema',''])

@app.route("/<parametro>")
def mostrar(parametro):
    if parametro=="IP":
        return render_template('index.html', mensaje=['Mostrar IP', socket.gethostbyname(socket.gethostname)])
    elif parametro=="nombre":
        return render_template('index.html', mensaje=['Nombre del Equipo', socket.gethostname()])
    elif parametro=="reinicio":
        return render_template('index.html', mensaje=['Reiniciar Equipo', subprocess.run("shutdown -r")])
    else:
        return render_template('index.html',mensaje=['Error','Parámetro no válido, haz clic en el menú superior'])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)