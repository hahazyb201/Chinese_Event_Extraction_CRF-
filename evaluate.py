# coding: utf-8
from sklearn.metrics import classification_report
import numpy as np

# Create a mapping of labels to indices
labels = {"SUBJECT": 0, "CONDITION": 1, 'BEHAVIOR': 2, 'RESULT': 3, 'KEY': 4, 'FORBIDDEN': 5, 'RIGHT': 6, 'OBLIGATION': 7, 'O': 8}
truth=[]
pred=[]

with open("./result.txt",'r',encoding="UTF-8") as f:
    lines=f.readlines()
    for line in lines:
    	
    	items=line.split()
    	if len(items)==0:
    		continue
    	pred.append(labels[items[-1].replace('B-', '').replace('I-', '')])
    	truth.append(labels[items[-2].replace('B-', '').replace('I-', '')])

if len(pred)!=len(truth):
	print("WTF!!!!!!!!!!!!")

truth=np.array(truth)
pred=np.array(pred)
# Print out the classification report
print('Generating report ...')
report = classification_report(truth, pred,
    target_names=["SUBJECT", "CONDITION", 'BEHAVIOR', 'RESULT', 'KEY', 'FORBIDDEN', 'RIGHT', 'OBLIGATION', 'O'])
print('report:', report)
