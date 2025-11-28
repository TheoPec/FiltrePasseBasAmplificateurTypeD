# 🎧 Projet TC - Conception du filtre de sortie d’un amplificateur numérique (Classe D)

## 🎯 Objectif du projet
Ce projet vise à comprendre et simuler le fonctionnement d’un amplificateur audio **classe D** basé sur une **modulation PWM**, puis à **concevoir le filtre analogique** permettant de restituer le signal audio en sortie.

Le travail est divisé en deux grandes parties :

---

## 🟦 Partie 1 — Simulation de la modulation et de l’amplification

➡ Réalisée sous **Python**

### 🔹 Étapes :
- Génération d’un signal **sinusoïdal** (1 kHz)
- Génération d’une **onde triangulaire** (20 kHz)
- Comparaison → création du **signal PWM**
- Étude de l’influence :
  - de la fréquence d’échantillonnage
  - de l’amplitude et de la fréquence de l’onde triangulaire
- Spectre du signal PWM (FFT)
- Simulation de l’**amplification** du PWM (gain = 100)

🎯 Résultat attendu :  
Le fondamental audio reste présent mais noyé dans les harmoniques → **le filtrage est indispensable**.

---

## 🟩 Partie 2 — Conception du filtre de sortie

➡ Réalisée via **méthodes RCAO + Python**

### 🔹 Objectif du filtre
- **Récupérer le signal audio** avant la conversion PWM
- Couper les composantes à **20 kHz et au-delà**

### 🔹 Spécifications audio retenues :
| Paramètre | Valeur |
|---------|--------|
| Bande utile | 0 – 20 kHz |
| Atténuation max bande utile (Ap) | 0,1 – 1 dB |
| Atténuation min bande coupée (As) | 40 – 60 dB |

### 🔹 Méthodes analysées
- Butterworth
- Chebyshev I
- Cauer / Elliptique

Pour chacune :
- Ordre du filtre
- Fonction de transfert
- Pôles & zéros
- Réponse en fréquence

🎯 Résultat attendu :  
Choix du **modèle optimal** pour les spécifications du projet puis **synthèse RCAO** en cellules de 1er / 2e ordre.

---

## 📁 Contenu du dépôt

| Fichier / Dossier | Description |
|------------------|-------------|
| `/src` | Scripts Python (PWM, FFT, synthèse filtre, etc.) |
| `/img` | Captures et graphes des résultats |
| `/doc` | Rapport + analyses + résultats |
| `README.md` | Ce document 👍 |

---

## ⚙️ Technologies utilisées
- Python 3.10+
- `numpy`, `matplotlib`, `scipy.signal`
- Outil interactif de synthèse RCAO fourni par l’enseignant

---

## 🧑‍💻 Auteurs
- Projet réalisé dans le cadre du cours de **Traitement & Conversion — 2025**
- Licence éducative / reproduction autorisée avec référence

---

## 📌 Conclusion
Le projet démontre qu’un amplificateur classe D est très efficace mais nécessite un **filtre passe-bas performant** pour éliminer les harmoniques de la PWM et obtenir un signal musical propre et fidèle.

---
