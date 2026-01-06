from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/contacto")
def contacto():
    nombre = request.form.get("nombre", "").strip()
    telefono = request.form.get("telefono", "").strip()
    mensaje = request.form.get("mensaje", "").strip()

    # Por ahora: solo verificar que llega (en consola)
    print("Nuevo contacto:", {"nombre": nombre, "telefono": telefono, "mensaje": mensaje})

    # Luego podemos: guardar en DB, enviar email, enviar a WhatsApp API, etc.
    return redirect(url_for("home") + "#contacto")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
