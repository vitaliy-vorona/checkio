import json

data = """
        "SuperMaxCapacity" =0
        "MaxCapacity": +4540;
        'CurrentCapacity'=   2897,
        "LegacyBatteryInfo" = {"Amperage"=18446744073709550521,"Flags"=4,"Capacity"=4540,"Current"=2897,"Voltage"=7283,"Cycle Count"=406}
        "MegaMaxCapacity" = 6700
"""


def get_battery_level(data):
    index_m = data.find('"MaxCapacity": +') + len('"MaxCapacity": +')
    index_c = data.find("'CurrentCapacity'=   ") + len("'CurrentCapacity'=   ")

    max_capacity = int(data[index_m : index_m + 4])
    curr_capacity = int(data[index_c : index_c + 4])

    percentage = round(100.0 * (curr_capacity / max_capacity), 2)

    return str(percentage) + "%"


"CurrentCapacity / MaxCapacity"

print(get_battery_level(data))
