import requests
from bs4 import BeautifulSoup


URL = "https://www.jobindex.dk/jobsoegning?q=python"  
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")

#print(page.content) 
#print(soup.prettify()) 

job_listings = soup.find_all('div', class_='PaidJob')
print(job_listings)
for job in job_listings:
  # title = job.find('div', class_='PaidJob-inner').text.strip()
    title = job.find('h4').text.strip()
    company = job.find('div', class_='jix-toolbar-top__company').text.strip()
    location = job.find('span', class_='jix_robotjob--area').text.strip()
    print('-----------------------------------------------------')
    print('')
    print(f"Job Title: {title}\nCompany: {company}\nLocation: {location}\n")

    