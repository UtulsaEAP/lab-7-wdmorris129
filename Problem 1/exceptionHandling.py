# def exceptionHandling():
#     name = input().split()[0]
#     while name != '-1':
#         try:
#             parts = input().split()
#             name = parts[0]
#             age = int(parts[1]) + 1
#             print(f'{name} {age}')
#         except ValueError:
#             print(f'{name} 0')
            

# if __name__ == '__main__':
#     exceptionHandling()


def exceptionHandling():
    name_parts = input().split()
    while name_parts[0] != '-1':
        try:
            # Ensure there are enough parts before trying to access them
            if len(name_parts) >= 2:
                name = name_parts[0]
                age = int(name_parts[1]) + 1
                print(f'{name} {age}')
            else:
                print("Invalid input format")
        except ValueError:
            # Output 0 for the age if conversion fails
            print(f'{name_parts[0]} 0')
        
        # Get next line
        name_parts = input().split()

if __name__ == '__main__':
    exceptionHandling()