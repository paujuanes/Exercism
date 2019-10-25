def convert(number):
    rainsound = ''
    if number % 3 == 0: rainsound += 'Pling'
    if number % 5 == 0: rainsound += 'Plang'
    if number % 7 == 0: rainsound += 'Plong'
    if not rainsound: rainsound = str(number)
    return rainsound