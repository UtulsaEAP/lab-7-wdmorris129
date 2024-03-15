def exceptionHandling():
    # Split input into 2 parts: name and age
    parts = input().split()
    name = parts[0]
    while name != '-1':
        try: 
            parts = input().split()
            name = parts[0]
            age = int(parts[1])
            age += 1
            print(f'{name} {age}')
        except ValueError:
            print(f'Invalid age for {name}')
            
        
        # Get next line
        parts = input().split()
        name = parts[0]

if __name__ == '__main__':
    exceptionHandling()