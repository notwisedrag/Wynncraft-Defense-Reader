def territory_data_extraction():
    import requests

    r = requests.get('https://api.wynncraft.com/v3/guild/list/territory')
    data = r.json()
    return data