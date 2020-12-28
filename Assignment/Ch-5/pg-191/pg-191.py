def how_should_i_get_there(miles):
    if miles > 120.0:
        print('Take a plane')
    elif miles >= 2.0:
            print('Take a car')
    else:
        print('walk')

how_should_i_get_there(800.3)
how_should_i_get_there(2.0)
how_should_i_get_there(.5)

#we don't need kilometars parameters
#because it how_should_i_get_there have one arguments
#and it was miles
