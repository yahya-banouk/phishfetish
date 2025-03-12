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

- **Installer MySQL** et créer une base de données nommée `phishfetish` :
  ```bash
  mysql -u root -p
  CREATE DATABASE phishfetish;
  ```
- **Installer Python 3.8+**
- `pip` et `virtualenv` (optionnel mais recommandé)
- Configurer la base de données MySQL avec les informations suivantes :
  ```
  ENV=dev

  # .env.dev pour le développement local
  DB_HOST=localhost
  DB_USER=admin
  DB_PASSWORD=admin
  DB_NAME=phishfetish
  ```
  **Vous pouvez modifier ces informations dans le fichier ****`.env.dev`**** pour qu'elles correspondent à votre configuration MySQL.**

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
   L'application utilise SQLAlchemy avec une base de données MySQL. Assurez-vous que votre base de données `phishfetish` est bien créée et accessible avec les informations fournies ci-dessus.

5. **Lancer l'API**

```bash
    env ENV=dev python3 -m uvicorn app:app --host 0.0.0.0 --reload
```

⚠️ **Note :** Cette commande peut varier en fonction du terminal utilisé. Assurez-vous que l'environnement virtuel est activé et que les variables d'environnement sont bien configurées.

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

