with open("data.txt") as f:

    bags = {}

    for line in f.read().split("\n"):
        container = line.split(" bags contain ")[0]
        contents = []
        if "no other bags" not in line:
            for c in line.split(" bags contain ")[1].split(", "):
                contents.append(c.split(" ")[0] + " " + c.split(" ")[1] + " " + c.split(" ")[2])
        bags[container] = contents

    def search_bag(bags, bag_name, q):
        total_q = 0
        for b in bags[bag_name]:
            quantity = int(b.split(" ")[0])
            total_q += quantity
            bn = " ".join(b.split(" ")[1:])
            total_q += search_bag(bags, bn, quantity)
        return total_q*q

    print(search_bag(bags, "shiny gold", 1))