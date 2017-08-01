from exam_scrambler import descrambler

def quizzer(exam_dct):
    '''returns student answer, the right answer and point gained'''
    point = 0
    results = dict()
    for question_num, dct_val in exam_dct.items():
        print('{}: {}'.format(question_num, dct_val['question']))
        print('Pick from the options below')
        for option in dct_val['options']:
            print(option['letter']+")", descrambler(option['answer'][0], option['answer'][1]))

        print('\n')
        student_a = input('Enter your answer: ')
        
        print('\n')
        results[question_num] = {
                                 'student_answer' : student_a, 
                                 'right_answer' : descrambler(dct_val['right_answer'][0], dct_val['right_answer'][1]),
                                 'points_gained' : answer_eval(student_a, dct_val)
                                }

    return results
  
def answer_eval(student_a, question_dct):
    '''returns point value based on student answer to question'''
    answer = descrambler(question_dct['right_answer'][0], question_dct['right_answer'][1]).lower()
    if student_a.lower() == answer:
        return question_dct['point']
    else:
        for dct in question_dct['options']:
            current_letter = dct['letter'].lower()
            if current_letter == student_a.lower():
                weight = float(descrambler(dct['w'][0], dct['w'][1]))
        return question_dct['point'] * weight

