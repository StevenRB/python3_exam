def quizzer(exam_dct):
    '''returns student answer, the right answer and point gained'''
    point = 0
    results = dict()
    for question_num, dct_val in exam_dct.items():
        print('{}: {}'.format(question_num, dct_val['question']))
        print('Pick from the options below')
        for option in dct_val['options']:
            print(option['letter']+")", descrambler(option['answer'][0], option['answer'][1]))

        student_a = input('Enter your answer: ')
        results[question_num] = {
                                 'student answer' : student_a, 
                                 'right_answer' : question_num['right_answer'],
                                 'point_gained' : answer_eval(student_a, dct_val)
                                }

    return results