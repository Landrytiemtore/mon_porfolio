from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
#from dotenv import load_dotenv

# Charger les variables d'environnement
#load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'votre_cle_secrete_ici')

# Configuration email depuis les variables d'environnement
EMAIL_CONFIG = {
    'smtp_server': os.getenv('SMTP_SERVER', 'smtp.gmail.com'),
    'smtp_port': int(os.getenv('SMTP_PORT', 587)),
    'email': os.getenv('EMAIL'),
    'password': os.getenv('EMAIL_PASSWORD')
}

def send_email(name, email, subject, message):
    """Fonction pour envoyer l'email"""
    try:
        # Configuration du message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG['email']
        msg['To'] = EMAIL_CONFIG['email']  # L'email où vous recevrez les messages
        msg['Subject'] = f"Portfolio Contact: {subject}"
        
        # Corps du message
        body = f"""
        Nouveau message de contact depuis votre portfolio:
        
        Nom: {name}
        Email: {email}
        Sujet: {subject}
        
        Message:
        {message}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Connexion au serveur SMTP
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        server.login(EMAIL_CONFIG['email'], EMAIL_CONFIG['password'])
        
        # Envoi de l'email
        text = msg.as_string()
        server.sendmail(EMAIL_CONFIG['email'], EMAIL_CONFIG['email'], text)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Erreur envoi email: {e}")
        return False

@app.route('/')
def index():
    return render_template('portfolio.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        # Récupération des données du formulaire
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        # Validation basique
        if not all([name, email, subject, message]):
            flash('Veuillez remplir tous les champs du formulaire.', 'error')
            return redirect(url_for('index') + '#contact')
        
        # Envoi de l'email
        if send_email(name, email, subject, message):
            flash('Votre message a été envoyé avec succès ! Je vous répondrai rapidement.', 'success')
        else:
            flash('Une erreur est survenue lors de l\'envoi du message. Veuillez réessayer.', 'error')
        
        return redirect(url_for('index') + '#contact')

#if __name__ == '__main__':
#    app.run(debug=True)