# Changelog

Toutes les modifications notables de ce projet sont documentees dans ce fichier.
Les dates correspondent aux timestamps de creation des fichiers originaux.

---

## [v5] - 2026-02-24 21:14 (tkinter-app/main.py)

**Photo Cleaner & Organizer v5 — Filtres de contenu avances**

### Ajouts
- 9 filtres de contenu activables individuellement :
  - Sans personne detectee (visage + corps via Haar cascades)
  - Photo industrielle / technique (saturation faible + densite de bords)
  - Emoticone / sticker / meme
  - Capture d'ecran (ameliore)
  - Document / texte imprime
  - Flou de mouvement directionnel
  - Fichier trop petit (< seuil Ko configurable)
  - Photo de nuit sans sujet
  - Paysage sans personne (optionnel)
- Sidebar scrollable pour accueillir tous les filtres
- Detection de corps entier (`haarcascade_fullbody`, `haarcascade_upperbody`)
- Score d'exposition composite (luminosite + contraste - pixels satures)

### Conserve
- Tous les filtres et fonctionnalites des versions precedentes

---

## [v4b] - 2026-02-24 17:52 (tkinter-app/archive/v4b_strict_copy.py)

**Variante v4 — Detection stricte des copies**

### Ameliorations
- Patterns "copie" separes en deux niveaux : strict (confiance 100%) et normal
- Detection immediate des fichiers nommes "copie", "- copie", "(copie)" etc.
- Signalement prioritaire independant de l'analyse de doublons
- Regex ameliorees pour les conventions de nommage Windows Explorer

---

## [v4] - 2026-02-24 17:44 (tkinter-app/archive/v4_smart_duplicates.py)

**Photo Cleaner & Organizer v4 — Corrections critiques doublons**

### Corrections
- Doublons : garde TOUJOURS la meilleure image (plus nette, plus lourde, nom sans "copie")
- La moins bonne image du groupe va systematiquement dans review

### Ameliorations
- Score de qualite revu : variance brute du Laplacien (plus fiable)
- Heuristique sur le nom de fichier (penalite pour "copie"/"copy"/"(2)")
- Taille fichier integree au score de classement
- Pre-cochage intelligent : seule la moins bonne d'un groupe est cochee

---

## [v3] - 2026-02-24 17:32 (tkinter-app/archive/v3_darkroom.py)

**Photo Cleaner & Organizer v3 — Darkroom & Auto-calibration**

### Ajouts
- Pre-cochage INTELLIGENT : pour deux doublons, seul le moins bon est coche
- Auto-calibration : analyse un echantillon (250 images max) pour adapter les seuils
- `DEF_AUTOCHECK_CONF` : seuil de confiance pour le pre-cochage automatique
- `collections.defaultdict` pour le groupage des doublons

### Interface
- Theme "Darkroom" modernise (inspire Lightroom / DaVinci Resolve)
- `ImageFilter` et `ImageDraw` importes pour effets visuels

---

## [v2] - 2026-02-24 17:19 (tkinter-app/archive/v2_thumbnails.py)

**Photo Cleaner & Organizer v2 — Miniatures & revue manuelle**

### Changement majeur
- L'analyse ne deplace plus rien automatiquement
- Resultats affiches avec miniatures (96x72)
- L'utilisateur coche ce qu'il veut deplacer, puis clique "Deplacer les selectionnes"

### Ajouts
- Detection de visages (`haarcascade_frontalface_default.xml`) pour proteger les portraits
- Score de confiance (0-100) pour chaque probleme detecte
- Seuils ajustables via curseurs dans l'interface
- Score minimal de confiance configurable (`DEFAULT_MIN_CONFIDENCE`)
- Miniatures generees avec Pillow (`ImageTk`)

### Ameliorations
- Seuils par defaut recalibres (blur: 30, dark: 20, bright: 245)
- Passage des commentaires et docstrings en francais

---

## [v1] - 2026-02-24 16:59 (tkinter-app/archive/v1_initial.py)

**Photo Cleanup & Organizer — Version initiale**

### Fonctionnalites
- Detection de doublons exacts (hash perceptuel, distance = 0)
- Detection de quasi-doublons (distance de Hamming <= 8)
- Analyse de qualite : flou (Laplacien), luminosite, uniformite
- Deplacement automatique des fichiers signales vers `review/`
- Interface Tkinter avec theme sombre (#1C1C2E)
- Tableau de resultats (Treeview) avec codes couleur par type de probleme
- Barre de progression
- Bouton pour ouvrir le dossier review (Windows/macOS/Linux)

### Dependances
- Pillow, opencv-python, imagehash, numpy

---

## [PhotoFlow PyQt6] - 2026-03-08 03:07 (pyqt6-app/)

**PhotoFlow — Reecriture PyQt6 modulaire**

### Nouveau projet
- Reecriture complete avec PyQt6 (remplacement de Tkinter)
- Architecture modulaire : `app/main_window.py`, `app/styles/theme_manager.py`
- Support HiDPI natif (`AA_EnableHighDpiScaling`, `AA_UseHighDpiPixmaps`)
- Police Segoe UI, theming centralise
- Point d'entree leger (35 lignes)

### Dependances ajoutees
- PyQt6 >= 6.6.0
- exifread >= 3.0.0
- opencv-python-headless (au lieu de opencv-python)
