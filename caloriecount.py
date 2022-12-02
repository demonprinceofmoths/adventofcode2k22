def main():
  print("Counting calories...");
  elves = []
  with open('cc_data.txt') as f:
      elf = 0
      while True:
          data = f.readline();
          if data == "":
              break
          else:
              if data =="\n":
                  elves.append(elf)
                  elf = 0
              else:
                  elf += int(data)
  print("sorting data...")
  elves = merge_sort(elves)
  print("Highest calories: " + str(elves[len(elves)-1]))
  print("Top three elves:")
  print("1: " + str(elves[len(elves)-1]))
  print("2: " + str(elves[len(elves)-2]))
  print("3: " + str(elves[len(elves)-3]))
  total = elves[len(elves)-1] + elves[len(elves)-2] + elves[len(elves)-3]
  print("Total: " + str(total))

def merge_sort(a):
    # recursive algorithm to merge sort two lists
    if(len(a) == 1):
        #if there is only one number in the list, return it
        return a
    else:
        #otherwise, split and sort
        left = a[:len(a)//2]
        right = a[len(a)//2:]
        left = merge_sort(left)
        right = merge_sort(right)
        #return the newly sorted list
        return merge(left, right)

def merge(l, r):
    n = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            n.append(l[i])
            i+=1
        else:
            n.append(r[j])
            j+=1
    while i < len(l):
        n.append(l[i])
        i+=1
    while j < len(r):
        n.append(r[j])
        j+=1
    return n


main()
