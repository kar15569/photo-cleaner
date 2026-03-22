# Architecture du projet

## Vue d'ensemble

Le projet Photo Cleaner & Organizer est compose de deux applications independantes qui partagent la meme logique d'analyse d'images, mais avec des interfaces et architectures differentes.

## 1. Version Tkinter (tkinter-app/)

### Architecture mono-fichier

Toute l'application est contenue dans un seul fichier `main.py` (1335 lignes). Ce choix a ete fait pour faciliter la distribution et l'utilisation immediate sans installation complexe.

### Organisation interne

Le fichier est structure en sections logiques :

**Constantes et configuration** — Seuils par defaut (flou, luminosite, uniformite, etc.), expressions regulieres pour la detection de copies, extensions supportees.

**Fonctions d'analyse image** — `laplacian_var()`, `mean_lum()`, `exposure_quality()`, `uniform_frac()`, `has_face()`, `has_body()`, `has_person()`, `compute_rank()`.

**Filtres de contenu** — 9 fonctions `detect_*()` retournant chacune un tuple `(detected: bool, confidence: int)` : `detect_no_person`, `detect_industrial`, `detect_emoji`, `detect_screenshot`, `detect_document`, `detect_motion_blur`, `detect_tiny_file`, `detect_night`, `detect_landscape_no_person`.

**Moteur d'analyse** — Pipeline complet : collecte des images, hashing perceptuel, detection de doublons, analyse qualite, application des filtres de contenu.

**Interface Tkinter** — Classe `PhotoCleanerApp(tk.Tk)` avec theme "Darkroom Pro", sidebar de filtres, zone de resultats avec miniatures, barre de progression.

### Flux de donnees

```
Dossier photos/
    │
    ▼
Collecte (os.walk + filtre extensions)
    │
    ▼
Hashing perceptuel (imagehash.phash)
    │
    ├──▶ Detection doublons (Hamming distance)
    │       │
    │       ▼
    │    Classement (compute_rank → garde le meilleur)
    │
    ▼
Analyse qualite (OpenCV)
    │
    ├──▶ Flou (Laplacien)
    ├──▶ Luminosite
    ├──▶ Uniformite
    │
    ▼
Filtres de contenu (9 detecteurs)
    │
    ▼
Resultats avec scores de confiance
    │
    ▼
Revue manuelle (miniatures + cochage)
    │
    ▼
Deplacement vers review/
```

## 2. Version PyQt6 (pyqt6-app/)

### Architecture modulaire

```
pyqt6-app/
├── main.py                     # Point d'entree
└── app/
    ├── __init__.py
    ├── main_window.py          # QMainWindow — interface principale
    └── styles/
        ├── __init__.py
        └── theme_manager.py    # Theming centralise (clair/sombre)
```

### Principes

**Separation des responsabilites** — Chaque module a un role unique. Le point d'entree ne fait que creer `QApplication` et `MainWindow`.

**Theming centralise** — `ThemeManager` gere les palettes de couleurs et applique les styles via `QApplication.setStyleSheet()`. Permet de basculer entre themes sans modifier les widgets.

**HiDPI natif** — Support des ecrans haute resolution via les attributs Qt `AA_EnableHighDpiScaling` et `AA_UseHighDpiPixmaps`.

### Modules prevus (a developper)

- `app/analysis/` — Moteur d'analyse (port depuis la version Tkinter)
- `app/widgets/` — Composants d'interface reutilisables
- `app/models/` — Modeles de donnees (resultats d'analyse, configuration)
- `app/utils/` — Utilitaires (gestion fichiers, EXIF via exifread)

## Technologies communes

| Composant | Bibliotheque | Usage |
|---|---|---|
| Hash perceptuel | imagehash | Detection de doublons (pHash 64-bit) |
| Analyse image | OpenCV (cv2) | Flou, luminosite, bords, Haar cascades |
| Manipulation image | Pillow (PIL) | Miniatures, lecture formats varies |
| Calcul numerique | NumPy | Statistiques sur les pixels |
