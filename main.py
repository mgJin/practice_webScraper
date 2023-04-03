from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

results = []
job_data = {}
base_url = "https://www.saramin.co.kr/zf_user/search?searchType=search&searchword="
search_keyword = "python"
final_url = f"{base_url}{search_keyword}"
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get(final_url)

soup = BeautifulSoup(browser.page_source, 'html.parser')

boxs = soup.find_all('div', class_="item_recruit")

for box in boxs:
  area_job = box.find('div', class_="area_job")
  area_corp = box.find('div', class_="area_corp")
  """
  job_anchors = area_job.select_one("h2 a")
  title = job_anchors['title']
  link = job_anchors['href']
  #print(title)
  #print(link)
  job_date =area_job.find('span',class_="date")
  #print(job_date)
  #print("\n")
  job_conditions_big = area_job.find('div',class_="job_condition")
  
  if(len(job_conditions_big('span'))==4):
    loca,carrer,education,worktime = job_conditions_big.find_all('span')
  elif(len(job_conditions_big('span'))==5):
    loca,carrer,education,worktime,money = job_conditions_big.find_all('span')
  else:
    print("much data")
  
  job_locations = loca.find_all('a')
  location=[]
  for job_location in job_locations:
    location.append(job_location.string)

  #print(location)
  #print("\n")
  """

  job_company = area_corp.select_one("strong a")
  company_link = job_company['href']
  company_name = job_company.string
