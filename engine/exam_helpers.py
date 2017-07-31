from exam_scambler import descrambler

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
