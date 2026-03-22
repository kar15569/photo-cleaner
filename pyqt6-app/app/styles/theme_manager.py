# TODO: Implementer le gestionnaire de themes PhotoFlow
# Ce module doit exporter une instance `theme_manager`
# capable d'appliquer un theme clair ou sombre a l'application.

from PyQt6.QtWidgets import QApplication


class ThemeManager:
    """Gestionnaire de themes pour PhotoFlow."""

    DARK_THEME = {
        "bg": "#1C1C2E",
        "surface": "#2A2A3E",
        "accent": "#7C5CBF",
        "accent2": "#A87EF5",
        "text": "#E8E8F0",
        "text_dim": "#8888AA",
        "success": "#4CAF82",
        "warning": "#F0A500",
        "danger": "#E05252",
    }

    def __init__(self):
        self.current_theme = "dark"

    def apply_theme(self, app: QApplication):
        """Appliquer le theme courant a l'application."""
        if self.current_theme == "dark":
            self._apply_dark(app)

    def _apply_dark(self, app: QApplication):
        """Appliquer le theme sombre."""
        colors = self.DARK_THEME
        app.setStyleSheet(f"""
            QMainWindow {{
                background-color: {colors['bg']};
            }}
            QLabel {{
                color: {colors['text']};
            }}
            QPushButton {{
                background-color: {colors['accent2']};
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {colors['accent']};
            }}
        """)


# Instance globale
theme_manager = ThemeManager()
