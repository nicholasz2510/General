def pyramid_of_layers(height, fatness, pyramid_made_of):
    amount = 1
    longest = None
    for x in range(height):
        longest = amount
        amount += fatness
    amount = 1
    for x in range(height):
        do_not_print_this = ""
        print_this = ""
        for y in range(amount):
            do_not_print_this += pyramid_made_of
        for x in range((longest - amount) / 2):
            print_this += " "
        print_this += do_not_print_this
        print print_this
        amount += fatness


pyramid_of_layers(10, 2, "fat ")
