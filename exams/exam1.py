import sys
sys.path.insert(0, '../engine/')

import exam_scrambler
import exam_helpers

name = input('What is your name?')

# Use and scramber and put the result here
exam = {}

result = exam_helpers.answer_eval(exam)









# -------------------------------

print('Here are your results')

max_score = 0
for k,v in exam:
	max_score += v['points']

score = 0
for k,v in result.items():
	print(k, ":")
	print("Your Answer:", v['student_answer'])
	print("Correct Answer:", v['right_answer'])
	print("Points Gained:", float(v['points_gained']))
	print('--')

	score+=float(v['points_gained'])

print("----------")
print("Final score: ", score, " out of ", max_score)

