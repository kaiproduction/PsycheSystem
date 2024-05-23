# installer.py
import requests

class FileInstaller:
    def download_file(self, url, dest_path):
        response = requests.get(url, stream=True)
        with open(dest_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Файл загружен и сохранен в {dest_path}")
