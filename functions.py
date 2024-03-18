import pandas as pd
import numpy as np
import datetime as datetime
import time
import urllib3
from urllib.request import urlopen


def get_all_teams(year, gender = 'men'):
    ## Return the first table if men's, the second if women's
    if gender == 'men':
        team_table = pd.read_html('https://www.sports-reference.com/cbb/schools/')[0]
    else:
        team_table = pd.read_html('https://www.sports-reference.com/cbb/schools/')[1]
    team_names = team_table.School[team_table.To == str(year)]
    teams = team_names.str.lower().replace(' ', '-', regex = True).replace('\&', '', regex = True).replace('\(', '', regex = True).replace('\)', '', regex = True).replace("\'", '', regex = True).replace('\.','', regex = True)
    ## Account for California and Texas schools
    teams = teams.str.replace('uc-', 'california-').replace('ut-', 'texas-').replace('nc-', 'north-carolina-')
    ## Edge cases
    teams = teams.str.replace('tcu', 'texas-christian').replace('sam-houston', 'sam-houston-state').replace('nc-state', 'north-carolina-state')
    return pd.DataFrame(np.transpose([team_names.tolist(), teams.tolist()]), columns = ['Name', 'name'])


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
        time.sleep(3)
    if (team == 'merrimack') or (thisyear == True):
        SLELO = (30 * bennett[0])**0.9
    else:
        #        SLELO = ((20*bennett[0])+(10*bennett[1]))**0.9
        SLELO = (((30 * bennett[0])**0.9) * 0.7) + (((30 * bennett[1])**0.9) * 0.3)
    return float(SLELO)


def get_team_bpm(tables):
    bpm_table = tables[13].fillna(0)
    min_factor = (bpm_table.MP / (bpm_table.G + 2)) ** 1.4
    adj_mpg = 200 * min_factor / sum(min_factor)
    return np.dot(bpm_table.BPM, adj_mpg) / 200


def get_team_experience(tables):
    my_keys = {
        'FR' : 1,
        'SO' : 2,
        'JR' : 3,
        'SR' : 4,
        np.nan : 2.5
    }
    roster = tables[0]
    exper = [my_keys.get(i) for i in roster.Class[pd.notnull(roster.Summary)]]
    bpm_table = tables[13]
    min_factor = (bpm_table.MP / (bpm_table.G + 2)) ** 1.4
    adj_mpg = 200 * min_factor / sum(min_factor)
    return np.average(exper, weights = adj_mpg)


def slelo_2024(team, year = 2024, gender = 'men'):
    tables = pd.read_html(f'https://www.sports-reference.com/cbb/schools/{team}/{gender}/{year}.html')
    exp_0 = get_team_experience(tables)
    bpm_0 = get_team_bpm(tables)
    net_this = bpm_0 + 0.2 * (exp_0 - 3)
    time.sleep(3)
    tables = pd.read_html(f'https://www.sports-reference.com/cbb/schools/{team}/{gender}/{year - 1}.html')
    exp_1 = get_team_experience(tables)
    bpm_1 = get_team_bpm(tables)
    net_last = bpm_1 + 0.2 * (exp_1 - 3)
    return net_this * 0.8 + net_last * 0.2
                                                                                        


m_f = input('Please choose team or gender (men or women): ')
if (m_f == 'men') or (m_f == 'women'):
    teams = get_all_teams(2024, gender = m_f)
    results_df = []
    print(teams)
    for i in teams.name:
        try:
            x = slelo_2024(i, gender = m_f)
            print([i, x])
            results_df.append([i, x])
            time.sleep(3)
        except:
            print(str(i) + ' (No data)')
            results_df.append([i, -19])
            time.sleep(3)
    results_df = pd.DataFrame(results_df, columns = ['Team', 'SLELO'])
    results_df.Team = teams.Name
    print(results_df.sort_values(by = ['SLELO'], ascending = False))
    results_df.to_csv(f'slelo_2024_{m_f}.csv', index = False)
else:
    gender = input('Please choose the gender for this team (men or women):')
    print(slelo_2024(m_f, gender = gender))


    

