def ResExtraction(terr_data):
    res_data = terr_data['resources']
    res_types = ['EMERALD','ORE','CROP','WOOD','FISH']
    generation = []
    storage = []
    limit = []
    for res in res_types:
        specific_res_data = next((r for r in res_data if r.get('type') == res), None)
        if specific_res_data:
            generation.append(specific_res_data['generation'])
            storage.append(specific_res_data['stored'])
            limit.append(specific_res_data['limit'])
        else:
            generation.append(0)
            storage.append(0)
            limit.append(0)
    return generation,storage,limit

def time_after_previous_tick(data,isPrint=False):
    calculated_times = []
    list_of_cities = ['Ragni','Nemract','Detlas','Troms','Nesaak','Lusuco','Lutho','Llevigar','Olux','Gelibord','Cinfras','Thesead','Thanos','Kandon-Beda','Rodoroc','Ahmsord','Selchar','Corkus City','Espren','Hyloch','Aldwell']
    for city in list_of_cities:
        if city is None:
            continue
        generation, storage, limit = ResExtraction(data[city])
        if limit[1] == 1200:
            usage_per_hour = 800
        elif limit[1] == 2400:
            usage_per_hour = 3000
        else:
            continue
        generation_per_hour = generation[0]
        current_ems_storage = storage[0]
        time_estimation = (current_ems_storage - usage_per_hour/60) / (generation_per_hour/3600 - usage_per_hour/3600)
        calculated_times.append(time_estimation)
    import statistics
    median_time = round(statistics.mode(calculated_times))
    if isPrint:
        print(f"Estimated time after previous resource tick: {median_time} seconds")
    return median_time

def ResEstimator(data,time,terr_name,isPrint=False):
    generation, storage, limit = ResExtraction(data[terr_name])
    usage_list = []
    def print_usages(usage_list):
        print("Estimated emerald usage per hour: ",usage_list[0])
        print("Estimated ore usage per hour: ",usage_list[1])
        print("Estimated crop usage per hour: ",usage_list[2])
        print("Estimated wood usage per hour: ",usage_list[3])
        print("Estimated fish usage per hour: ",usage_list[4])

    for i in range(0, len(generation)):
        generation_per_hour = generation[i]
        current_storage = storage[i]
        usage_per_hour = (current_storage - generation_per_hour*time/3600) * 3600 / (60-time)
        usage_list.append(usage_per_hour)

    if isPrint:
        print_usages(usage_list)