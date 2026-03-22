# Photo Cleaner & Organizer — Version Tkinter

Application de bureau Tkinter pour detecter et trier les photos problematiques dans vos collections.

## Fonctionnalites (v5 — version finale)

**Analyse de qualite :**
- Flou (variance du Laplacien)
- Luminosite (trop sombre / surexpose)
- Uniformite (image unie / capture d'ecran)
- Flou de mouvement directionnel

**Detection de doublons :**
- Doublons exacts via hash perceptuel (pHash)
- Quasi-doublons (distance de Hamming configurable)
- Conservation automatique de la meilleure version
- Detection des fichiers "copie" par analyse du nom

**Filtres de contenu :**
- Photos sans personne detectee (visage + corps)
- Photos industrielles / techniques
- Emoticones / stickers / memes
- Captures d'ecran
- Documents / texte imprime
- Fichiers trop petits
- Photos de nuit sans sujet
- Paysages sans personne

**Interface :**
- Theme "Darkroom Pro" inspire Lightroom
- Miniatures pour revue visuelle
- Pre-cochage intelligent (seul le moins bon doublon est coche)
- Auto-calibration des seuils sur vos photos
- Sidebar scrollable avec tous les filtres activables
- Barre de progression et scores de confiance

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python main.py
```

1. Selectionnez un dossier racine contenant un sous-dossier `photos/`
2. Lancez l'analyse
3. Examinez les resultats (miniatures + scores)
4. Cochez les photos a deplacer
5. Cliquez "Deplacer les selectionnes" — les fichiers vont dans `review/`

## Versions archivees

Le dossier `archive/` contient toutes les versions intermediaires. Voir `archive/README.md` pour le detail de chaque version.
