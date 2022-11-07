import re
from collections import Counter
import pickle
import json
import pandas as pd
import re

def words(text):
    if type(text)==str:
        return re.findall(r'\w+',text.lower())

def getDataCounter(df, columns=[]):
    data = df[columns] if columns else df
    
    # load counter.json
    try:
        data_counter = json.load(open('./counter/counter.json', encoding='utf-8'))
    except:
        data_counter = {}
    counter = Counter(data_counter)
    
    # update counter 
    for (col, values) in data.iteritems():
        for value in values:
            counter.update(words(value))
            
    # update counter.json file
    with open('./counter/counter.json','w',encoding='utf-8') as f:
        json.dump(counter,f,ensure_ascii=False,indent=4)
    return counter