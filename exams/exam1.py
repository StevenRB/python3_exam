import sys
sys.path.insert(0, '../engine/')

import exam_scrambler
import exam_helpers

name = input('What is your name?')

exam1 = {}

result = exam_helpers.answer_eval(exam1)









# -------------------------------

print('Here are your results')

max_points = 0
for n in exam1:
	
	
score = 0
for k,v in result.items():
	print(k, ":")
	print("Your Answer:", v['student_answer'])
	print("Correct Answer:", v['right_answer'])
	print("Points Gained:", v['points_gained'])
	print('--')

	score+=v['points_gained']

print("----------")
print("Final score: ", score)

