Tower = {0: 0,
         1: 100,
		 2: 300,
		 3: 600,
		 4: 1200,
		 5: 2400,
		 6: 4800,
		 7: 8400,
		 8: 12000,
		 9: 15600,
		 10: 19200,
		 11: 22800}

Aura = {0: 0,
        1: 800,
        2: 1600,
        3: 3200}

Volley = {0: 0,
          1: 200,
          2: 400,
          3: 800}

Strong_Minion = {0: 0,
                 1: 200,
                 2: 400,
                 3: 800,
                 4: 1600}

Multihit = {0: 0,
            1: 5000}

def DefensePrediction(res):
    ore = res[1]
    crop = res[2]
    wood = res[3]
    fish = res[4]
    best_ore_approx = [-100000,0,0]
    best_crop_approx = [-100000,0,0]
    best_wood_approx = [-100000,0,0]
    best_fish_approx = [-100000,0,0]
    for key2, value2 in Volley.items():
        for key, value in Tower.items():
            temp_approx = [value + value2, key, key2]
            if temp_approx[0] <= 1.15*ore and temp_approx[0] >= 0.85*ore and abs(temp_approx[0]-ore) < abs(best_ore_approx[0]-ore):
                best_ore_approx = temp_approx
    for key2, value2 in Aura.items():
        for key, value in Tower.items():
            temp_approx = [value + value2, key, key2]
            if temp_approx[0] <= 1.15*crop and temp_approx[0] >= 0.85*crop and abs(temp_approx[0]-crop) < abs(best_crop_approx[0]-crop):
                best_crop_approx = temp_approx
    for key2, value2 in Strong_Minion.items():
        for key, value in Tower.items():
            temp_approx = [value + value2, key, key2]
            if temp_approx[0] <= 1.15*wood and temp_approx[0] >= 0.85*wood and abs(temp_approx[0]-wood) < abs(best_wood_approx[0]-wood):
                best_wood_approx = temp_approx
    for key2, value2 in Multihit.items():
        for key, value in Tower.items():
            temp_approx = [value + value2, key, key2]
            if temp_approx[0] <= 1.15*fish and temp_approx[0] >= 0.85*fish and abs(temp_approx[0]-fish) < abs(best_fish_approx[0]-fish):
                best_fish_approx = temp_approx
    predicted_defs = [best_ore_approx, best_crop_approx, best_wood_approx, best_fish_approx]
    return predicted_defs