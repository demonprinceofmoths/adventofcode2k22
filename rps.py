def main():
    print("parsing data...")
    score = 0
    with open("rps_data.txt") as f:
        while True:
            data = f.readline()
            if data == "":
                break
            else:
                opp, me = data.split(" ")
                score += score_match(opp, me)
    print("Final score: " + str(score))

def score_match(o, m):
    choice_score = 0
    win_score = 0
    # a beats z, b beats x, c beats y
    #if i choose rock
    if m.strip("\n") == "X":
        choice_score = 1
        if o == "C":
            win_score = 6
        elif o == "A":
            win_score = 3
    # if i choose paper
    if m.strip("\n") == "Y":
        choice_score = 2
        if o == "A":
            win_score = 6
        elif o == "B":
            win_score = 3
    #if i choose scissors
    if m.strip("\n") == "Z":
        choice_score = 3
        if o == "B":
            win_score = 6
        elif o == "C":
            win_score = 3
    return choice_score + win_score


main()
