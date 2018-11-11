i = 1
list_of_terms = input('Enter name of file: ')
with open(list_of_terms) as f_in:
    with open('new.txt', 'w') as f_out:
        while i < 10:
            term = input('Term:')
            a = len(term)
            for line in f_in:
                if line.startswith(term, 0, a+1):
                    print(line, end='')
                    f_out.write(line)
            f_out.write('\n')
