from flask import Flask, render_template, request

from util.playlist import compute


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
