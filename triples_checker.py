print('Welcome to the Pythagorean Triples Checker.' '\n' '\n'
      'This simple program checks to see whether your choice of' '\n'
      'three side-lengths are able to form a right-angled triangle.')

happy_message = 'Yes! These are the sides of a right-angled triangle.'
neutral_message = 'These sides do not form a right-angled triangle.'
sad_message = 'Try again with exactly three positive numbers, separated by commas.'
to_play = '~ Go again, or q to quit ~'
or_not_to_play = 'Thanks for using the Pythagorean Triples Checker!'
no = 'pls no'


while True:
    sides = input('\n' 'Enter three side-lengths separated by commas: ')
    three_sides = sides.split(',')
    if sides == 'q':
        print('\n', or_not_to_play)
        break
    elif len(three_sides) != 3:
        print('\n', sad_message)
    elif '-' in sides:
        print('\n', sad_message)
    else:
        try:
            s = [float(x) for x in three_sides]
        except ValueError:
            print('\n', sad_message)
        if all(x for x in s) == 0:
            print('\n', no)
        elif (s[0])**2 + (s[1])**2 == (s[2])**2:
            print('\n', happy_message, '\n' '\n', to_play)
        elif (s[1])**2 + (s[2])**2 == (s[0])**2:
            print('\n', happy_message, '\n' '\n', to_play)
        elif (s[2])**2 + (s[0])**2 == (s[1])**2:
            print('\n', happy_message, '\n' '\n', to_play)
        else:
            print('\n', neutral_message, '\n' '\n', to_play)
