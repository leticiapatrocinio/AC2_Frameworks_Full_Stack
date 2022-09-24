import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'produtos'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('cadastro_produto.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastrar():
    produto=request.form['produto']
    preco=request.form['preco']
    categoria=request.form['categoria']

    if produto and preco and categoria:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert tbl_produtos (nome_produto, preco_produto, categoria_produto) VALUES (%s, %s, %s)', (produto, preco, categoria))
        conn.commit()
    return render_template('cadastro_produto.html')

@app.route('/produtos', methods=['POST', 'GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select (nome_produto, preco_produto, categoria_produto from tbl_produtos')
  data = cursor.fetchall()
  conn.commit()
  return render_template('listagem_produto.html', dados=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)


