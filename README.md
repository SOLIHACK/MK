# Ultimate Network Scanner 🚀

L'**Ultimate Network Scanner** est un outil puissant et polyvalent conçu pour explorer en profondeur un domaine, trouver ses sous-domaines, scanner les ports ouverts, détecter les vulnérabilités, et fournir un rapport détaillé. Inspiré du style rétro "GameBoyColor", il offre une interface interactive et facile à utiliser.

---

## Fonctionnalités 🎯

1. **Exploration de Domaine** :
   - Recherche des sous-domaines associés à un domaine donné.
   - Basé sur un fichier de dictionnaire personnalisable (`subdomains.txt`).

2. **Scan de Ports** :
   - Identification des ports ouverts sur chaque sous-domaine trouvé.
   - Analyse des services associés aux ports (HTTP, FTP, SSH, etc.).

3. **Analyse des Vulnérabilités** :
   - Détection des vulnérabilités connues via l'API Shodan.
   - Identification des configurations faibles ou des services obsolètes.

4. **Rapport Complet** :
   - Génération d'un rapport détaillé au format `.txt` avec :
     - Sous-domaines trouvés.
     - Ports ouverts.
     - Vulnérabilités détectées et suggestions de correction.

5. **Interface Utilisateur Interactive** :
   - Menu interactif stylé avec des couleurs et animations.
   - Inspiré de l'esthétique rétro "GameBoyColor".

---

## Installation 🛠️

### Prérequis
- Python 3.8 ou supérieur
- Clé API Shodan (facultative, mais recommandée pour l'analyse des vulnérabilités)

### Étapes
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/SOLIHACK/ultimate-network-scanner.git
   cd ultimate-network-scanner
   ```

2. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

3. Ajoutez un fichier `subdomains.txt` contenant une liste de sous-domaines potentiels :
   ```plaintext
   www
   api
   mail
   admin
   ```
   Vous pouvez utiliser un fichier de dictionnaire existant pour des résultats plus précis.

---

## Utilisation 🚀

1. Lancez le scanner :
   ```bash
   python main.py
   ```

2. Suivez les instructions dans le terminal :
   - Entrez un domaine à analyser (par exemple, `example.com`).
   - Fournissez votre clé API Shodan (facultatif).
   - Patientez pendant que le scan est effectué.

3. Consultez le rapport généré dans le fichier `scan_results.txt`.

---

## Exemple de Résultat 📝

Voici un exemple de rapport généré :

```plaintext
=== Scan Results ===

Subdomain: www.example.com
Open Ports: 80, 443
Vulnerabilities: CVE-2023-12345, CVE-2024-67890

Subdomain: api.example.com
Open Ports: 8080, 8443
Vulnerabilities: CVE-2023-23456

Subdomain: mail.example.com
Open Ports: 25, 110, 143
Vulnerabilities: None

Subdomain: admin.example.com
Open Ports: 22, 3389
Vulnerabilities: CVE-2022-98765
```

---

## Fonctionnalités Futures 🔮

- Génération de rapports en HTML avec graphiques interactifs.
- Intégration avec d'autres outils comme Nmap et Metasploit.
- Support pour des scans sur des plages d'IP plus larges.

---

## Contribution 🤝

Les contributions sont les bienvenues ! Suivez ces étapes pour contribuer :
1. Forkez ce dépôt.
2. Créez une nouvelle branche :
   ```bash
   git checkout -b feature-nouvelle-fonctionnalité
   ```
3. Effectuez vos modifications et testez-les.
4. Soumettez une Pull Request.

---

## Avertissement ⚠️

Cet outil est conçu pour des **tests d'intrusion légaux** et des **analyses de sécurité** uniquement. L'utilisation non autorisée peut être illégale. L'auteur décline toute responsabilité en cas d'utilisation abusive.

---

## Auteurs ✍️

- **SOLIHACK** - Créateur et développeur principal

---

## Licence 📜

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.
