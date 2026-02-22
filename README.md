# 🛡️ Détecteur d'Intrusion Réseau par IA

Projet réalisé dans un cadre d'apprentissage et de manière autonome

## 🎯 Objectif
Détecter automatiquement les cyberattaques réseau 
(Nmap, DoS) à l'aide du Machine Learning.

## 🏗️ Architecture du projet
```
Labo virtuel (VirtualBox)
    ↓ Capture trafic (tcpdump)
Fichiers .pcap
    ↓ Conversion (Python/pyshark)
Dataset CSV (3,1M paquets labellisés)
    ↓ Entraînement (scikit-learn)
Random Forest → 99.90% de précision
```

## 🛠️ Technologies utilisées
- **Virtualisation** : VirtualBox, Kali Linux, Ubuntu Server
- **Capture réseau** : tcpdump, pyshark
- **Machine Learning** : Python, scikit-learn, Random Forest
- **Visualisation** : matplotlib, seaborn

## 📊 Résultats
| Métrique | Valeur |
|----------|--------|
| Précision globale | 99.90% |
| Paquets analysés | 3 147 059 |
| DoS détecté | 100% |
| Faux négatifs | 0 |

## 🚀 Tester le modèle en direct
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/abderemaneattoumani/ids-reseau-ia/blob/main/colab_demo.ipynb)

## 📁 Structure du projet
```
ids-reseau-ia/
├── ids_model.ipynb      # Notebook complet
├── colab_demo.ipynb     # Démo interactive
├── pcap_to_csv.py       # Convertisseur pcap→csv
├── Datasets/
│   └── dataset_sample.csv
└── Docs/
    └── resultats_ids.png
```
