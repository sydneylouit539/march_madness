## File to store old March Madness data for backtesting
mm16 = ['Kansas','Austin Peay','Colorado','Connecticut','Maryland','South Dakota State','California','Hawaii','Arizona','Wichita State','Vanderbilt','Miami FL','Buffalo','Iowa','Temple','Villanova','North Carolina Asheville','Oregon','Holy Cross','Southern','Saint Josephs','Cincinnati','Baylor','Yale','Duke','North Carolina Wilmington','Texas','Northern Iowa','Texas AM','Green Bay','Oregon State','Virginia Commonwealth','Oklahoma','Cal State Bakersfield','North Carolina','Florida Gulf Coast','Fairleigh Dickinson','Southern California','Providence','Indiana','Chattanooga','Kentucky','Stony Brook','Notre Dame','Michigan','Tulsa','West Virginia','Stephen F Austin','Wisconsin','Pittsburgh','Xavier','Weber State','Virginia','Hampton','Texas Tech','Butler','Purdue','Arkansas Little Rock','Iowa State','Iona','Seton Hall','Gonzaga','Utah','Fresno State','Dayton','Syracuse','Michigan State','Middle Tennessee']

mm17 = ['Villanova','Mount St Marys','New Orleans','Wisconsin','Virginia Tech','Virginia','North Carolina Wilmington','Florida','East Tennessee State','Southern Methodist','Providence','Southern California','Baylor','New Mexico State','South Carolina','Marquette','Duke','Troy','Gonzaga','South Dakota State','Northwestern','Vanderbilt','Notre Dame','Princeton','West Virginia','Bucknell','Maryland','Xavier','Florida State','Florida Gulf Coast','Saint Marys CA','Virginia Commonwealth','Arizona','North Dakota','Kansas','California Davis','North Carolina Central','Miami FL','Michigan State','Iowa State','Nevada','Purdue','Vermont','Creighton','Rhode Island','Oregon','Iona','Michigan','Oklahoma State','Louisville','Jacksonville State','North Carolina','Texas Southern','Arkansas','Seton Hall','Minnesota','Middle Tennessee','Butler','Winthrop','Cincinnati','Kansas State','Wake Forest','UCLA','Kent State','Dayton','Wichita State','Kentucky','Northern Kentucky']

mm = ['Virginia', 'Maryland Baltimore County', 'Creighton', 'Kansas State', 'Kentucky', 'Davidson', 'Arizona', 'Buffalo', 'Miami FL', 'Loyola IL', 'Tennessee', 'Wright State', 'Nevada', 'Texas', 'Cincinnati', 'Georgia State', 'Xavier', 'North Carolina Central', 'Texas Southern', 'Missouri', 'Florida State', 'Ohio State', 'South Dakota State', 'Gonzaga', 'North Carolina Greensboro', 'Houston', 'San Diego State', 'Michigan', 'Montana', 'Texas AM', 'Providence', 'North Carolina', 'Lipscomb','Villanova', 'Radford', 'Long Island University', 'Virginia Tech', 'Alabama', 'West Virginia', 'Murray State', 'Wichita State', 'Marshall', 'Florida', 'St Bonaventure', 'UCLA', 'Texas Tech', 'Stephen F Austin', 'Arkansas', 'Butler', 'Purdue', 'Cal State Fullerton', 'Kansas', 'Pennsylvania', 'Seton Hall', 'North Carolina State', 'Clemson', 'New Mexico State', 'Auburn', 'College of Charleston', 'Texas Christian', 'Arizona State', 'Syracuse', 'Michigan State', 'Bucknell', 'Rhode Island', 'Oklahoma', 'Duke', 'Iona']
mm19 = ['Duke','North Carolina Central','North Dakota State','Virginia Commonwealth','Central Florida','Mississippi State','Liberty','Virginia Tech','Saint Louis','Maryland','Belmont','Temple','Louisiana State','Yale','Louisville','Minnesota','Michigan State','Bradley','Gonzaga','Fairleigh Dickinson','Prairie View','Syracuse','Baylor','Marquette','Murray State','Florida State','Vermont','Buffalo','Arizona State','St Johns NY','Texas Tech','Northern Kentucky','Nevada','Florida','Michigan','Montana','Virginia','Gardner-Webb','Mississippi','Oklahoma','Wisconsin','Oregon','Kansas State','California Irvine','Villanova','Saint Marys CA','Purdue','Old Dominion','Cincinnati','Iowa','Tennessee','Colgate','North Carolina','Iona','Utah State','Washington','Auburn','New Mexico State','Kansas','Northeastern','Iowa State','Ohio State','Houston','Georgia State','Wofford','Seton Hall','Kentucky','Abilene Christian']

mm22 = ['Gonzaga','Georgia State','Boise State','Memphis','Connecticut','New Mexico State','Arkansas','Vermont','Alabama','Rutgers','Notre Dame','Texas Tech','Montana State','Michigan State','Davidson','Duke','Cal State Fullerton','Baylor','Norfolk State','North Carolina','Marquette','Saint Marys CA','Wyoming','Indiana','UCLA','Akron','Texas','Virginia Tech','Purdue','Yale','Murray State','San Francisco','Kentucky','Saint Peters','Arizona','Bryant','Wright State','Seton Hall','Texas Christian','Houston','Alabama-Birmingham','Illinois','Chattanooga','Colorado State','Michigan','Tennessee','Longwood','Ohio State','Loyola IL','Villanova','Delaware','Kansas','Texas Southern','Texas AM Corpus Christi','San Diego State','Creighton','Iowa','Richmond','Providence','South Dakota State','Louisiana State','Iowa State','Wisconsin','Colgate','Southern California','Miami FL','Auburn','Jacksonville State']
#'Bethune-Cookman'


ef pm(player, year=2023, number='01'):
    print(nbapm.extrapm(player,year,number))
    print(nbapm.extraon(player,year,number))
    print(nbapm.extraoff(player,year,number))
    print("Isn't that interesting?")


def teamper(team,year):
    Q = round(nbapm.playerper(team,year),4)
    R = int((10*(Q-15))+41)
    print(f"Average team PER is {Q}, equivalent to a {R}-win season.")
    print("Isn't that interesting?")


def spitemout(year = 2023):
    for x in nbaeast:
        P = round(nbapm.playerper(x,year),4)
        print(P)
    print(' ')
    print(' ')
    for y in nbawest:
        N = round(nbapm.playerper(y,year),4)
        print(N)


def playoffteamper(year = 2023):
    for a in playoffs:
        team = round(nbapm.playoffper(a), 4)
        print(team)


def pyt(year = 2023):
    for x in nbaeast:
        A = nbapm.teampythag(x,year)
        print(A)
    print(' ')
    print(' ')
    for y in nbawest:
        B = nbapm.teampythag(y,year)
        print(B)


def cbbper(team, year=2023):
    Q = round(cbb.avper(team,year),4)
    R = int((10*(Q-15))+41)
    print(Q)


def cbbspit(teams, year=2023):
    for x in teams:
        Z = round(cbb.avper(x, int(year)),4)
        print(Z)


def spitsos(teams, year=2023):
    for x in teams:
        C = cbb.sos(x,year)
        print(C)


def spitcbbpyt(teams, year=2023):
    for x in teams:
        N = cbb.teampythag(x,year)
        print(N)


def cbbstats(team, year=2023):
    print(cbb.avper(team))
    time.sleep(1)
    print(cbb.sos(team))
    time.sleep(1)
    print(cbb.teampythag(team))
    time.sleep(1)
    print(cbb.avper(team, int(year) - 1))
    time.sleep(1)
    print(cbb.sos(team, int(year) - 1))
    time.sleep(1)
    print(cbb.teampythag(team, int(year) - 1))


def spitcbbexp(teams, year=2023):
    for x in teams:
        N = cbb.exp(x, year)
        print(N)
