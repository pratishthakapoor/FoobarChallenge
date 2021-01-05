def minHenchmenCount(total_lambs, henchmen_num, current_lambs, last_lambs):
    total_lambs -= 1

    while total_lambs > 0:
        if total_lambs < current_lambs * 2:
            if total_lambs > current_lambs + last_lambs:
                henchmen_num += 1
            break
        henchmen_num += 1
        current_lambs, last_lambs = current_lambs* 2, current_lambs
        total_lambs -= current_lambs
        #print(henchmen_num)
    return henchmen_num



def maxHenchmenCount(total_lambs, henchmen_num, current_lambs, last_lambs):
    total_lambs -= 1

    while total_lambs > 0:
        if total_lambs < current_lambs + last_lambs:
            break;
        henchmen_num += 1
        current_lambs, last_lambs = current_lambs + last_lambs, current_lambs
        total_lambs -= current_lambs 
        #print(henchmen_num)
    return henchmen_num



def solution(total_lambs):
    #intial count is 1 as there will be atleast one hechmen in the team
    henchmen_num = 1
    # since the junior henchmen can have only 1 lamb so current_lamb is set to 1
    current_lambs = 1
    # value of the last lamb given to the henchmam
    last_lambs = 0

    # returns the difference between the minimum and maximum no of henchmen who can share the lamb
    return (maxHenchmenCount(total_lambs, henchmen_num, current_lambs, last_lambs) - 
minHenchmenCount(total_lambs, henchmen_num, current_lambs, last_lambs))

print(solution(10))
print(solution(143))
