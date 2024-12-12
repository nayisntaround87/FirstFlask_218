from flask import Flask, request, render_template

app = Flask(__name__)

# Route untuk menampilkan halaman HTML
@app.route("/")
def index():
    return render_template("index.html")

# Route dengan metode POST
@app.route("/submit", methods=["POST"])
def submit():
    # Mengambil data dari form
    text = request.form.get("textfield")
    return f"Anda mengirimkan: {text}"

if __name__ == "__main__":
    app.run(debug=True)
