from pprint import pprint

dictionary = {
    "city": "Москва",
    "temperature": "20"
}
dictionary["temperature"] = int(dictionary["temperature"]) - 5
pprint(dictionary)
print(dictionary.get("country", "Россия"))
dictionary["date"] = "27.05.2019"
print(len(dictionary))
