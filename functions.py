import pandas as pd
import numpy as np
import datetime as datetime
import time
import urllib3
from urllib.request import urlopen


def get_all_teams(year, gender = 'M'):
    ## Return the first table if men's, the second if women's
    if gender == 'M':
        team_table = pd.read_html('https://www.sports-reference.com/cbb/schools/')[0]
    else:
        team_table = pd.read_html('https://www.sports-reference.com/cbb/schools/')[1]
    teams = team_table.School[team_table.To == str(year)]
    teams = teams.str.lower().replace(' ', '-', regex = True).replace('\&', '', regex = True).replace('\(', '', regex = True).replace('\)', '', regex = True).replace("\'", '', regex = True).replace('\.','', regex = True)
    return teams


def slelo(team, year = 2024, men = True, thisyear = False):
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
            tots += float(min) * float(bpm)
            allmin += float(min)
        ## Combine variables
        BPM = float(tots / allmin)
        print(BPM)
        bennett.append(float(((1 + (SOS / 25)) * PYT * (15 + BPM / 1.5)) + EXP))
    time.sleep(2)
    if (team == 'merrimack') or (thisyear == True):
        SLELO = (30 * bennett[0])**0.9
    else:
        #        SLELO = ((20*bennett[0])+(10*bennett[1]))**0.9
        SLELO = (((30 * bennett[0])**0.9) * 0.7) + (((30 * bennett[1])**0.9) * 0.3)
    return float(SLELO)




x = get_all_teams(2024)
for i in x[:10]:
    print([i, slelo(i)])



































































































