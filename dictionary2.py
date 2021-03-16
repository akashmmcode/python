country = int(input("input : "))

places = []
for i in range(country):
    t = {"country":input("country : "), "capital":input("capital : "),"currency":input("currency : ")}
    places.append(t)

# y = input("input a country to search capital : ")


# for x in range(country):
#     if (places[x]["country"]) == y:
#         print(places[x]["capital"])
#     else:
#         print("not a valid input")
#     continue    

while True:
    y = input("input a country to search capital : ")
    for x in range(country):
        if (places[x]["country"]) == y:
            print(places[x]["capital"])
        