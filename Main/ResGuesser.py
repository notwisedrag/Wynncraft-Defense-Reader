from wynnapi import territory_data_extraction
from TickEstimator import ResEstimator, ResExtraction, time_after_previous_tick
from DefensePredictions import *

data = territory_data_extraction()
time = time_after_previous_tick(data,isPrint=True)

terr_name = 'Entrance to Nivla Woods'
res = ResEstimator(data,time,terr_name,isPrint=True)
Predicted_Defs = DefensePrediction(res)
print("For Territory: ", terr_name)
print("Predicted Tower level: ",Predicted_Defs[0][1],Predicted_Defs[1][1],Predicted_Defs[2][1],Predicted_Defs[3][1])
print("Predicted Aura level: ",Predicted_Defs[1][2])
print("Predicted Volley level: ",Predicted_Defs[0][2])
print("Predicted Strong Minion level: ",Predicted_Defs[2][2])
print("Predicted Multihit level: ",Predicted_Defs[3][2])