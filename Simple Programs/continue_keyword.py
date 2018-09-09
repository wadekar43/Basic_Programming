def continue_test():
    while True:
        s = input('Enter something:')
        if s == 'saurabh':
            break
        if len(s) < 5:
             print('Tooo small')
             continue
        print("Input is of sufficient length")
continue_test()