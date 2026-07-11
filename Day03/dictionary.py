customer = {
"name": "Almaz Bekele",
"balance": 1500, # ETB
"city": "Addis Ababa",
}
customer["name"] # "Almaz Bekele"
customer["balance"] = 2000 # update a value
customer.get("phone", "N/A") # safe access, no KeyError
print (customer)