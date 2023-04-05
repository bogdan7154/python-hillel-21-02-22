if __name__ == '__main__':
    with open('my_text.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines() if 'a' in line.lower()]
        result = [line[line.index('a'):].strip().capitalize() if 'a' in line else '' for line in lines]

    print(result)
