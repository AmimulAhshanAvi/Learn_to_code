scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
         34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 67,
         46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

#lets find the highest score
high_score = 0
length = len(scores)
for i in range(length):
    print('bubble solution#' + str(i), scores[i])
    if scores[i] > high_score:
        high_score = scores[i];

print('Bubble tests:', length)
print('Highest Bubble tests:', high_score)

#lets find the highest index score
best_solution = []
for i in range(length):
    if high_score == scores[i]:
        best_solution.append(i);

print('solution with the highest score:', best_solution)



#lets find the lowest score
lowest_score = max(scores)
for i in range(length):
    if scores[i] < lowest_score:
        lowest_score = scores[i];
print('The lowest score is:', lowest_score)


#lets find the lowest index
lowest_index = []
for i in range(length):
    if lowest_score == scores[i]:
        lowest_index.append(i);

print('The lowest index is:', lowest_index)
