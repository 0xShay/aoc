def next_round(seat_layout):

    row_len = len(seat_layout[0])
    seat_layout_new = []

    for row_index in range(len(seat_layout)):
        new_row = []
        for seat_index in range(len(seat_layout[row_index])):
            if seat_layout[row_index][seat_index] == ".":
                new_row.append(".")
            else:
                tl, tm, tr = "-", "-", "-"
                ml, __, mr = "-", "-", "-"
                bl, bm, br = "-", "-", "-"

                # tm
                temp_row_index = row_index-1
                while temp_row_index >= 0 and tm == "-":
                    if seat_layout[temp_row_index][seat_index] != ".":
                        tm = seat_layout[temp_row_index][seat_index]
                    temp_row_index -= 1

                # bm
                temp_row_index = row_index+1
                while temp_row_index < len(seat_layout) and bm == "-":
                    if seat_layout[temp_row_index][seat_index] != ".":
                        bm = seat_layout[temp_row_index][seat_index]
                    temp_row_index += 1

                # ml
                temp_seat_index = seat_index-1
                while temp_seat_index >= 0 and ml == "-":
                    if seat_layout[row_index][temp_seat_index] != ".":
                        ml = seat_layout[row_index][temp_seat_index]
                    temp_seat_index -= 1

                # mr
                temp_seat_index = seat_index+1
                while temp_seat_index < row_len and mr == "-":
                    if seat_layout[row_index][temp_seat_index] != ".":
                        mr = seat_layout[row_index][temp_seat_index]
                    temp_seat_index += 1

                # tl
                temp_row_index = row_index-1
                temp_seat_index = seat_index-1
                while temp_row_index >= 0 and temp_seat_index >= 0 and tl == "-":
                    if seat_layout[temp_row_index][temp_seat_index] != ".":
                        tl = seat_layout[temp_row_index][temp_seat_index]
                    temp_row_index -= 1
                    temp_seat_index -= 1
                
                # tr
                temp_row_index = row_index-1
                temp_seat_index = seat_index+1
                while temp_row_index >= 0 and temp_seat_index < row_len and tr == "-":
                    if seat_layout[temp_row_index][temp_seat_index] != ".":
                        tr = seat_layout[temp_row_index][temp_seat_index]
                    temp_row_index -= 1
                    temp_seat_index += 1
                
                # bl
                temp_row_index = row_index+1
                temp_seat_index = seat_index-1
                while temp_row_index < len(seat_layout) and temp_seat_index >= 0 and bl == "-":
                    if seat_layout[temp_row_index][temp_seat_index] != ".":
                        bl = seat_layout[temp_row_index][temp_seat_index]
                    temp_row_index += 1
                    temp_seat_index -= 1

                # br
                temp_row_index = row_index+1
                temp_seat_index = seat_index+1
                while temp_row_index < len(seat_layout) and temp_seat_index < row_len and br == "-":
                    if seat_layout[temp_row_index][temp_seat_index] != ".":
                        br = seat_layout[temp_row_index][temp_seat_index]
                    temp_row_index += 1
                    temp_seat_index += 1

                surrounding_count = [tl, tm, tr, ml, mr, bl, bm, br].count("#")
                if surrounding_count == 0:
                    new_row.append("#")
                elif surrounding_count >= 5:
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