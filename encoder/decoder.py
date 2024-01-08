# Branch Metric
# states = { 
#     "00": ["000", "111"], 
#     "01": ["101", "010"], 
#     "10": ["110", "001"], 
#     "11": ["011", "100"]
# }

states = { 
    "00": ["000", "111"], 
    "01": ["001", "110"], 
    "10": ["011", "100"], 
    "11": ["010", "101"]
}

# Path Metric
pathes = {
    "00": ["00", "10"], 
    "01": ["00", "10"], 
    "10": ["01", "11"], 
    "11": ["01", "11"]
}


def binary_string_to_array(input_str):
    while len(input_str) % 3 != 0:
        input_str += '0'
    result_array = [input_str[i:i+3] for i in range(0, len(input_str), 3)]
    return result_array

def compare_bits_with_array(main_str, str_array):
    result_array = []
    for str_in_array in str_array:
        if len(main_str) != len(str_in_array):
            raise ValueError("Input strings must have the same length")
        
        mismatch_count = sum(bit1 != bit2 for bit1, bit2 in zip(main_str, str_in_array))
        result_array.append(mismatch_count)
    return result_array

def combine_two_routes(route1, route2):
    combined_route = {
        "to": route2["to"],
        "value": route1["value"] + route2["value"],
        "dist": route1["dist"] + route2["dist"]
    }
    return combined_route

def check_path(routes, to):
    for route in routes:
        if route["to"] == to:
            return route
    return None  

def drop_duplicates(routes):
    unique_routes = []

    for route in routes:
        duplicate_found = False
        for existing_route in unique_routes:
            if route["to"] == existing_route["to"]:
                if route["dist"] < existing_route["dist"]:
                    existing_route.update(route)
                duplicate_found = True
                break

        if not duplicate_found:
            unique_routes.append(route)

    return unique_routes

def min_dist_value(routes):
    if not routes:
        return None  
    min_dist_route = min(routes, key=lambda x: x["dist"])
    return min_dist_route["value"]


def decode(sequence):
    temp_route = {}
    one_before = {}

    two_routes = []
    four_routes = []
    final_route = ""

    hamming_dist = []
    arr_strings = binary_string_to_array(sequence)

    for i in range(len(arr_strings)):
        eight_routes = []

        if(i == 0):
            hamming_dist = compare_bits_with_array(arr_strings[i], ["000", "111"])
            two_routes.append({
                "to": pathes["00"][0], 
                "value": "0",
                "dist": hamming_dist[0]
            })
            two_routes.append({
                "to": pathes["00"][1], 
                "value": "1",
                "dist": hamming_dist[1]
            })

        elif(i == 1):
            for state in pathes["00"]:
                hamming_dist = compare_bits_with_array(arr_strings[i], states[state])
                one_before = check_path(two_routes, state)
                for index in range(2):
                    temp_route = {
                        "to": pathes[state][index],
                        "value": str(index),
                        "dist": hamming_dist[index]
                    }
                    
                    combined_route = combine_two_routes(one_before, temp_route)
                    
                    four_routes.append(combined_route)

        else:
            for key, value in states.items():
                hamming_dist = compare_bits_with_array(arr_strings[i], value)

                for index in range(len(pathes[key])):  
                    temp_route = {
                        "to": pathes[key][index],
                        "value": str(index),
                        "dist": hamming_dist[index]
                    }
                    one_before = check_path(four_routes, key)
                    combined_route = combine_two_routes(one_before, temp_route)
                    eight_routes.append(combined_route)
            print(eight_routes)
            four_routes = drop_duplicates(eight_routes)
            print(four_routes)

    final_route = min_dist_value(four_routes)

    return final_route
    


        
print("The code bits after correction: ", decode("001110011001"))


