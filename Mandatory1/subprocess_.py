import subprocess

# kloner GitHub-repo
repo_url = 'https://github.com/python-elective-kea/spring2024.git'
clone = ['git', 'clone', repo_url]
subprocess.run(clone) 

# Åbne index.html filen i browseren fra docs mappen
file_path = 'spring2024/docs/index.html'
open_ = ['open', file_path] # 'open' er et kommando til at åbne filer i MacOS terminal
subprocess.run(open_) 

