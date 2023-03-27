my_dict = {
    "Name": "Smruti",
    "Age": 22,
    "Qualification": "B.Tech",
    "Branch": "Electrical",
    "Passing_Year": 2022
}
print(my_dict)
print(my_dict.get("Age"))
my_dict["Age"] = 23
print(my_dict)
my_dict.update({"Passing_Year": 2020})
print(my_dict)
my_dict.pop("Age")
print(my_dict)
my_dict.popitem()
print(my_dict)