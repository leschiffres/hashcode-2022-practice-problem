from parse import parse_file
from algorithms import get_file_specs, greedy_search, incremental_greedy_search
from submit import submit
import datetime
filenames = ['a_an_example.in.txt', 'b_basic.in.txt', 'c_coarse.in.txt', 'd_difficult.in.txt', 'e_elaborate.in.txt']
for filename in filenames:

    print('-'*100)
    print(filename)
    print('-'*100)
    input_path = 'input/' + filename
    output_path = 'output/' + filename
    # read data
    clients = parse_file(input_path)
    # run algorithm to get desired output
    get_file_specs(clients)
    
    print(f'Start of the algorithm: {datetime.datetime.now()}')
    
    # ingredients = greedy_search(clients)
    ingredients = incremental_greedy_search(clients)
    
    print(f'End of the algorithm: {datetime.datetime.now()}')
    # store output in the proper file
    submit(output_path, ingredients)

    print(f'Stored file {output_path} for input file: {filename}')
