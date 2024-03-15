"""Will Morris, Friday Afternoon"""

def exceptionHandling():
    name_parts = input().split()
    while name_parts[0] != '-1':
        try:
            if len(name_parts) >= 2:
                name = name_parts[0]
                age = int(name_parts[1]) + 1
                print(f'{name} {age}')
            else:
                print("Invalid input format")
        except ValueError:
            print(f'{name_parts[0]} 0')
        
    
        name_parts = input().split()

if __name__ == '__main__':
    exceptionHandling()