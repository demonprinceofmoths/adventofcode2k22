def main():
    sum = 0
    print("parsing data...")
    with open("rucksack_data.txt") as f:
        while True:
            data = f.readline()
            if data == "":
                break
            else:
                first = data[:len(data)//2]
                second = data[len(data)//2:]
                dupe = find_dupes(first, second)
                #print("Dupe: " + str(dupe))
                priority = prioritize(dupe)
                #print("Priority: " + str(priority))
                sum += priority
    print("Sum: " + str(sum))
def find_dupes(a, b):
    for x in range(len(a)):
        for y in range(len(b)):
            if a[x] == b[y]:
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
