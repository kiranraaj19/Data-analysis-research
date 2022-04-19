import pandas as pd 
import numpy as np
from glob import glob

def hashed_data(x,constraint,wanted,filepath):
    df = pd.read_csv(filepath)
    result = df[df[constraint] == x][wanted]
    return result

df = pd.read_csv('training_data.csv')

record = []

for x in range(967):
    current = df.iloc[x].tolist()
    records = [[hashed_data(current[0],'venue','runs_off_bat','venue_ease.csv'),current[1],np.mean([hashed_data(x,'striker','runs_off_bat','batsmen_power.csv') for x in list(current[2].split(","))]),np.mean([hashed_data(x,'bowler','weakness_coeff','bowlers_weakness.csv') for x in list(current[3].split(","))]),current[4]]]
    df2 = pd.DataFrame(records,columns = ['venue','innings','batsmen','bowlers','total'])
    df2.to_csv('hashed_training_data.csv',mode = 'a',header = False)

#dataset now in hashed_training_data.csv