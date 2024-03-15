def exceptionHandling():
    name = input().split()[0]
    while name != '-1':
        try:
            parts = input().split()
            name = parts[0]
            age = int(parts[1]) + 1
            print(f'{name} {age}')
        except ValueError:
            print(f'{name} 0')
            

if __name__ == '__main__':
    exceptionHandling()