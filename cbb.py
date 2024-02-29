import introcs
import math
"""
Modules for Men's and Women's College Basketball-related player and team statistics.

Includes Player +/-, Team PER, and Team Pythagorean Wins

Enjoy!
"""

wcbb = ['Baylor','Abilene Christian','California','N. Carolina','Florida St.','Bucknell','South Carolina','Belmont','Kentucky','Princeton','N.C. State','Maine','Missouri','Drake','Iowa','Mercer','Mississippi St.','Southern','South Dakota','Clemson','Arizona St.',
'UCF','Miami (FL)','Fla. Gulf Coast','S. Dakota St.','Quinnipiac','Syracuse','Fordham','Texas','Indiana','Oregon','Portland St.','Notre Dame','Bethune-Cookman','Cent. Michigan','Michigan St.','Marquette','Rice','Texas A&M','Wright St.','DePaul','Missouri St.''Iowa St.','N. Mex. St.','BYU','Auburn','Stanford','UC Davis','Louisville','Robert Morris','Michigan','Kansas St.','Gonzaga','AR Little Rock','Oregon St.','Boise St.','UCLA','Tennessee','Maryland','Radford','Rutgers','Buffalo','Connecticut','Towson']

def avper(team, year=2020):
    """
    Determines the average Player Efficiency Rating (PER) of a college basketball team in any recent year
    Parameters: Team name and Year
    Precondition: Team name is valid
    """
    U = team.lower().replace(' ','-')
    Portland = introcs.urlread('https://www.sports-reference.com/cbb/schools/'+str(U)+'/'+str(year)+'.html')
    tots = 0
    allmin = 0
    a = int(Portland.find('data-label=\"Advanced'))
    A = int(Portland.find('tbody', a+1))
    Z = int(Portland.find('data-label=\"Conference Per Game'))
    Portland = Portland[A:Z]
    for x in range(Portland.count('ranker')):
        B = int(Portland.find('data-stat=\"mp\" >'))
        C = int(Portland.find('<',B+1))
        D = int(Portland.find('data-stat=\"per\" >',C+1))
        E = int(Portland.find('<',D+1))
        min = Portland[B+16:C]
        per = Portland[D+17:E]
        if min == '':
            min = 0
        if per == '':
            per = 0
        Portland = Portland[E:]
        tots = tots+(float(min)*float(per))
        allmin = allmin+float(min)
    return tots/allmin


def teampythag(team, year=2020):
    """
    Returns the team's Pythagorean Wins for any men's college basketball team in any recent year

    Parameters:

    Precondition:
    """
    C = team.lower()
    D = C.replace(' ','-')
    E = introcs.urlread('https://www.sports-reference.com/cbb/schools/'+str(D)+'/'+str(year)+'.html')
    F = E.find('ORtg:</strong> ')
    G = E.find(' (',F+1)
    H = E.find('DRtg:</strong> ')
    I = E.find(' (',H+1)
    J = float(E[F+15:G])
    K = float(E[H+15:I])
    L = J**9
    M = K**9
    N = round((L/(L+M)),4)
    return N


def sos(team, year=2020):
    """
    Returns the weighted Strength of Schedule of a team

    Parameters:

    Precondition:
    """
    Z = team.lower()
    Y = Z.replace(' ','-')
    A = introcs.urlread('https://www.sports-reference.com/cbb/schools/'+str(Y)+'/'+str(year)+'.html')
    B = A.find('SOS</a>:</strong> ')
    C = A.find(' (',B+1)
    D = float(A[B+18:C])
    return D


def exp(team, year=2020):
    """
    Returns the average years of experience on a team

    Parameters:

    Precondition:
    """
    Y = team.lower().replace(' ','-')
    A = introcs.urlread('https://www.sports-reference.com/cbb/schools/'+str(Y)+'/'+str(year)+'.html')
    B = A.find('Avg. Years Exp:</strong>&nbsp;')
    C = A.find('<',B+25)
    D = float(A[B+30:C])
    return D


def wsos(team):
    """
    Returns the weighted Strength of Schedule of a team

    Parameters:

    Precondition:
    """
    rpis = introcs.urlread('http://www.realtimerpi.com/college_Women_basketball_rpi_Full.html')
    cut = rpis.find('Conf.<br>W-L</b>')
    rpis = rpis[cut:]
    for x in wcbb:
        team = rpis.find(x)
