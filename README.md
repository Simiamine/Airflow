# Airflow & Spark Integration for Data Pipelines

## Présentation générale

Ce projet vise à orchestrer et exécuter des pipelines de données distribués dans un environnement sécurisé Sanofi. Il combine **Apache Airflow** pour l’orchestration, **Apache Spark** pour le traitement distribué, **Metabase** pour la visualisation, et **MinIO** pour le stockage objet compatible S3. Le déploiement et la gestion locale s’appuient sur **Astro CLI (Astronomer)**, le tout packagé avec **Docker** et **docker-compose**, optimisé pour macOS via **Colima**.

---

## Stack technique

- **Apache Airflow** : Orchestration des workflows et gestion des DAGs.
- **Apache Spark** : Traitement distribué des données.
- **Metabase** : Visualisation et exploration des données.
- **MinIO** : Stockage objet compatible S3, utilisé pour les échanges de fichiers.
- **Astro CLI** : Gestion locale et déploiement des environnements Airflow.
- **Docker & docker-compose** : Conteneurisation et orchestration des services.
- **Colima** : Moteur de virtualisation pour Docker sur macOS.
- **Certificats Sanofi (.pem)** : Sécurisation des communications et conformité.

---

## Installation et configuration locale

### Prérequis

- macOS (recommandé)
- [Colima](https://github.com/abiosoft/colima)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Astro CLI](https://docs.astronomer.io/astro/cli/install-cli)
- Certificats Sanofi : `SanofiRootCA.pem`, `SanofiTechnicalCA.pem`

### Étapes

1. **Installer Colima et Docker Desktop**
    ```bash
    brew install colima
    colima start
    ```

2. **Installer Astro CLI**
    ```bash
    curl -sSL https://install.astronomer.io | sudo bash
    ```

3. **Cloner le projet**
    ```bash
    git clone <repo-url>
    cd airflow-spark-integration
    ```

4. **Placer les certificats Sanofi dans le dossier `certs/`**
    ```
    certs/SanofiRootCA.pem
    certs/SanofiTechnicalCA.pem
    ```

5. **Construire et démarrer les services**
    ```bash
    astro dev start
    ```

6. **Accéder aux interfaces**
    - Airflow : http://localhost:8080
    - Metabase : http://localhost:3000
    - MinIO : http://localhost:9000

---

## Structure du projet

```
airflow-spark-integration/
├── dags/
│   └── stock_market.py
├── plugins/
├── docker-compose.yml
├── Dockerfile
├── certs/
│   ├── SanofiRootCA.pem
│   └── SanofiTechnicalCA.pem
├── .gitignore
├── README.md
└── ...
```

---

## Fonctionnement du pipeline

### Exemple : `stock_market.py`

- **Source** : Extraction des données de marché depuis une API sécurisée.
- **Traitement** : Spark nettoie et agrège les données.
- **Stockage** : Les résultats sont déposés sur MinIO.
- **Visualisation** : Metabase interroge MinIO pour afficher les tableaux de bord.
- **Orchestration** : Airflow gère la planification et le suivi du pipeline.

---

## Commandes principales

- **Build des images Docker**
  ```bash
  astro dev build
  ```
- **Démarrer les services**
  ```bash
  astro dev start
  ```
- **Arrêter les services**
  ```bash
  astro dev stop
  ```
- **Afficher les logs**
  ```bash
  astro dev logs
  ```
- **Accéder au shell Airflow**
  ```bash
  astro dev bash
  ```

---

## Dépannage

- **Erreurs SSL** : Vérifiez la présence et le chemin des certificats `.pem` dans `certs/`.
- **Conflits de ports** : Modifiez les ports dans `docker-compose.yml` si nécessaires.
- **Certificats manquants** : Téléchargez les certificats Sanofi requis ou contactez l’administrateur.

---

## Sécurité et conformité

- **Certificats Sanofi** : Obligatoires pour toute connexion sécurisée.
- **.gitignore** : Les fichiers sensibles (`certs/*.pem`, credentials, etc.) sont ignorés par défaut.
- **Conformité** : Respect des politiques internes Sanofi pour le stockage et le transfert des données.

---

## Contributeurs

- Amine M'ZALI

---

## Licence

Ce projet est sous licence MIT, sauf mention contraire dans des fichiers spécifiques.

---