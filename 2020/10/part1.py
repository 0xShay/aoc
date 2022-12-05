with open("data.txt") as f:
    adapter_ratings = list(map(int, f.read().split("\n")))
    device_adapter_rating = max(adapter_ratings) + 3

    outlet = 0
    ar = {1:0, 2:0, 3:1}

    while outlet != device_adapter_rating-3:
        outlet_found = False
        i = 1
        while i < 4 and not outlet_found:
            if (outlet+i in adapter_ratings):
                ar[i] += 1
                outlet += i
                outlet_found = True
            i += 1

    print(ar)
    print(ar[1] * ar[3])