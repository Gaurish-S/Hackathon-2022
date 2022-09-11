def dictionary_to_list(list_of_dict):
    new_list = []
    for item in list_of_dict:
        new_list.append([
            item["location"], 
            item["temp"], 
            item["pH"],
            item["DO"],
            item["conductivity"],
            item["BOD"],
            item["nitrate_n_nitrite"],
            item["fecal_coliform"]
        ])
    return new_list

if __name__ == "__main__":
    test = [
        {'a' : 'apple', 'b' : 'bee', 'c' : 'cat'},
        {'a' : 'avocado', 'b' : 'bear', 'c' : 'cobra'},
    ]
    new_list = dictionary_to_list(test)
    for key in new_list:
        print(key)