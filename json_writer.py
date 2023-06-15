# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 16:28:33 2023

@author: abhia
"""

import json
import pandas as pd

'''
with open("8_videos_Json_test.json", "r") as read_file:
    data = json.load(read_file)
'''

ex_data = pd.read_excel('D:/UNITN work/DEAP Video downloads/Analysis/selected_videos.xlsx');

       
list_data=[{"Batch_wise": []}];



batchsize = 14
for batch_id in range(batchsize):
    a =   {
    "batch_id": batch_id+1,
    "items": []
    }
    
    for i in range(len(ex_data)):
        b = {
          "id": str(ex_data['Online_id'][i]),
          "batch_id": str(batch_id+1),
          "vid_name": str(ex_data['Online_id'][i])+ "-" + str(ex_data['Title'][i]) + ".mp4",
          "Val_scale_range": [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
          "Aro_scale_range": [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
          "textValence": [
            "Please rate the valence"
          ],
          "textArousal": [
            "Please rate the arousal"
          ],
          "trigger": "false"
        }
        a["items"].append(b)
         
    list_data[0]["Batch_wise"].append(a)
        


with open('D:/UNITN work/DEAP Video downloads/Analysis/elicitation_experiment.json', 'w') as fp:
    json.dump(list_data, fp,indent = 3)

        
        
        





