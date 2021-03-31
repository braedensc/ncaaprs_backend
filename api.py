import time
from flask import Flask
from athleteProfiles import *
import json
import copy
from flask import request
from flask_cors import CORS

#use for deployment
#app = Flask(__name__, static_folder='../build', static_url_path='/')

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    print("Hello, you connected to default route!")
    return '<p1>Hello, this is the backend server for ncaaprs. A GET request to `https://ncaaprs-backend.herokuapp.com/api/athletes/?param1=${<insert team link here>}` will return a JSON obectt of a track team with all of its athletes prs in each event</p1>'

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}



@app.route('/api/athletes/')
def get_athlete_lists():
    '''Returns a JSON object containingg lists of all events and its athletes for the given team the parameter is the url needed to go to to find the team roster '''
    teamurl = request.args.get('param1')
    athletes = buildAthleteList(teamurl)
    athletes = setallprs(athletes)
    sathletes = copy.deepcopy(athletes)
    for i in range(len(athletes)):
        athletes[i] = json.dumps(athletes[i].toJson())
    athletes60 = buildprList(sathletes, 'pr60')
    for i in range(len(athletes60)):
        athletes60[i] = json.dumps(athletes60[i].toJson())
    athletes60H = buildprList(sathletes, 'pr60H')
    for i in range(len(athletes60H)):
        athletes60H[i] = json.dumps(athletes60H[i].toJson())
    athletes100 = buildprList(sathletes, 'pr100')
    for i in range(len(athletes100)):
        athletes100[i] = json.dumps(athletes100[i].toJson())
    athletes200 = buildprList(sathletes, 'pr200')
    for i in range(len(athletes200)):
        athletes200[i] = json.dumps(athletes200[i].toJson())
    athletes400 = buildprList(sathletes, 'pr400')
    for i in range(len(athletes400)):
        athletes400[i] = json.dumps(athletes400[i].toJson())
    athletes100H = buildprList(sathletes, 'pr100H')
    for i in range(len(athletes100H)):
        athletes100H[i] = json.dumps(athletes100H[i].toJson())
    athletes110H = buildprList(sathletes, 'pr110H')
    for i in range(len(athletes110H)):
        athletes110H[i] = json.dumps(athletes110H[i].toJson())
    athletes400H = buildprList(sathletes, 'pr400H')
    for i in range(len(athletes400H)):
        athletes400H[i] = json.dumps(athletes400H[i].toJson())
    athletes600 = buildprList(sathletes, 'pr600')
    for i in range(len(athletes600)):
        athletes600[i] = json.dumps(athletes600[i].toJson())
    athletes3000S = buildprList(sathletes, 'pr3000S')
    for i in range(len(athletes3000S)):
        athletes3000S[i] = json.dumps(athletes3000S[i].toJson())
    athletes1000 = buildprList(sathletes, 'pr1000')
    for i in range(len(athletes1000)):
        athletes1000[i] = json.dumps(athletes1000[i].toJson())
    athletes800 = buildprList(sathletes, 'pr800')
    for i in range(len(athletes800)):
        athletes800[i] = json.dumps(athletes800[i].toJson())
    athletes1500 = buildprList(sathletes, 'pr1500')
    for i in range(len(athletes1500)):
        athletes1500[i] = json.dumps(athletes1500[i].toJson())
    athletesMile = buildprList(sathletes, 'prMile')
    for i in range(len(athletesMile)):
        athletesMile[i] = json.dumps(athletesMile[i].toJson())
    athletes3000 = buildprList(sathletes, 'pr3000')
    for i in range(len(athletes3000)):
        athletes3000[i] = json.dumps(athletes3000[i].toJson())
    athletes5000 = buildprList(sathletes, 'pr5000')
    for i in range(len(athletes5000)):
        athletes5000[i] = json.dumps(athletes5000[i].toJson())
    athletes10000 = buildprList(sathletes, 'pr10000')
    for i in range(len(athletes10000)):
        athletes10000[i] = json.dumps(athletes10000[i].toJson())
    athletes8k = buildprList(sathletes, 'pr8k')
    for i in range(len(athletes8k)):
        athletes8k[i] = json.dumps(athletes8k[i].toJson())
    athletes10k = buildprList(sathletes, 'pr10k')
    for i in range(len(athletes10k)):
        athletes10k[i] = json.dumps(athletes10k[i].toJson())
    athletes5k = buildprList(sathletes, 'pr5k')
    for i in range(len(athletes5k)):
        athletes5k[i] = json.dumps(athletes5k[i].toJson())
    athletes6k = buildprList(sathletes, 'pr6k')
    for i in range(len(athletes6k)):
        athletes6k[i] = json.dumps(athletes6k[i].toJson())
    
    athletesTJ = buildprList(sathletes, 'prTJ')
    for i in range(len(athletesTJ)):
        athletesTJ[i] = json.dumps(athletesTJ[i].toJson())
    athletesHJ = buildprList(sathletes, 'prHJ')
    for i in range(len(athletesHJ)):
        athletesHJ[i] = json.dumps(athletesHJ[i].toJson())
    athletesLJ = buildprList(sathletes, 'prLJ')
    for i in range(len(athletesLJ)):
        athletesLJ[i] = json.dumps(athletesLJ[i].toJson())
    athletesPV = buildprList(sathletes, 'prPV')
    for i in range(len(athletesPV)):
        athletesPV[i] = json.dumps(athletesPV[i].toJson())
    athletesWT = buildprList(sathletes, 'prWT')
    for i in range(len(athletesWT)):
        athletesWT[i] = json.dumps(athletesWT[i].toJson())
    athletesHT = buildprList(sathletes, 'prHT')
    for i in range(len(athletesHT)):
        athletesHT[i] = json.dumps(athletesHT[i].toJson())
    athletesDT = buildprList(sathletes, 'prDT')
    for i in range(len(athletesDT)):
        athletesDT[i] = json.dumps(athletesDT[i].toJson())
    athletesJT = buildprList(sathletes, 'prJT')
    for i in range(len(athletesJT)):
        athletesJT[i] = json.dumps(athletesJT[i].toJson())
    athletesST = buildprList(sathletes, 'prST')
    for i in range(len(athletesST)):
        athletesST[i] = json.dumps(athletesST[i].toJson())

    return {'athletes' : athletes,
            'athletes60' : athletes60,
            'athletes60H' : athletes60H,
            'athletes100' : athletes100,
            'athletes200' : athletes200,
            'athletes400' : athletes400,
            'athletes100H' : athletes100H,
            'athletes110H' : athletes110H,
            'athletes400H' : athletes400H,
            'athletes600' : athletes600,
            'athletes3000S' : athletes3000S,
            'athletes1000' : athletes1000,
            'athletes800' : athletes800,
            'athletes1500' : athletes1500,
            'athletesMile' : athletesMile,
            'athletes3000' : athletes3000,
            'athletes5000' : athletes5000,
            'athletes10000' : athletes10000,
            'athletes8k' : athletes8k,
            'athletes10k' : athletes10k,
            'athletes5k' : athletes5k,
            'athletes6k' : athletes6k,
            'athletesTJ' : athletesTJ,
            'athletesLJ' : athletesLJ,
            'athletesHJ' : athletesHJ,
            'athletesPV' : athletesPV,
            'athletesWT' : athletesWT,
            'athletesST' : athletesST,
            'athletesDT' : athletesDT,
            'athletesHT' : athletesHT,
            'athletesJT' : athletesJT,
        }

