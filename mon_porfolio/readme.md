# Portfolio Personnel - Landry Tiemtoré

## À propos

Portfolio professionnel de **Landry Tiemtoré**, développeur web full-stack. Ce site présente mes projets récents, mes compétences techniques et permet aux visiteurs de me contacter directement via un formulaire fonctionnel.

## Fonctionnalités

- **Design moderne et responsive** : Adapté à tous les appareils
- **Formulaire de contact fonctionnel** : Envoi d'emails en temps réel
- **Section projets** : Présentation de mes réalisations
- **Système de notifications** : Messages de confirmation/erreur
- **Intégration réseaux sociaux** : Liens vers mes profils professionnels

## Technologies utilisées

- **Backend** : Python avec Flask
- **Frontend** : HTML5, CSS3, JavaScript
- **Email** : SMTP avec authentification
- **Icônes** : Font Awesome 6.4.0
- **Hébergement** : Compatible avec tous les services (PythonAnywhere, Heroku, etc.)

## Prérequis

Avant de commencer, assurez-vous d'avoir :

- Python 3.8 ou supérieur
- Pip (gestionnaire de paquets Python)
- Un compte email pour l'envoi de messages

## Installation

### 1. Cloner le projet
```bash
git clone https://github.com/votre-username/portfolio-landry.git
cd portfolio-landry
```

### 2. Créer un environnement virtuel
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# MacOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install flask python-dotenv
```

### 4. Configuration des variables d'environnement

Créer un fichier `.env` à la racine du projet :

```env
# Fichier .env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL=votre-email@gmail.com
EMAIL_PASSWORD=votre-mot-de-passe-application
SECRET_KEY=votre-cle-secrete-ici
```

### 5. Configuration de l'email Gmail

Pour utiliser Gmail comme service SMTP :

1. **Activer la validation en 2 étapes** sur votre compte Google
2. **Générer un mot de passe d'application** :
   - Allez dans [Sécurité Google](https://myaccount.google.com/security)
   - Sous "Connexion à Google" → "Validation en 2 étapes" → Activer
   - Retournez à "Sécurité" → "Mots de passe d'application"
   - Créez un nouveau mot de passe pour "Application personnalisée"
   - Nommez-le "Portfolio Contact Form"
   - Copiez le mot de passe généré (16 caractères)

3. **Mettre à jour le fichier `.env`** :
   ```
   EMAIL=votre-email@gmail.com
   EMAIL_PASSWORD=le-mot-de-passe-généré-ici
   ```

### Alternative : Autres services email

Pour **Outlook/Office 365** :
```env
SMTP_SERVER=smtp.office365.com
SMTP_PORT=587
```

Pour **Yahoo Mail** :
```env
SMTP_SERVER=smtp.mail.yahoo.com
SMTP_PORT=587
```

## Lancement de l'application

### Mode développement
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- slide -->


```bash
python app.py
```
L'application sera accessible à l'adresse : [http://localhost:5000](http://localhost:5000)

### Mode production
```bash
# Pour Windows
set FLASK_ENV=production
python app.py

# Pour MacOS/Linux
export FLASK_ENV=production
python app.py
```

## Structure du projet

```
portfolio-landry/
├── app.py                    # Application Flask principale
├── .env                      # Variables d'environnement (à créer)
├── .gitignore                # Fichiers ignorés par Git
├── requirements.txt          # Dépendances Python
├── README.md                 # Documentation (ce fichier)
├── templates/
│   └── index.html           # Template HTML principal
└── static/
    ├── css/
    │   └── portfolio.css    # Feuille de style principale
    └── images/
        ├── picOO1.png       # Photo de profil
        ├── pic01.jpg        # Images des projets
        └── ...              # Autres images
```

## Sécurité

### Fichier `.gitignore`
Assurez-vous que le fichier `.gitignore` contient :
```gitignore
# Fichiers sensibles
.env
__pycache__/
*.pyc
venv/
```

### Clé secrète
Générez une clé secrète sécurisée :
```python
import secrets
print(secrets.token_hex(32))
```

## Déploiement

### Sur PythonAnywhere
1. Créez un compte sur [PythonAnywhere](https://www.pythonanywhere.com)
2. Téléversez vos fichiers
3. Configurez l'application web
4. Ajoutez les variables d'environnement dans la console
5. Redémarrez l'application

### Sur Heroku
```bash
# Créer un fichier Procfile
echo "web: gunicorn app:app" > Procfile

# Créer un fichier runtime.txt
echo "python-3.9.0" > runtime.txt

# Déployer
heroku create portfolio-landry
git push heroku main
```

## Sections du site

### 1. Accueil
- Photo de profil
- Présentation personnelle
- Boutons d'action

### 2. Projets
- Grille de projets (6 projets)
- Images descriptives
- Descriptions courtes

### 3. Contact
- Formulaire de contact fonctionnel
- Validation en temps réel
- Messages de confirmation
- Protection contre les spams

### 4. Footer
- Liens vers réseaux sociaux
- Informations de copyright

## Dépannage

### Problèmes courants

1. **Erreur d'authentification SMTP**
   ```
   Solution : Vérifiez votre mot de passe d'application
   ```

2. **Messages non envoyés**
   ```
   Solution : Vérifiez les ports SMTP (587 pour TLS)
   ```

3. **Erreur "Connection refused"**
   ```
   Solution : Vérifiez votre connexion internet et les paramètres du pare-feu
   ```

4. **Images non chargées**
   ```
   Solution : Vérifiez les chemins dans le fichier HTML
   ```

### Journalisation
Les erreurs sont affichées dans la console Flask :
```bash
# Activer le mode debug
app.run(debug=True)
```

## Améliorations futures

- [ ] Ajout d'une base de données pour sauvegarder les messages
- [ ] Section blog intégrée
- [ ] Téléchargement direct du CV
- [ ] Mode sombre/clair
- [ ] Multilangue (Français/Anglais)
- [ ] Analytics intégré

## Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet
2. Créez une branche (`git checkout -b feature/Amelioration`)
3. Commitez vos changements (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`)
4. Pushez vers la branche (`git push origin feature/Amelioration`)
5. Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Auteur

**Landry Tiemtoré**
- Email : emmanuellandrytiemtore@gmail.com
- LinkedIn : [Landry Tiemtoré](https://linkedin.com/in/landrytiemtore)
- GitHub : [@landrytiemtore](https://github.com/landrytiemtore)

## Remerciements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Font Awesome](https://fontawesome.com/)
- [Python SMTP](https://docs.python.org/3/library/smtplib.html)
- Tous les contributeurs et testeurs

---

**Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile sur GitHub !** ⭐

## Support

Pour toute question ou problème :
- Ouvrez une [issue](https://github.com/LandryTiemtore/portfolio-landry/issues)
- Contactez-moi par email : emmanuellandrytiemtore@gmail.com

**Dernière mise à jour :** Décembre 2023

---

*Ce portfolio est constamment mis à jour avec de nouveaux projets et fonctionnalités. Revenez régulièrement pour voir les nouveautés !*