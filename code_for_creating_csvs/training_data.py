import pandas as pd 
import numpy as np
from glob import glob

filenames = glob('./dataset/*.csv')

def append_training_data(filepath):
    df = pd.read_csv(filepath)

    #selecting only 6 overs

    df = df[df['ball']<5.6]

    #removing columns which are not required

    unwanted = ['match_id','season','start_date','batting_team','bowling_team','non_striker','wides','noballs','byes','legbyes','penalty','wicket_type','player_dismissed','other_wicket_type','other_player_dismissed']

    df = df.drop(unwanted,axis = 'columns')

    #splitting tables by innings

    innings1 = df[df['innings'] == 1]

    inningsother = df[df['innings'] == 2]

    batsmen1 = innings1.striker.unique().tolist()
    bowlers1 = innings1.bowler.unique().tolist()

    batsmen2 = inningsother.striker.unique().tolist()
    bowlers2 = inningsother.bowler.unique().tolist()

    #making a dataframe for each inning to train the model later
    data1 = [[innings1.venue.iloc[0],1,",".join(batsmen1),",".join(bowlers1),innings1.runs_off_bat.sum() + innings1.extras.sum()]]
    df1 = pd.DataFrame(data1,columns = ['venue','innings','batsmen','bowlers','total'])

    data2 = [[inningsother.venue.iloc[0],2,",".join(batsmen2),",".join(bowlers2),inningsother.runs_off_bat.sum() + inningsother.extras.sum()]]
    df2 = pd.DataFrame(data2,columns = ['venue','innings','batsmen','bowlers','total'])

    #appending to 'training_data.csv'

    df1.to_csv('training_data.csv',mode = 'a',header = False)
    df2.to_csv('training_data.csv',mode = 'a',header = False)


for x in filenames:
    append_training_data(x[:9]+'/'+x[10:])