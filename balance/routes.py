from balance import app


@app.route("/")
def inicio():
    return "Bienvenido a la aplicación de balance"