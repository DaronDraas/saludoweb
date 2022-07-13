from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return '¡Hola Mundo!'
@app.route('/say/<string:nombre>')
def ruta(nombre):
    return render_template("index.html",nombre=nombre)
@app.route('/ruta')
def saludo():
    return render_template("index.html")
@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output
      # Devuelve la cadena '¡Hola Mundo!' como respuesta
if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)   