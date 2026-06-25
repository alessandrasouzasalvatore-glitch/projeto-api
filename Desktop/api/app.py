from flask import Flask, render_template, request, redirect

app = Flask(__name__)

dados = [
    {
        "id": 1,
        "nome": "Roberto Oliveira",
        "email": "roberto.web10@gmail.com",
        "telefone": "51991941810"
    },
    {
        "id": 2,
        "nome": "Carlos da Silva",
        "email": "carlos@gmail.com",
        "telefone": "51 999999999"
    },
    {
        "id": 3,
        "nome": "Vitor",
        "email": "vi@gmail.com",
        "telefone": "51 89898989"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        novo_usuario = {
            "id": len(dados) + 1,
            "nome": request.form["nome"],
            "email": request.form["email"],
            "telefone": request.form["telefone"]
        }

        dados.append(novo_usuario)
        return redirect("/")

    return render_template("index.html", dados=dados)

if __name__ == "__main__":
    app.run(debug=True)