import json

# Read json file
with open("apc_seeded_2018.json") as json_file:
    json_data = json.load(json_file)

    bin_list = json_data['bin_contents']
    #print(bin_list)
    for var in bin_list:
        x = {var['bin_E']}
        #print(y)
    # What items are located in bin A
    items_bin_A = json_data["bin_contents"]["bin_A"]
    #print(items_bin_A)


# List of items we would rather not pick up:

# dove box of soap ()
# set of cups (first_years_take_and_toss_straw_cup?)
# dog tennis ball (kong_air_dog_squeakair_tennis_ball)
# green book

# The shelves that are impossible to get to:
