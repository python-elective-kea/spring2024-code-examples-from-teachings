import json
import requests

# 1. 
# From this api https://api.github.com/orgs/python-elective-kea/repos 
# get all clone_urls of the repos and write them to an appropiate datastructure.
url = 'https://api.github.com/orgs/python-elective-kea/repos'

response = requests.get(url)

if response.status_code == 200:
    print('-- succesful request --')
    data = response.json()  # Konverterer response til JSON format

list = []

for thing in data:
    list.append(thing['clone_url'])

for url in list:
    print(url)

# 2. 
# Create a folder inside the one you are currently in.

import os

# gå til ses4 og opret ny folder
os.chdir("/workspaces/spring2024-code-examples-from-teachings/ses4") # går til ses4
if os.path.isdir("/workspaces/spring2024-code-examples-from-teachings/ses4/all_repos") == False:
    os.mkdir('5_json_new_folder')

# gå til ny folder
os.chdir('5_json_new_folder')
print(f'Vi er nu i: {os.getcwd()}, containing {os.listdir}')

# 3.
# Clone all repos into this folder.

# ????????????
