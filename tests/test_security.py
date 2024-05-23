# tests/test_security.py
import pytest
from psyche_system.security import SystemSecurity

def test_get_system_info():
    security = SystemSecurity()
    info = security.get_system_info()
    assert 'os' in info
    assert 'os_version' in info
    assert 'architecture' in info
    assert 'processor' in info

def test_check_for_vulnerabilities():
    security = SystemSecurity()
    vulnerabilities = security.check_for_vulnerabilities()
    assert isinstance(vulnerabilities, list)
