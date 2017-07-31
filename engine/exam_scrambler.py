import math
import random
import string

encryption_lib = string.ascii_letters+string.digits+string.punctuation+" "

def main_scrambler(exam):
	scr_exam = {}
	for question,data in exam.items():
		scr_exam[question] = data
		for ind in range(len(exam[question]['options'])):
			scr_exam[question]['options'][ind]['answer'] = scrambler(exam[question]['options'][ind]['answer'])
			scr_exam[question]['options'][ind]['w'] = scrambler(str(exam[question]['options'][ind]['w']))
		scr_exam[question]['right_answer'] = scrambler(exam[question]['right_answer'])

	return scr_exam


def scrambler(msg):
	enc_len = len(encryption_lib)
	key = []
	scrambled_msg = ''

	while len(key)<3:
		rand = random.randrange(-enc_len, enc_len)
		key.append(rand)
	
	new_key = key[:]

	if len(msg)>len(key):
		for x in range(len(msg) - len(key)):
			if x<len(key): k=x
			else: k=x%len(key)
			new_key.append(x-key[k])
	
	
	for n in range(len(msg)):
		enc_index = encryption_lib.index(msg[n])
		accum = enc_index+new_key[n]

		if accum<enc_len : new_ind = accum
		else: new_ind = accum%enc_len

		scrambled_msg += encryption_lib[new_ind]

	return (scrambled_msg, key)


def descrambler(msg, key):
	enc_len = len(encryption_lib)
	descrambled_msg = ''
	new_key = key[:]

	if len(msg)>len(key):
		for x in range(len(msg) - len(key)):
			if x<len(key): k=x
			else: k=x%len(key)
			new_key.append(-(key[k]-x))

	for n in range(len(msg)):
		enc_index = encryption_lib.index(msg[n])

		accum = new_key[n]-enc_index
		if math.fabs(accum)<enc_len : new_ind = -accum
		else: new_ind = -(enc_len%accum)

		descrambled_msg += encryption_lib[new_ind]

	return descrambled_msg




def main():
	exam = {
		'question 1':{
			'question': "what is blah?" ,
			'question_type':  'Multiple Choice'  ,
			'options': (
				{'letter':'A', 'answer':'The right answer choice', 'w':'1' },
				{'letter':'B', 'answer':'The wrong answer choice', 'w':'0' },
				{'letter':'C', 'answer':'The partial answer choice', 'w':'0.5' }
			),
			'right_answer':'A',
			'point': 3.0
		}, 
		'question 2':{
			'question': "what is YO?" ,
			'question_type':  'Multiple Choice'  ,
			'options': (
				{'letter':'A', 'answer':'The wrong answer choice', 'w':'0' },
				{'letter':'B', 'answer':'The right answer choice', 'w':'1' },
				{'letter':'C', 'answer':'The partial answer choice', 'w':'0.5' }
			),
			'right_answer':'B',
			'point': 5.0
		}
	}
	scr = main_scrambler(exam)
	print(scr)
	tst = scr['question 1']['right_answer']
	print("descrambled ra: "+ descrambler(tst[0], tst[1]))



if __name__=="__main__":
	main()

