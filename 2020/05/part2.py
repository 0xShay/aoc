with open("data.txt") as f:

    seat_ids = []

    for line in f.read().split("\n"):

        row_min = 0
        row_max = 127
        for a in line[0:7]:
            if a == "F":
                row_max = (row_min + row_max) // 2
            elif a == "B":
                row_min = (row_min + row_max) // 2

        col_min = 0
        col_max = 7
        for a in line[7:10]:
            if a == "L":
                col_max = (col_min + col_max) // 2
            elif a == "R":
                col_min = (col_min + col_max) // 2

        seat_ids.append((row_max * 8) + col_max)

    last_sid = sorted(seat_ids)[0]

    for sid in sorted(seat_ids):
        if sid > last_sid+1:
            print(f"Seat ID {last_sid+1} is missing")
        last_sid = sid
