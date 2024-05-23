# tests/test_window.py
from psyche_system.window import PsycheWindow
from PyQt5.QtWidgets import QApplication
import pytest
import sys

@pytest.fixture
def app(qtbot):
    test_app = QApplication(sys.argv)
    qtbot.addWidget(test_app)
    return test_app

def test_window_creation(qtbot, app):
    window = PsycheWindow("Test Window", 600, 400)
    qtbot.addWidget(window)
    window.show()
    assert window.windowTitle() == "Test Window"
    assert window.width() == 600
    assert window.height() == 400
