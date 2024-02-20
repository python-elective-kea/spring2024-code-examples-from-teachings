import requests 
import subprocess
import os


# Hent data fra API'en
response = requests.get('https://api.github.com/orgs/python-elective-kea/repos')
repos = response.json()

# Uddrag clone_urls
clone_urls = [repo['clone_url'] for repo in repos]

# Navnet på mappen, hvor repos skal klones ind i. Hvis mappen ikke eksisterer, oprettes den. Hvis den eksisterer, gør det ikke noget.
folder_name = 'cloned_repos'
os.makedirs(folder_name, exist_ok=True)

# Skifter mappe til den nye mappe
os.chdir(folder_name)

# Kloner repos
for url in clone_urls:
    subprocess.run(['git', 'clone', url])