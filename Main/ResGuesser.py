from wynnapi import territory_data_extraction
from TickEstimator import ResEstimator, ResExtraction, time_after_previous_tick

data = territory_data_extraction()
time = time_after_previous_tick(data,isPrint=True)

res = ResEstimator(data,time,'Ragni South Entrance',isPrint=True)