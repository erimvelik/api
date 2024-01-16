import requests
from bs4 import BeautifulSoup
import string


def compute(date):
  date = date.split('/')
  
  program_year = date[2]
  program_month = date[0]
  program_day = date[1]

  URL = "https://www.cbc.ca/listen/live-radio/1-1044-about-time/clip/d" +program_year + program_month + program_day 

  page = requests.get(URL)

  soup = BeautifulSoup(page.content, "html.parser")

  results = soup.find(id="app")
  
  job_elements = results.find_all("div", class_="ule-playlog__track__item__value")

  track_list = []
  
  for job_element in job_elements:
    track_list.append(string.capwords(job_element.contents[0]))
  
  
  return track_list
