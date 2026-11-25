N = int(input())
age = int(input())

if N:
    print('WOMAN' if age >= 19 else 'GIRL')
else:
    print('MAN' if age >= 19 else 'BOY')