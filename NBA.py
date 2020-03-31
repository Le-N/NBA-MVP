import pandas as pd
import numpy as np

players = pd.read_csv('/Users/Coni/Desktop/ENSAE/1A/Projet informatique/Data/players.csv')
seasons_stats = pd.read_csv('/Users/Coni/Desktop/ENSAE/1A/Projet informatique/Data/seasons_stats.csv')

seasons_stats['classé MVP'] = 0
seasons_stats['score MVP'] = 0 


def add_score(player_name, year, score):
    seasons_stats.loc[(seasons_stats['Player']==player_name) & (seasons_stats['Year']==year), ['classé MVP']] = 1
    seasons_stats.loc[(seasons_stats['Player']==player_name) & (seasons_stats['Year']==year), ['score MVP']] = score


def extract_mvp_y_by_y(year):
    df=seasons_stats[(seasons_stats['Year']==year) & (seasons_stats['classé MVP']==1)]
    chemin = '/Users/Coni/Desktop/ENSAE/1A/Projet informatique/Data/mvp' + str(year) + '.csv'
    df.to_csv(chemin, index=False)

df = seasons_stats[seasons_stats['Year']>1973]
df.isnull().sum()

### 2016 - 2017 ###
add_score('Russell Westbrook',2017,0.879)
add_score('James Harden',2017,0.746)
add_score('Kawhi Leonard',2017,0.495)
add_score('LeBron James',2017,0.330)
add_score('Isaiah Thomas',2017,0.08)
add_score('Stephen Curry',2017,0.051)
add_score('Giannis Antetokounmpo',2017,0.007)
add_score('John Wall',2017,0.007)
add_score('Anthony Davis',2017,0.002)
add_score('Kevin Durant',2017,0.002)
add_score('DeMar DeRozan',2017,0.001)
extract_mvp_y_by_y(2017)
mvp_2017 = pd.read_csv('/Users/Coni/Desktop/ENSAE/1A/Projet informatique/Data/mvp2017.csv')

### 2015 - 2016 ###
add_score('Stephen Curry',2016,1)
add_score('Kawhi Leonard',2016,0.484)
add_score('LeBron James',2016,0.482)
add_score('Russell Westbrook',2016,0.371)
add_score('Kevin Durant',2016,0.112)
add_score('Chris Paul',2016,0.082)
add_score('Draymond Green',2016,0.038)
add_score('Damian Lillard',2016,0.02)
add_score('James Harden',2016,0.007)
add_score('Kyle Lowry',2016,0.005)
extract_mvp_y_by_y(2016)
mvp_2016 = pd.read_csv('/Users/Coni/Desktop/ENSAE/1A/Projet informatique/Data/mvp2016.csv')

### 2014 - 2015 ###
add_score('Stephen Curry',2015,0.922)
add_score('James Harden',2015,0.72)
add_score('LeBron James',2015,0.425)
add_score('Russell Westbrook',2015,0.271)
add_score('Anthony Davis',2015,0.156)
add_score('Chris Paul',2015,0.095)
add_score('LaMarcus Aldridge',2015,0.005)
add_score('Marc Gasol',2015,0.002)
add_score('Blake Griffin',2015,0.002)
add_score('Tim Duncan',2015,0.001)
add_score('Kawhi Leonard',2015,0.001)
add_score('Klay Thompson',2015,0.001)
extract_mvp_y_by_y(2015)
mvp_2015 = pd.read_csv('/Users/Coni/Desktop/ENSAE/1A/Projet informatique/Data/mvp2015.csv')

### 2013 - 2014 ###
add_score('Kevin Durant',2014,0.986)
add_score('LeBron James',2014,0.713)
add_score('Blake Griffin',2014,0.347)
add_score('Joakim Noah',2014,0.258)
add_score('James Harden',2014,0.068)
add_score('Stephen Curry',2014,0.053)
add_score('Chris Paul',2014,0.036)
add_score('Al Jefferson',2014,0.027)
add_score('Paul George',2014,0.026)
add_score('LaMarcus Aldridge',2014,0.021)
add_score('Kevin Love',2014,0.020)
add_score('Tim Duncan',2014,0.017)
add_score('Tony Parker',2014,0.017)
add_score('Dirk Nowitzki',2014,0.006)
add_score('Carmelo Anthony',2014,0.003)
add_score('Goran Dragic',2014,0.002)
add_score('Mike Conley',2014,0.001)
extract_mvp_y_by_y(2014)
mvp_2014 = pd.read_csv('/Users/Coni/Desktop/ENSAE/1A/Projet informatique/Data/mvp2014.csv')

### 2012 - 2013 ###
add_score('LeBron James',2013,0.998)
add_score('Kevin Durant',2013,0.632)
add_score('Carmelo Anthony',2013,0.393)
add_score('Chris Paul',2013,0.239)
add_score('Kobe Bryant',2013,0.152)
add_score('Tony Parker',2013,0.071)
add_score('Tim Duncan',2013,0.054)
add_score('James Harden',2013,0.027)
add_score('Russell Westbrook',2013,0.007)
add_score('Dwyane Wade',2013,0.004)
add_score('Stephen Curry',2013,0.002)
add_score('Kevin Garnett',2013,0.001)
add_score('Marc Gasol',2013,0.001)
add_score('Ty Lawson',2013,0.001)
add_score('David Lee',2013,0.001)
add_score('Joakim Noah',2013,0.001)
extract_mvp_y_by_y(2013)
mvp_2013 = pd.read_csv('/Users/Coni/Desktop/ENSAE/1A/Projet informatique/Data/mvp2013.csv')

### 2011 - 2012 ###
add_score('LeBron James',2012,0.888)
add_score('Kevin Durant',2012,0.735)
add_score('Chris Paul',2012,0.318)
add_score('Kobe Bryant',2012,0.291)
add_score('Tony Parker',2012,0.274)
add_score('Kevin Love',2012,0.048)
add_score('Dwight Howard',2012,0.011)
add_score('Rajon Rondo',2012,0.01)
add_score('Steve Nash',2012,0.006)
add_score('Dwyane Wade',2012,0.005)
add_score('Derrick Rose',2012,0.004)
add_score('Dirk Nowitzki',2012,0.003)
add_score('Russell Westbrook',2012,0.003)
add_score('Tim Duncan',2012,0.002)
add_score('Joe Johnson',2012,0.001)
extract_mvp_y_by_y(2012)
mvp_2012 = pd.read_csv('/Users/Coni/Desktop/ENSAE/1A/Projet informatique/Data/mvp2012.csv')

### 2010 - 2011 ###
add_score('Derrick Rose',2011,0.977)
add_score('Dwight Howard',2011,0.531)
add_score('LeBron James',2011,0.431)
add_score('Kobe Bryant',2011,0.354)
add_score('Kevin Durant',2011,0.157)
add_score('Dirk Nowitzki',2011,0.093)
add_score('Dwyane Wade',2011,0.02)
add_score('Manu Ginobili',2011,0.017)
add_score("Amar'e Stoudemire",2011,0.007)
add_score('Blake Griffin',2011,0.004)
add_score('Rajon Rondo',2011,0.004)
add_score('Tony Parker',2011,0.002)
add_score('Chris Paul',2011,0.002)
extract_mvp_y_by_y(2011)
mvp_2011 = pd.read_csv('/Users/Coni/Desktop/ENSAE/1A/Projet informatique/Data/mvp2011.csv')







### 1993 - 1994 ### 

addscore('Hakeem Olajuwon',1994,0.880)
addscore('David Robinson',1994,0.723)
addscore('Scottie Pippen',1994,0.386)
addscore('Shaquille ONeal',1994,0.286)  
addscore('Patrick Ewing',1994,0.252)
addscore('Gary Payton',1994,0.020)
addscore('Shawn Kemp',1994,0.017)
addscore('Karl Malone',1994,0.017)  
addscore('Mark Price',1994,0.007)
addscore('Charles Barkley',1994,0.005)
addscore('Mookie Blaylock',1994,0.001)
addscore('Kevin Johnson',1994,0.001)  
addscore('Dennis Rodman',1994,0.001)
addscore('Latrell Sprewell',1994,0.001)
addscore('John Stockton',1994,0.001)
addscore('Dominique Wilkins',1994,0.001)  
addscore('Kevin Willis',1994,0.001)           
      
### 1992 - 1993 ###

addscore('Charles Barkley',1993,0.852)
addscore('Hakeem Olajuwon',1993,0.660)
addscore('Michael Jordan',1993,0.577)
addscore('Patrick Ewing',1993,0.366)
addscore('Dominique Wilkins',1993,0.055)
addscore('David Robinson',1993,0.034)
addscore('Shaquille ONeal',1993,0.031)
addscore('Karl Malone',1993,0.010)
addscore('Mark Price',1993,0.010)
addscore('Brad Daugherty',1993,0.001)
addscore('Clyde Drexler',1993,0.001)
addscore('Joe Dumars',1993,0.001)         
addscore('Shawn Kemp',1993,0.001)
addscore('John Stockton',1993,0.001)
       
         
### 1991 - 1992 ### 

addscore('Michael Jordan',1992,0.938)
addscore('Clyde Drexler',1992,0.584)
addscore('David Robinson',1992,0.351)
addscore('Karl Malone',1992,0.273)         
addscore('Patrick Ewing',1992,0.104)
addscore('Chris Mullin',1992,0.084)
addscore('Mark Price',1992,0.069)
addscore('Tim Hardaway',1992,0.067)
addscore('Scottie Pippen',1992,0.033)
addscore('Dennis Rodman',1992,0.027)
addscore('Brad Daugherty',1992,0.025)
addscore('Charles Barkley',1992,0.019)         
addscore('John Stockton',1992,0.019)
addscore('Larry Bird',1992,0.003)
addscore('Kevin Johnson',1992,0.002)
addscore('Danny Manning',1992,0.001)  
addscore('Detlef Schrempf',1992,0.001)         
         
### 1990 - 1991 ###

addscore('Michael Jordan',1991,0.928)
addscore('Magic Johnson',1991,0.518)
addscore('David Robinson',1991,0.496)
addscore('Charles Barkley',1991,0.231)
addscore('Karl Malone',1991,0.148)
addscore('Clyde Drexler',1991,0.078)
addscore('Kevin Johnson',1991,0.033)
addscore('Dominique Wilkins',1991,0.030)
addscore('Larry Bird',1991,0.026)
addscore('Terry Porter',1991,0.026)
addscore('Patrick Ewing',1991,0.021)
addscore('John Stockton',1991,0.016)
addscore('Isiah Thomas',1991,0.011)
addscore('Robert Parish',1991,0.010)
addscore('Joe Dumars',1991,0.008)
addscore('Bernard King',1991,0.007)
addscore('Kenny Smith',1991,0.005)
addscore('Hakeem Olajuwon',1991,0.004)
addscore('Tim Hardaway',1991,0.001)
addscore('Kevin McHale',1991,0.001)


### 1989-1990 ###

add_score('Magic Johnson',1990,0.691)
add_score('Charles Barkley',1990,0.667)
add_score('Michael Jordan',1990,0.613)
add_score('Karl Malone',1990,0.233)
add_score('Patrick Ewing',1990,0.176)
add_score('David Robinson',1990,0.111)
add_score('Hakeem Olajuwon',1990,0.070)
add_score('Tom Chambers', 1990,0.013)
add_score('John Stockton',1990,0.010)
add_score('Larry Bird',1990,0.005)
add_score('Buck Williams',1990,0.005)
add_score('Clyde Drexler',1990,0.003)
add_score('Joe Dumars',1990,0.001)
add_score('Isiah Thomas',1990,0.001)

#Ajout des bilans des équipes


# Choix des feature 


