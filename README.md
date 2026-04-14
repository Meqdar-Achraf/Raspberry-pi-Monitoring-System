# Raspberry-pi-Monitoring-System

Système de surveillance Raspberry Pi

📌 Aperçu

Le système de surveillance Raspberry Pi est un projet IoT compact conçu pour détecter le mouvement et la présence d’eau à l’aide d’un Raspberry Pi 4 connecté à des capteurs.
Ce système améliore la sécurité en surveillant les conditions environnementales en temps réel.

Le Raspberry Pi est accessible à distance via SSH en utilisant PuTTY, où un script Python basé sur la bibliothèque "gpiozero" contrôle et lit les données des capteurs.

🎯 Objectifs du projet

Détecter le mouvement à l’aide d’un capteur PIR (HC-SR501).

Détecter la présence d’eau à l’aide d’un capteur de niveau d’eau (HW-038).

Permettre la surveillance et l’exécution à distance via SSH.

Fournir une solution IoT simple et efficace pour la surveillance.

🧰 Matériel requis

Raspberry Pi 4

Capteur de mouvement PIR (HC-SR501)

Capteur de niveau d’eau (HW-038)

Fils de connexion (jumper wires)

Carte MicroSD (ou clé USB) avec Raspberry Pi OS

💻 Logiciels requis

Raspberry Pi OS
Python 3
Bibliothèque gpiozero
PuTTY (pour l’accès SSH)

Installer la bibliothèque requise avec : ⚠⚠⚠
### Bash
```markdown
sudo apt update
sudo apt install python3-gpiozero -y
```

📘 Guide de câblage.

Capteur PIR (HC-SR501).
- VCC → 5V (Pin 2).
- GND → Masse (Pin 6).
- OUT → GPIO17 (Pin 11).

Capteur de niveau d’eau (HW-038).
- VCC → 3.3V (Pin 1).
- GND → Masse (Pin 9).
- DO → GPIO27 (Pin 13).

🛠 Installation & Configuration
- Intallation de Raspberry PI OS via le programme raspberry pi imager sur un support de stockage
- Insertion du support dans raspberry pi
- Acceder au raspberry pi via SSH (PUTTY)
- Installer la bibliothèque requise ⬆⬆
- Ajouter les fichier (PIR-HC-SR.py & Water-sensor-HW-038)
- Ajouter le droit d'execution aux fichier :
### Bash
```markdown
sudo chmod PIR-HC-SR.py
sudo chmod Water-sensor-HW-038
```
- Execurion des fichier
### Bash
```markdown
python3 PIR-HC-SR.py
```
```markdown
python3 Water-sensor-HW-038
```
