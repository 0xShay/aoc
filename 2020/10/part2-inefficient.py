success_count = 0

def check_possible(outlet, device_adapter_rating, adapter_ratings, route=[]):

    global success_count

    for i in range(1, 4):
        if (outlet+i in adapter_ratings):
            check_possible(outlet+i, device_adapter_rating, adapter_ratings, route+[outlet+i])
    
    if (outlet == device_adapter_rating-3):
        # print(route)
        success_count += 1

with open("data-sample.txt") as f:

    adapter_ratings = list(map(int, f.read().split("\n")))
    device_adapter_rating = max(adapter_ratings) + 3

    check_possible(0, device_adapter_rating, adapter_ratings)

    print(success_count)