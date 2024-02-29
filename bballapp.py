import nbapm
import cbb
#import introcs
#import urllib
from urllib.request import urlopen
import numpy as np
import datetime
import csv
import time
"""
App to access everything
"""

allteams = ['Abilene Christian','Air Force','Akron','Alabama A&M','Alabama-Birmingham','Alabama State','Alabama','Albany (NY)','Alcorn State','American','Appalachian State','Arizona State','Arizona','Arkansas-Little Rock','Arkansas-Pine Bluff','Arkansas State','Arkansas','Army','Auburn','Austin Peay','Ball State','Baylor','Belmont','Bethune-Cookman',
'Binghamton','Boise State','Boston College','Boston University','Bowling Green State','Bradley','Brigham Young','Brown','Bryant','Bucknell','Buffalo','Butler','Cal Poly','Cal State Bakersfield','Cal State Fullerton','Cal State Northridge','California Baptist','California-Davis','California-Irvine','California-Riverside','California-Santa Barbara','California','Campbell','Canisius','Central Arkansas','Central Connecticut State','Central Florida','Central Michigan','Charleston Southern','Charlotte','Chattanooga','Chicago State','Cincinnati','Citadel','Clemson','Cleveland State','Coastal Carolina','Colgate','College of Charleston','Colorado State','Colorado','Columbia','Connecticut','Coppin State','Cornell','Creighton','Dartmouth','Davidson','Dayton','Delaware State','Delaware','Denver','DePaul','Detroit Mercy','Drake','Drexel','Duke','Duquesne','East Carolina','East Tennessee State','Eastern Illinois','Eastern Kentucky','Eastern Michigan','Eastern Washington','Elon','Evansville','Fairfield','Fairleigh Dickinson','Florida A&M','Florida Atlantic','Florida Gulf Coast','Florida International','Florida State','Florida','Fordham','Fresno State','Furman','Gardner-Webb','George Mason','George Washington','Georgetown','Georgia Southern','Georgia State','Georgia Tech','Georgia','Gonzaga','Grambling','Grand Canyon','Green Bay','Hampton','Hartford','Harvard','Hawaii','High Point','Hofstra','Holy Cross','Houston Baptist','Houston','Howard','Idaho State','Idaho','Illinois-Chicago','Illinois State','Illinois','Incarnate Word','Indiana State','Indiana','Iona','Iowa State','Iowa','IPFW','IUPUI','Jackson State','Jacksonville State','Jacksonville','James Madison','Kansas State','Kansas','Kennesaw State','Kent State','Kentucky','La Salle','Lafayette','Lamar','Lehigh','Liberty','Lipscomb','Long Beach State','Long Island University','Longwood','Louisiana-Lafayette','Louisiana-Monroe','Louisiana State','Louisiana Tech','Louisville','Loyola (IL)','Loyola Marymount','Loyola (MD)','Maine','Manhattan','Marist','Marquette','Marshall','Maryland-Baltimore County','Maryland-Eastern Shore','Maryland','Massachusetts-Lowell','Massachusetts','McNeese State','Memphis','Mercer','Merrimack','Miami (FL)','Miami (OH)','Michigan State','Michigan','Middle Tennessee','Milwaukee','Minnesota','Mississippi State','Mississippi Valley State','Mississippi','Missouri-Kansas City','Missouri State','Missouri','Monmouth','Montana State','Montana','Morehead State','Morgan State',"Mount St. Mary's",'Murray State','Navy','Nebraska Omaha','Nebraska','Nevada-Las Vegas','Nevada','New Hampshire','New Mexico State','New Mexico','New Orleans','Niagara','Nicholls State','NJIT','Norfolk State','North Alabama','North Carolina-Asheville','North Carolina A&T','North Carolina Central','North Carolina-Greensboro','North Carolina State','North Carolina-Wilmington','North Carolina','North Dakota State','North Dakota','North Florida','North Texas','Northeastern','Northern Arizona','Northern Colorado','Northern Illinois','Northern Iowa','Northern Kentucky','Northwestern State','Northwestern','Notre Dame','Oakland','Ohio State','Ohio','Oklahoma State','Oklahoma','Old Dominion','Oral Roberts','Oregon State','Oregon','Pacific','Penn State','Pennsylvania','Pepperdine','Pittsburgh','Portland State','Portland','Prairie View','Presbyterian','Princeton','Providence','Purdue','Quinnipiac','Radford','Rhode Island','Rice','Richmond','Rider','Robert Morris','Rutgers','Sacramento State','Sacred Heart','Saint Francis (PA)',"Saint Joseph's",'Saint Louis',"Saint Mary's (CA)","Saint Peter's",'Sam Houston State','Samford','San Diego State','San Diego','San Francisco','San Jose State','Santa Clara','Seattle','Seton Hall','Siena','South Alabama','South Carolina State','South Carolina Upstate','South Carolina','South Dakota State','South Dakota','South Florida','Southeast Missouri State','Southeastern Louisiana','Southern California','Southern Illinois Edwardsville','Southern Illinois','Southern Methodist','Southern Mississippi','Southern Utah','Southern','St. Bonaventure','St. Francis (NY)',"St. John's (NY)",'Stanford','Stephen F. Austin','Stetson','Stony Brook','Syracuse','Temple','Tennessee-Martin','Tennessee State','Tennessee Tech','Tennessee','Texas A&M-Corpus Christi','Texas A&M','Texas-Arlington','Texas Christian','Texas-El Paso','Texas-Pan American','Texas-San Antonio','Texas Southern','Texas State','Texas Tech','Texas','Toledo','Towson','Troy','Tulane','Tulsa','UCLA','Utah State','Utah Valley','Utah','Valparaiso','Vanderbilt','Vermont','Villanova','Virginia Commonwealth','Virginia Military Institute','Virginia Tech','Virginia','Wagner','Wake Forest','Washington State','Washington','Weber State','West Virginia','Western Carolina','Western Illinois','Western Kentucky','Western Michigan','Wichita State','William Mary','Winthrop','Wisconsin','Wofford','Wright State','Wyoming','Xavier','Yale','Youngstown State']
allteams21 = ['Abilene Christian','Air Force','Akron','Alabama A&M','Alabama-Birmingham','Alabama State','Alabama','Albany (NY)','Alcorn State','American','Appalachian State','Arizona State','Arizona','Arkansas-Little Rock','Arkansas-Pine Bluff','Arkansas State','Arkansas','Army','Auburn','Austin Peay','Ball State','Baylor','Bellarmine','Belmont','Binghamton','Boise State','Boston College','Boston University','Bowling Green State','Bradley','Brigham Young','Bryant','Bucknell','Buffalo','Butler','Cal Poly','Cal State Bakersfield','Cal State Fullerton','Cal State Northridge','California Baptist','California-Davis','California-Irvine','California-Riverside','California-Santa Barbara','California','Campbell','Canisius','Central Arkansas','Central Connecticut State','Central Florida','Central Michigan','Charleston Southern','Charlotte','Chattanooga','Cincinnati','Citadel','Clemson','Cleveland State','Coastal Carolina','Colgate','College of Charleston','Colorado State','Colorado','Connecticut','Coppin State','Creighton','Davidson','Dayton','Delaware State','Delaware','Denver','DePaul','Detroit Mercy','Drake','Drexel','Duke','Duquesne','East Carolina','East Tennessee State','Eastern Illinois','Eastern Kentucky','Eastern Michigan','Eastern Washington','Elon','Evansville','Fairfield','Fairleigh Dickinson','Florida A&M','Florida Atlantic','Florida Gulf Coast','Florida International','Florida State','Florida','Fordham','Fresno State','Furman','Gardner-Webb','George Mason','George Washington','Georgetown','Georgia Southern','Georgia State','Georgia Tech','Georgia','Gonzaga','Grambling','Grand Canyon','Green Bay','Hampton','Hartford','Hawaii','High Point','Hofstra','Holy Cross','Houston Baptist','Houston','Idaho State','Idaho','Illinois-Chicago','Illinois State','Illinois','Incarnate Word','Indiana State','Indiana','Iona','Iowa State','Iowa','IPFW','IUPUI','Jackson State','Jacksonville State','Jacksonville','James Madison','Kansas State','Kansas','Kennesaw State','Kent State','Kentucky','La Salle','Lafayette','Lamar','Lehigh','Liberty','Lipscomb','Long Beach State','Long Island University','Longwood','Louisiana-Lafayette','Louisiana-Monroe','Louisiana State','Louisiana Tech','Louisville','Loyola (IL)','Loyola Marymount','Loyola (MD)','Manhattan','Marist','Marquette','Marshall','Maryland-Baltimore County','Maryland','Massachusetts-Lowell','Massachusetts','McNeese State','Memphis','Mercer','Merrimack','Miami (FL)','Miami (OH)','Michigan State','Michigan','Middle Tennessee','Milwaukee','Minnesota','Mississippi State','Mississippi Valley State','Mississippi','Missouri-Kansas City','Missouri State','Missouri','Monmouth','Montana State','Montana','Morehead State','Morgan State',"Mount St. Mary's",'Murray State','Navy','Nebraska Omaha','Nebraska','Nevada-Las Vegas','Nevada','New Hampshire','New Mexico State','New Mexico','New Orleans','Niagara','Nicholls State','NJIT','Norfolk State','North Alabama','North Carolina-Asheville','North Carolina A&T','North Carolina Central','North Carolina-Greensboro','North Carolina State','North Carolina-Wilmington','North Carolina','North Dakota State','North Dakota','North Florida','North Texas','Northeastern','Northern Arizona','Northern Colorado','Northern Illinois','Northern Iowa','Northern Kentucky','Northwestern State','Northwestern','Notre Dame','Oakland','Ohio State','Ohio','Oklahoma State','Oklahoma','Old Dominion','Oral Roberts','Oregon State','Oregon','Pacific','Penn State','Pepperdine','Pittsburgh','Portland State','Portland','Prairie View','Presbyterian','Providence','Purdue','Quinnipiac','Radford','Rhode Island','Rice','Richmond','Rider','Robert Morris','Rutgers','Sacramento State','Sacred Heart','Saint Francis (PA)',"Saint Joseph's",'Saint Louis',"Saint Mary's (CA)","Saint Peter's",'Sam Houston State','Samford','San Diego State','San Diego','San Francisco','San Jose State','Santa Clara','Seattle','Seton Hall','Siena','South Alabama','South Carolina State','South Carolina Upstate','South Carolina','South Dakota State','South Dakota','South Florida','Southeast Missouri State','Southeastern Louisiana','Southern California','Southern Illinois Edwardsville','Southern Illinois','Southern Methodist','Southern Mississippi','Southern Utah','Southern','St. Bonaventure','St. Francis (NY)',"St. John's (NY)",'Stanford','Stephen F. Austin','Stetson','Stony Brook','Syracuse','Temple','Tennessee-Martin','Tennessee State','Tennessee Tech','Tennessee','Texas A&M-Corpus Christi','Texas A&M','Texas-Arlington','Texas Christian','Texas-El Paso','Texas-Pan American','Texas-San Antonio','Texas Southern','Texas State','Texas Tech','Texas','Toledo','Towson','Troy','Tulane','Tulsa','UCLA','Utah State','Utah Valley','Utah','Valparaiso','Vanderbilt','Vermont','Villanova','Virginia Commonwealth','Virginia Military Institute','Virginia Tech','Virginia','Wagner','Wake Forest','Washington State','Washington','Weber State','West Virginia','Western Carolina','Western Illinois','Western Kentucky','Western Michigan','Wichita State','William Mary','Winthrop','Wisconsin','Wofford','Wright State','Wyoming','Xavier','Youngstown State']

nbaeast = ['TOR','BOS','IND','MIL','WAS','PHI','CLE','MIA','CHO','ATL','CHI','DET','BRK','ORL','NYK']

nbawest = ['GSW','HOU','SAS','LAL','OKC','UTA','NOP','MIN','DEN','LAC','POR','DAL','PHO','MEM','SAC']

playoffs = ['MIL','DET','BOS','IND','PHI','BRK','TOR','ORL','GSW','LAC','HOU','UTA','POR','OKC','DEN','SAS']


def slelo(team, year = 2023, men = True, thisyear = False):
    donovan = [int(year), int(year) - 1]
    if (team == 'merrimack') or (thisyear == True):
        donovan = [int(year)]
    bennett = []
    team = team.lower().replace(' ','-')
    for zion in donovan:
        if men == True:
            gender = 'men'
        else:
            gender = 'women'
        url = f'https://www.sports-reference.com/cbb/schools/{team}/{gender}/{zion}.html'
        Portland = str(urlopen(url).read())
        ## Pythagorean Wins
        F = Portland.find('ORtg:</strong> ')
        G = Portland.find(' (', F + 1)
        H = Portland.find('DRtg:</strong> ')
        I = Portland.find(' (', H + 1)
        offrtg = float(Portland[F+15:G])
        defrtg = float(Portland[H+15:I])
        PYT = float((offrtg**9) / (offrtg**9 + defrtg**9))
        ## Strength of Schedule
        J = Portland.find('SOS</a>:</strong> ')
        K = Portland.find(' (', J + 1)
        SOS = float(Portland[J+18:K])
        ## Experience (Updated 2023)
        L = Portland.find('of minutes played')
        M = Portland.find('>', L - 10)
        try:
            experience = float(Portland[M+1:L-2])
        except:
            experience = 50
        EXP = 0.5 + experience / 40
        ## Weighted team PER
        A = int(Portland.find('data-label=\"Advanced'))
        A = int(Portland.find('tbody', A + 1))
        Z = int(Portland.find('div_advanced_conf'))
        Portland = Portland[A:Z]
        tots = 0; allmin = 0
        for x in range(Portland.count('ranker')):
            B = int(Portland.find('data-stat=\"mp\" >'))
            C = int(Portland.find('<', B + 1))
            D = int(Portland.find('data-stat=\"bpm\" >', C + 1))
            E = int(Portland.find('<', D + 1))
            min = Portland[B+16:C]
            bpm = Portland[D+17:E]
            if min == '':
                min = 0
            if bpm == '':
                bpm = 0
            Portland = Portland[E:]
            tots = tots + (float(min) * float(bpm))
            allmin = allmin + float(min)
        ## Combine variables
        BPM = float(tots / allmin)
        bennett.append(float(((1 + (SOS / 25)) * PYT * (15 + BPM / 1.5)) + EXP))
        time.sleep(2)
    if (team == 'merrimack') or (thisyear == True):
        SLELO = (30 * bennett[0])**0.9
    else:
#        SLELO = ((20*bennett[0])+(10*bennett[1]))**0.9
        SLELO = (((30 * bennett[0])**0.9) * 0.7) + (((30 * bennett[1])**0.9) * 0.3)
    return float(SLELO)


def kenpom(year = 2023, men = True, thisyear = False):
    rankings = allteams
    ratings = []
    for team in allteams:
        x = team.lower().replace(' ','-').replace('&','').replace('(','').replace(')','').replace("'",'').replace('.','')
        try:
            y = slelo(x, year, men, thisyear)
            time.sleep(3)
        except:
            print(str(team)+' - No data')
            continue
        ratings.append(round(float(y), 4))
        print(team + ' - ' + str(y))
    ratings = np.array(ratings)
    sort_index = np.argsort(ratings)
    accum = 0
    list = []
    for a in sort_index[::-1]:
        list.append([accum + 1, rankings[a], float(ratings[a])])
        accum += 1
    return list


def gettime():
    return datetime.datetime.now().strftime('%m-%d-%Y')


def csv_upload():
    with open('C::Users/Sydney/Desktop/SLELO/slelo'+str(gettime())+'.csv', 'w', newline='') as rank:
        writer = csv.writer(rank)
        writer.writerows(kenpom())

#Upload data as .txt file
def txt_upload():
    filename = str(gettime())+'.txt'
    with open(filename, 'w') as f:
        for sublist in jj:
            line = "{}, {}, {}\n".format(sublist[0], sublist[1], sublist[2])
            f.write(line)

def game(teams):
    x = len(teams)
    assert np.log2(x) - round(np.log2(x)) < 0.0001
    if x == 2:
        rtg1 = slelo(teams[0]); rtg2 = slelo(teams[1])
        chance1 = 1 / (1 + np.exp((rtg2 - rtg1) / 60))
        return[chance1, 1 - chance1]
    return [game(teams[ :int(x/2)]), game(teams[ :int(x/2)])]
    rtg1 = slelo(team1); rtg2 = slelo(team2)
    chance1 = 1 / (1 + np.exp((rtg2 - rtg1) / 60))
    return [chance1, 1 - chance1]


#def game(teams):
#    rtg1 = slelo(team1); rtg2 = slelo(team2)
#    chance1 = 1 / (1 + 2.718281828459045**((rtg2 - rtg1) / 60))
#    return [chance1, 1 - chance1]





#
