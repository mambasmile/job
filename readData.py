#coding=utf-8

import json
import pandas as pd

with open(r"nodes.json","r") as json_file:
    nodes = json.load(json_file)

keyword_feature_list = ['keyword_'+str(i) for i in range(0,53)]
venue_feature_list = ['venue_'+str(i) for i in range(0,348)]
allFeatureList = ['id','first','last','num_papers']+keyword_feature_list+venue_feature_list

personFeatureDict = {}
for index,node in enumerate(nodes):
    personFeature = []
    for feature in allFeatureList:
        personFeature.append(node.get(feature,0))
    personFeatureDict[index] = personFeature.copy()
    print(node)

personDF = pd.DataFrame(personFeatureDict)
personDF_T = pd.DataFrame(personDF.values.T,columns=allFeatureList)
personDF_T.to_csv("info.csv",index=False,header=True,columns=allFeatureList)


