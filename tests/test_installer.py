# tests/test_installer.py
import pytest
from psyche_system.installer import FileInstaller
import requests
from unittest.mock import patch

@patch('requests.get')
def test_download_file(mock_get):
    mock_get.return_value.iter_content = lambda chunk_size: [b'test data']
    mock_get.return_value.__enter__ = lambda s: s
    mock_get.return_value.__exit__ = lambda s, *exc: None
    mock_get.return_value.status_code = 200
    
    fi = FileInstaller()
    with patch('builtins.open', lambda filename, mode: None):
        fi.download_file("http://example.com/file.zip", "file.zip")
    mock_get.assert_called_once_with("http://example.com/file.zip", stream=True)
