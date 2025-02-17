# Phishing Detector API

## Description
Phishing Detector API est une application basée sur FastAPI qui permet d'identifier les tentatives de phishing en utilisant une base de données de contenu connu ainsi qu'un modèle d'analyse sémantique basé sur `sentence-transformers`. L'application propose également une analyse IA de phishing lorsque le contenu n'est pas trouvé dans la base de données.

## Fonctionnalités
- Vérification du contenu pour identifier des tentatives de phishing connues
- Analyse IA du contenu si aucune correspondance n'est trouvée
- Ajout manuel de nouvelles entrées de phishing à la base de données
- API REST avec FastAPI

## Installation

### Prérequis
- Python 3.8+
- `pip` et `virtualenv` (optionnel mais recommandé)
- Base de données MySQL configurée avec les informations suivantes :
  ```
  ENV=dev
  
  # .env pour le développement local
  DB_HOST=localhost
  DB_USER=root
  DB_PASSWORD="Ybmiola99."
  DB_NAME=phishfetish
  ```
  **Assurez-vous d'avoir une base de données nommée `phishfetish` avant de démarrer l'application.**

### Étapes d'installation

1. **Cloner le dépôt**
```bash
    git clone https://github.com/votre-repo/phishing-detector.git
    cd phishing-detector
```

2. **Créer un environnement virtuel (optionnel mais recommandé)**
```bash
    python3 -m venv venv
    source venv/bin/activate  # Sur MacOS/Linux
    venv\Scripts\activate  # Sur Windows
```

3. **Installer les dépendances**
```bash
    pip install -r requirements.txt
```

4. **Configurer la base de données**
L'application utilise SQLAlchemy avec une base de données MySQL. Assurez-vous que votre base de données est bien configurée et accessible avec les informations fournies ci-dessus.

5. **Lancer l'API**
```bash
    env ENV=dev python3 -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
L'API sera accessible sur `http://0.0.0.0:8000`

## Utilisation

### Vérifier si un contenu est du phishing
**Endpoint:**
```
POST /check-phishing/
```
**Exemple de requête:**
```json
{
    "content": "Votre compte a été compromis. Veuillez réinitialiser votre mot de passe immédiatement."
}
```
**Réponse possible:**
```json
{
    "found_in_db": true,
    "is_phishing": true,
    "message": "⚠️ This is a known phishing attempt! (Similarity: 0.85)"
}
```

### Ajouter une nouvelle entrée de phishing
**Endpoint:**
```
POST /add-phishing/
```
**Exemple de requête:**
```json
{
    "content": "Cliquez ici pour gagner un iPhone gratuit!",
    "is_phishing": true
}
```
**Réponse:**
```json
{
    "message": "Content added successfully!"
}
```

## Développement et contribution
- Forkez le projet
- Créez une branche feature (`git checkout -b feature-nouvelle-fonction`)
- Committez vos modifications (`git commit -am 'Ajout d'une nouvelle fonctionnalité'`)
- Poussez la branche (`git push origin feature-nouvelle-fonction`)
- Ouvrez une pull request

