# PhotoFlow — Version PyQt6

Reecriture modulaire de Photo Cleaner & Organizer avec **PyQt6**.

## Statut

En cours de developpement. Le point d'entree et l'architecture sont en place, les modules fonctionnels sont a completer.

## Architecture

```
pyqt6-app/
├── main.py                 # Point d'entree (lance QApplication + MainWindow)
├── requirements.txt        # Dependances
└── app/
    ├── __init__.py
    ├── main_window.py      # Fenetre principale (a completer)
    └── styles/
        ├── __init__.py
        └── theme_manager.py  # Gestionnaire de theme centralise (a completer)
```

## Differences avec la version Tkinter

| Aspect | Tkinter | PyQt6 |
|---|---|---|
| Framework GUI | Tkinter (stdlib) | PyQt6 |
| Architecture | Mono-fichier | Modulaire (app/) |
| Theming | Manuel (couleurs hardcodees) | Centralise (theme_manager) |
| HiDPI | Non gere | Natif (AA_EnableHighDpiScaling) |
| OpenCV | opencv-python | opencv-python-headless |
| EXIF | Non | exifread |

## Installation

```bash
pip install -r requirements.txt
```

## Lancement

```bash
python main.py
```

## Feuille de route

- [ ] Implementer `app/main_window.py` (interface principale)
- [ ] Implementer `app/styles/theme_manager.py` (themes clair/sombre)
- [ ] Porter les fonctionnalites d'analyse de la version Tkinter v5
- [ ] Ajouter la lecture EXIF (exifread)
- [ ] Systeme de plugins pour filtres personnalises
