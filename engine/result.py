import sys
sys.path.insert(0, '../engine/')
import exam_helpers

def generate(exam):
	name = input('What is your name? >> ')
	print('\n')
	
	res = exam_helpers.quizzer(exam)

	print("\n\n")
	print('Alright', name ,'Here are your results')
	print("\n")

	max_score = 0
	for k,v in exam.items():
		max_score += v['point']

	score = 0
	for k,v in res.items():
		print(k, ":", exam[k]['question'])
		print("Your Answer:", v['student_answer'])
		print("Correct Answer:", v['right_answer'])
		print("Points Gained:", float(v['points_gained']))
		print('--')

		score+=float(v['points_gained'])
	print("\n")
	print("----------")
	print("\n")
	print("Final score: ", score, " out of ", max_score)
	print("\n")