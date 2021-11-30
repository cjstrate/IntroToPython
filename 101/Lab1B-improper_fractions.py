#Carter Strate
#CSCI 101-Section G
#Week 1 - Part B
#References: Assignment details for formating
#Time: 15 minutes

numerator = int(input('Input the numerator of the improper fraction.\nNUMERATOR> '))
denominator = int(input('Input the denominator of the improper fraction.\nDENOMINATOR> '))

mixed_number_coefficent = numerator//denominator
mixed_number_fraction = numerator%denominator

print(f'{numerator}/{denominator} as a mixed fraction is:\nOUTPUT {mixed_number_coefficent} {mixed_number_fraction}/{denominator}')
