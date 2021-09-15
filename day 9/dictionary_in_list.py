travel_log =[
    {
        "country": "France",
        "visits":12,
        "cities":["Paris","Lille","Dijon"]
    },
    {
        "country": "Germany",
        "visits":5,
        "cities":["Berlin","Hamburg","Stuttgart"]
    }
]

def add_new_country(country ,visit,city):
    new_log ={}
    new_log["country"]= country
    new_log["visits"]= visit
    new_log["city"]= city
    print(new_log)
    travel_log.append(new_log)
    print(travel_log)
add_new_country("Russia",2,["Moscow","Saint Petersbu"])