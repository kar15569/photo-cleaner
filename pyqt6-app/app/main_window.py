# TODO: Implementer la fenetre principale PhotoFlow
# Ce module doit exporter la classe MainWindow
# qui herite de QMainWindow et contient l'interface utilisateur.

from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    """Fenetre principale de PhotoFlow."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PhotoFlow")
        self.setMinimumSize(1100, 720)
        self._build_ui()

    def _build_ui(self):
        """Construire l'interface utilisateur."""
        # TODO: Implementer l'interface
        pass
