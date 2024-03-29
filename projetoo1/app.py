from flask import Flask, request
from funcoes import sigla, ordenar_cidades

# Instanciar a aplicação
app = Flask(__name__)

@app.route("/consulta_ibge", methods=['GET'])  #contruindo uma rota com os metodos permitido
def estado(): 
    UF = request.args.get('UF')
    resposta = sigla(UF)
    return resposta

@app.route("/ordenar_cidades", methods=['GET'])
def ordenar():
    UF = request.args.get('UF')
    cidades = estado()  # Obtém os distritos do estado
    cidades_ordenadas = ordenar_cidades(cidades)  # Ordena as cidades
    return {f"cidades_ordenadas de {UF}": cidades_ordenadas}

if __name__ == "__main__":
    app.run(debug=True)
