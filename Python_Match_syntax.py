
# command = 'Hello World'
# command = 'Goodbye-World'
command = 'Hello Sir'

match command:
    case 'Hello World':
        print("Hello to you too")
    case 'Goodbye-World':
        print("See you soon")
    case _:
        print("No match found")

