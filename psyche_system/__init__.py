# __init__.py
from .window import PsycheWindow
from .security import SystemSecurity
from .password import PasswordManager
from .installer import FileInstaller

class PsycheSystem:
    def __init__(self):
        self._window = None
        self._security = None
        self._password_manager = None
        self._file_installer = None

    @property
    def window(self):
        if self._window is None:
            self._window = PsycheWindow()
        return self._window

    @property
    def security(self):
        if self._security is None:
            self._security = SystemSecurity()
        return self._security

    @property
    def password_manager(self):
        if self._password_manager is None:
            self._password_manager = PasswordManager()
        return self._password_manager

    @property
    def file_installer(self):
        if self._file_installer is None:
            self._file_installer = FileInstaller()
        return self._file_installer
