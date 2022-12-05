def next_round(seat_layout):

    row_len = len(seat_layout[0])
    seat_layout_new = []

    for row_index in range(len(seat_layout)):
        new_row = []
        for seat_index in range(len(seat_layout[row_index])):
            if seat_layout[row_index][seat_index] == ".":
                new_row.append(".")
            else:
                tl, tm, tr = "L", "L", "L"
                ml, __, mr = "L", "L", "L"
                bl, bm, br = "L", "L", "L"

                if row_index-1 != -1:
                    if seat_index-1 != -1:
                        tl = seat_layout[row_index-1][seat_index-1]
                    tm = seat_layout[row_index-1][seat_index]
                    if seat_index+1 != row_len:
                        tr = seat_layout[row_index-1][seat_index+1]

                if seat_index-1 != -1:
                    ml = seat_layout[row_index][seat_index-1]                
                if seat_index+1 != row_len:
                    mr = seat_layout[row_index][seat_index+1]
                
                if row_index+1 != len(seat_layout):
                    if seat_index-1 != -1:
                        bl = seat_layout[row_index+1][seat_index-1]
                    bm = seat_layout[row_index+1][seat_index]
                    if seat_index+1 != row_len:
                        br = seat_layout[row_index+1][seat_index+1]

                surrounding_count = [tl, tm, tr, ml, mr, bl, bm, br].count("#")
                if surrounding_count == 0:
                    new_row.append("#")
                elif surrounding_count >= 4:
                    new_row.append("L")
                else:
                    new_row.append(seat_layout[row_index][seat_index])
        seat_layout_new.append(new_row)
    
    return seat_layout_new

with open("data.txt") as f:
    seat_layout = []
    for l in f.read().split("\n"):
        seat_layout.append([c for c in l])
    row_len = len(seat_layout[0])

    last_occupied_seats = -1
    occupied_seats = 0
    while occupied_seats != last_occupied_seats:
        last_occupied_seats = occupied_seats
        seat_layout = next_round(seat_layout)
        occupied_seats = 0
        for r in seat_layout:
            occupied_seats += r.count("#")
    print(occupied_seats)