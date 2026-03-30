travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C","D"]]
print(nested_list[2][1])

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

dict["c"] = [1, 2, 3]
print(dict)

order = {
    "starter": {
        1: "Salad",
        2: "Soup"
    },
    "main": {
        1: ["Burger", "Fries"],
        2: ["Steak"]
    },
    "dessert": {
        1: ["Ice Cream"],
        2: []
    },
}
print(order["main"][2][0])