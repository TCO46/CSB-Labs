high_score_list = [80, 82, 73, 74, 84, 94]

high_score_list.sort(reverse=True)
print("High score: ")
for i in range(len(high_score_list)):
    i+=1
    print(f"{i}. {high_score_list[i-1]}")