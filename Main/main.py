from wynnapi import territory_data_extraction
from TickEstimator import ResEstimator, ResExtraction, time_after_previous_tick
from DefensePredictions import *

data = territory_data_extraction()
time = time_after_previous_tick(data,isPrint=True)
def print_defs(predicted_defs):
    print("Predicted Tower level: ",predicted_defs[0][1],predicted_defs[1][1],predicted_defs[2][1],predicted_defs[3][1])
    print("Predicted Aura level: ",predicted_defs[1][2])
    print("Predicted Volley level: ",predicted_defs[0][2])
    print("Predicted Strong Minion level: ",predicted_defs[2][2])
    print("Predicted Multihit level: ",predicted_defs[3][2])
terr_name = 'Fungal Grove'
res = ResEstimator(data,time,terr_name,isPrint=True)
Predicted_Defs = DefensePrediction(res)
print("For Territory: ", terr_name)
print_defs(Predicted_Defs)