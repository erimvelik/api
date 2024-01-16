from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import string
#from requests import get

from api.util import playlist

#def compute(date):
#  date = date.split('/')
#  
#  program_year = date[2]
#  program_month = date[0]
#  program_day = date[1]
#
#  URL = "https://www.cbc.ca/listen/live-radio/1-1044-about-time/clip/d" +program_year + program_month + program_day 
#
#  page = get(URL)
#
#  soup = BeautifulSoup(page.content, "html.parser")
#
#  results = soup.find(id="app")
#  
#  job_elements = results.find_all("div", class_="ule-playlog__track__item__value")
#
#  track_list = []
#  
#  for job_element in job_elements:
#    track_list.append(string.capwords(job_element.contents[0]))
#  
#  
#  return track_list


app = Flask(__name__)

@app.route('/')
def main_tom_allen():
    return render_template("tomallen-date.html")

@app.route('/tomallen-results', methods=['POST'])
def tom_allen_results():
    if request.method=='POST':
      track_list = compute(date=request.form['date'])  
      total_tracks = int(len(track_list) / 4)
      
      if (len(track_list) > 0):
      #return job_elements[0]
        return render_template("about_time.html", track_list=track_list, total_tracks=total_tracks)
      else:
        return "<h3>No Show Today!</h3>"
