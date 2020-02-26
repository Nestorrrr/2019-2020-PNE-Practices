from Seq0 import seq_complement

can_continue = False
while not can_continue:
    user_input = input('Type here a valid file: ')
    FILENAME = user_input + '.txt'
    if user_input == 'stop':
        can_continue = True
    else:
        FOLDER = "../Session_04/"

        DNA_file = FOLDER + FILENAME

        seq_complement(DNA_file,user_input)