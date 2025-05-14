# MK - Ultimate Network Scanner 🚀

**MK** est un outil puissant et polyvalent conçu pour explorer en profondeur un domaine. Il permet de :
- Découvrir les sous-domaines associés.
- Scanner tous les ports ouverts (sur les domaines et sous-domaines).
- Identifier les vulnérabilités Internet connues.
- Générer un rapport complet pour analyser et corriger les failles trouvées.

Avec un style rétro inspiré de la "GameBoyColor", **MK** offre une interface utilisateur interactive et élégante pour une expérience inégalée.

---

## Fonctionnalités Principales 🎯

1. **Recherche de Sous-Domaines** :
   - Identification des sous-domaines actifs en utilisant des techniques avancées de reconnaissance DNS.
   - Basé sur un fichier de dictionnaire personnalisable (`subdomains.txt`).

2. **Scan de Ports** :
   - Scan de tous les ports ouverts (par défaut ou personnalisés).
   - Détection des services associés aux ports ouverts (HTTP, FTP, SSH, etc.).

3. **Analyse des Vulnérabilités** :
   - Intégration avec l'API Shodan pour détecter les vulnérabilités connues.
   - Identification des configurations faibles ou des services obsolètes.

4. **Rapport Complet** :
   - Génération d'un rapport détaillé en `.txt` avec :
     - Les sous-domaines trouvés.
     - Les ports ouverts.
     - Les vulnérabilités détectées et des recommandations pour les corriger.

5. **Interface Utilisateur Interactive** :
   - Menu interactif stylé avec animations.
   - Inspiré de l'esthétique rétro "GameBoyColor".

---

## Installation 🛠️

### Prérequis
- **Python** : Version 3.8 ou supérieure.
- **Bibliothèques Python** : Installez-les via le fichier `requirements.txt`.
- **Clé API Shodan** (facultative, mais recommandée pour l'analyse des vulnérabilités).

### Étapes à Suivre
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/SOLIHACK/MK.git
   cd MK
   ```

2. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

3. Ajoutez un fichier `subdomains.txt` :
   - Ce fichier doit contenir une liste de sous-domaines potentiels (une ligne par sous-domaine).
   - Exemple :
     ```plaintext
     www
     api
     mail
     admin
     ```

---

## Utilisation 🚀

1. Lancez **MK** :
   ```bash
   python main.py
   ```

2. Suivez les instructions dans le terminal :
   - Entrez un domaine cible (par exemple, `example.com`).
   - Fournissez votre clé API Shodan (facultatif).
   - Patientez pendant que le scan est en cours.

3. Consultez le rapport généré dans le fichier `scan_results.txt`.

---

## Exemple de Résultat 📝

Voici un exemple de rapport généré par **MK** :

```plaintext
=== Rapport de Scan Avancé ===

Date du Scan : 2025-05-14
Domaine Analysé : example.com
Durée Totale du Scan : 12 minutes 34 secondes

---

# 1. Sous-domaines Découverts :
- www.example.com (Adresse IP : 192.168.1.1)
- api.example.com (Adresse IP : 192.168.1.2)
- mail.example.com (Adresse IP : 192.168.1.3)
- admin.example.com (Adresse IP : 192.168.1.4)

---

# 2. Ports Ouverts et Services :
## Sous-domaine : www.example.com
- Port 80  : HTTP (Serveur Web)
- Port 443 : HTTPS (Serveur Web Securisé)

## Sous-domaine : api.example.com
- Port 8080 : HTTP (API Endpoint)
- Port 8443 : HTTPS (API Endpoint Securisé)

## Sous-domaine : mail.example.com
- Port 25   : SMTP (Serveur Mail)
- Port 110  : POP3 (Serveur Mail)
- Port 143  : IMAP (Serveur Mail)

## Sous-domaine : admin.example.com
- Port 22   : SSH (Accès Administratif)
- Port 3389 : RDP (Bureau à Distance)

---

# 3. Vulnérabilités Détectées :
## Sous-domaine : www.example.com
- CVE-2023-12345 : Vulnérabilité critique dans le serveur web Apache (Version Obsolète).
  -> Solution : Mettre à jour Apache à la version 2.4.57.

## Sous-domaine : api.example.com
- CVE-2024-67890 : Mauvaise configuration CORS (Cross-Origin Resource Sharing).
  -> Solution : Restreindre les domaines autorisés dans la configuration du serveur.

## Sous-domaine : mail.example.com
- Aucune vulnérabilité majeure détectée.

## Sous-domaine : admin.example.com
- CVE-2022-98765 : Mot de passe SSH faible détecté via brute force.
  -> Solution : Changer le mot de passe SSH et activer l'authentification par clé publique.

---

# 4. Recommandations Générales :
1. Vérifiez que tous les sous-domaines inutilisés sont désactivés ou supprimés.
2. Mettez à jour tous les logiciels obsolètes pour éviter les vulnérabilités connues.
3. Activez un pare-feu pour restreindre l'accès aux ports non nécessaires.
4. Effectuez des audits réguliers pour identifier les nouvelles failles.

---

# 5. Résumé Global :
- Sous-domaines trouvés : 4
- Ports ouverts trouvés : 11
- Vulnérabilités détectées : 3

Rapport généré automatiquement par l'outil MK.
```

---

## Fonctionnalités Futures 🔮

- Génération de rapports interactifs au format HTML.
- Intégration avec d'autres outils de sécurité comme **Nmap** et **Metasploit**.
- Support pour des scans sur des plages d'IP complètes.

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

**MK** est conçu pour des **tests d'intrusion légaux** et des **analyses de sécurité** uniquement. Toute utilisation non autorisée peut être illégale. L'auteur décline toute responsabilité en cas d'utilisation abusive.

---

## Auteur ✍️

- **SOLIHACK** - Créateur et développeur principal

---

## Licence 📜

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.
