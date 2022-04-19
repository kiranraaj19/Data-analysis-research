import pickle
import pandas as pd 
import numpy as np
import math as ma

df = pd.read_csv('inputFile.csv')
with open('model_pickle','rb') as f:
    mp = pickle.load(f)

def hashed_data(x,constraint,wanted,filepath):
    df = pd.read_csv(filepath)
    result = df[df[constraint] == x][wanted]
    return result

def predict(predictArray):
    return mp.predict(predictArray)
    

def predictRuns(testInput):
    prediction = 0
        
    current = df.iloc[0].tolist()
    
    batsmen = current[4].split(',')
    bowlers = current[5].split(',')
    
    predictArray = [[list(hashed_data(current[0],'venue','runs_off_bat','./used_for_hashing/venue_ease.csv'))[0],np.mean([hashed_data(x,'striker','runs_off_bat','./used_for_hashing/batsmen_power.csv') for x in batsmen]),np.mean([hashed_data(x,'bowler','weakness_coeff','./used_for_hashing/bowlers_weakness.csv') for x in bowlers])]]
    prediction = predict(predictArray)
    
    return ma.floor(prediction)
