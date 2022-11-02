# Importar a classe Flask, objeto request e o objeto jsonify:
from tokenize import Double
from flask import Flask, request, jsonify

# Criar o objeto Flask app:
app = Flask(__name__)


# atividade 20
produtos = [{'nome': 'sapato', 'preco': 128.55},
            {'nome': 'camisa', 'preco': 49.89},
            {'nome': 'calça', 'preco': 89.99},
            {'nome': 'bermuda', 'preco': 78.63}]

camisas = [{'tamanho': 'p','preco':10},
           {'tamanho': 'm','preco':12},
           {'tamanho': 'g','preco':15}]

trabalho = [{'hora': 'normal','valor': 40},
            {'hora': 'extra','valor': 50}]

# http://127.0.0.1:5000/produtos
@app.route('/produtos', methods=['GET'])
def retornar_todos_os_produtos():
    resp = produtos
    if 'X-nome-produto' in request.headers:
        nome = request.headers['X-nome-produto']
        for produto in produtos:
            if produto['nome'] == nome:
                resp = produto
    return jsonify(resp)

# http://127.0.0.1:5000/produtos/camisas
@app.route('/produtos/camisas', methods=['GET'])
def calculo_camisas():
    if 'p' in request.headers:
        p = int(request.headers['p'])
    if 'm' in request.headers:
        m = int(request.headers['m'])
    if 'g' in request.headers:
        g = int(request.headers['g'])
    
    total = 0
    camisa = camisas
    for camisa in camisas:
        if camisa['tamanho']=='p':
            total=total+((camisa['preco'])*p)
        if camisa['tamanho']=='m':
            total=total+((camisa['preco'])*m)
        if camisa['tamanho']=='g':
            total=total+((camisa['preco'])*g)

    return jsonify(total)

# http://127.0.0.1:5000/empresa/salario
@app.route('/empresa/salario', methods=['GET'])
def calculo_salario():
    if 'hora_normal' in request.headers:
        normal = float(request.headers['hora_normal'])
    if 'hora_extra' in request.headers:
        extra = float(request.headers['hora_extra'])

    total = 0
    trabalhados=trabalho
    for trabalhados in trabalho:
        if trabalhados['hora']=='normal':
            total=total+(trabalhados['valor']*normal)
        if trabalhados['hora']=='extra':
            total=total+(trabalhados['valor']*extra)
    
    total=total*0.9
    return jsonify(total)

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug=True, port=5000)
