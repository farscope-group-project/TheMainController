import json
import random

# Read json file. Use ITEM_FINAL to actually select which item! 
with open("apc_seeded_2018.json") as json_file:
    json_data = json.load(json_file)
    bin_list = json_data['bin_contents']

    # Delete items in shelves that are impossible to reach
    del bin_list["bin_J"]
    del bin_list["bin_K"]
    del bin_list["bin_L"]
    
    # Initiate intermediate dictionary
    order_items = {}
    # Make item key, assign value to bin location
    for key, value in bin_list.items():
        for i in value:
                item_in_bin = i
                order_items[i] = key

    # Initiate dictionary to select from
    item_final = {}
    # Delete items that we can't pick up
    for key,value in order_items.items():
        if (key == "dr_browns_bottle_brush") \
           or (key == "kong_air_dog_squeakair_tennis_ball")\
           or (key == "first_years_take_and_toss_straw_cup")\
           or (key == "highland_6539_self_stick_notes"):
            pass
        else:
            item_final[key] = value

    print(item_final) 


# List of items we would rather not pick up:
# dove box of soap ()
# set of cups (first_years_take_and_toss_straw_cup?)
# dog tennis ball (kong_air_dog_squeakair_tennis_ball)
# green book


# How will the target item be picked?
pick_an_item = random.randint(0,10)
target_item = list(item_final.keys())[pick_an_item]
print(target_item)

# All main movement stuff here?

# Assume that target item is dropped into box
success = 1

# On completion of movement, delete item from list
if (success == 1) or (success == 0):
    del item_final[target_item]
else:
    print("Status unknown")
    # Force a value that equals to failure
    success = 0

# Create JSON output file. Output if item picked or not.
item_status = {}
item_status['output'] = []
item_status['output'].append({
    target_item : success
})
with open('picked_status_single.json', 'w') as outfile:
    json.dump(item_status, outfile)
