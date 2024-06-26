import time
import generate_board as gb

# Generate many boards and analyze the number of attempts to create each one
# Store boards and attempts counts in a new list
# Boards are created as 'board_objects' which are a two element list. The element is the 2d array game board. 
# The second element is the number of attempts the script took to generate a valid board



def generate_board_container(n):
    board_container = []
    for i in range(n): board_container.append(gb.create_board())
    return board_container



def get_generation_attempts(n):
    start_time = time.time()
    board_container = generate_board_container(n)
    attempt_list = [i[1] for i in board_container]
    average_attempts = sum(attempt_list)/n
    execution_time = time.time() - start_time   
    max_attempts = max(attempt_list)

    #print(attempt_list)
    print(n, 'boards generated in an average of', str(average_attempts), 'attempts to generate.') 
    print('The board that took the longest required', max_attempts, 'attempts to generate.')
    print('Execution took', "%.4f seconds" % (execution_time))
    print('Average time to generate a board:', '%.4f seconds' % (execution_time/n))

    # for board_object in board_container: gb.print_board_object(board_object)


get_generation_attempts(10000)

