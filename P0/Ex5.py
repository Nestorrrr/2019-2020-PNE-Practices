from Seq0 import seq_count

can_continue = False
while not can_continue:
    user_input = input('Type here a valid file: ')
    FILENAME = user_input + '.txt'
    if user_input == 'stop':
        can_continue = True
    else:
        FOLDER = "../Session_04/"

        DNA_file = FOLDER + FILENAME

        seq_count(DNA_file,user_input)