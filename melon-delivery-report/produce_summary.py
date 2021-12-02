def printReport(day, path):
    print(day)
    the_file = open(path)

    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()


printReport("Day 1","um-deliveries-day-1.txt")
printReport("Day 2","um-deliveries-day-2.txt")
printReport("Day 3","um-deliveries-day-3.txt")

