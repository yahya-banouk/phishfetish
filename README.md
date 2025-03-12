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
- Base de données MySQL installée et configurée

### Configuration de la base de données

1. **Installer MySQL** :

```bash
sudo apt-get update
sudo apt-get install mysql-server
```

2. **Se connecter à MySQL et créer la base de données** :

```sql
CREATE DATABASE phishfetish;
```

3. **Configurer les identifiants de connexion à la base de données** : Le fichier `.env.dev` doit contenir :

```
ENV=dev
DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=admin
DB_NAME=phishfetish
```

> **Remarque:** Vous pouvez adapter ces identifiants à votre configuration en modifiant les variables dans le fichier `.env.dev`.

### Installation de l'application

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

4. **Lancer l'API**

```bash
env ENV=dev python3 -m uvicorn app:app --host 0.0.0.0 --reload
```

> **Remarque :** Cette commande est valable pour les terminaux bash. Si vous utilisez un terminal Windows (PowerShell ou Command Prompt), adaptez la syntaxe comme suit :

```powershell
$env:ENV="dev"; python3 -m uvicorn app:app --host 0.0.0.0 --reload
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

