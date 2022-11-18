from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'thicode'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'testedali13@gmail.com',
    "MAIL_PASSWORD": 'eerkehktqkyizlhs'
}

app.config.update(mail_settings)
mail = Mail(app)

class Contato:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["telefone"]
        )

        msg = Message(
            subject = 'Confirmação de e-mail',
            sender = 'testedali13@gmail.com',
            recipients = [formContato.email],
            body = f'''
            Parabéns {formContato.nome} por fazer cadastro com a Dalí.

            
              Seu e-mail foi confirmado.

            '''
        )
        mail.send(msg)
        flash('E-mail de confirmação enviado!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)