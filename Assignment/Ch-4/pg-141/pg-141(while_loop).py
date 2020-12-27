smoothies = ['coconut',
             'strawberry',
             'banana',
             'tropical',
             'acai berry']

has_coconut = [True,
               True,
               True,
               False,
               True]

length = len(has_coconut)

i = 0
while i < length:
    if has_coconut[i]:
        print(smoothies[i],'contains coconut')
        i = i + 1
