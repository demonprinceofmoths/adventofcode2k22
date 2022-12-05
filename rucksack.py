def main():
    sum_one = 0
    sum_two = 0
    group = []
    print("parsing data...")
    with open("rucksack_data.txt") as f:
        while True:
            data = f.readline()
            if data == "":
                break
            else:
                if len(group) < 3:
                    group.append(data)
                first = data[:len(data)//2]
                second = data[len(data)//2:]
                dupe = find_dupes(first, second)
                #print("Dupe: " + str(dupe))
                priority = prioritize(dupe)
                #print("Priority: " + str(priority))
                sum_one += priority
                if len(group) == 3:
                    dupe_two = find_dupes_three(group.pop(), group.pop(), group.pop())
                    priority = prioritize(dupe_two)
                    sum_two += priority
    print("Sum One: " + str(sum_one))
    print("Sum Two: " + str(sum_two))
def find_dupes(a, b):
    for x in range(len(a)):
        for y in range(len(b)):
            if a[x] == b[y]:
                return a[x]

def find_dupes_three(a, b, c):
    for x in range(len(a)):
        for y in range(len(b)):
            for z in range(len(c)):
                if a[x] == b[y] == c[z]:
                    return a[x]

def prioritize(letter):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if letter.islower():
        for x in range(len(alpha)):
            if alpha[x] == letter:
                #print("X: " + str(x))
                return int(x+1)
    else:
        #print("uppercase!")
        for x in range(len(alpha)):
            if alpha[x] == letter.lower():
                #print("X: " + str(x))
                return int(x+27)

main()
