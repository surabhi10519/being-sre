def reverse(s):
    list1 = s.split()
    list1.reverse()
    print(" ".join(list1))

def numbers(list1):
    start, end = 0, len(list1)-1
    while start < end:
        while list1[start] == 0 and start < end:
            start += 1
        while list1[end] == 1 and start < end:
            end -= 1
        if start < end:
            list1[start],list1[end]= 0,1
            end = end - 1
            start = start + 1
    print list1


def main():
    s = ' I am a Surabhi '
    list1 = [0,1,0,1,0,0,1,1,1,0]
    print('This function reverses a string.')
    reverse(s)
    print('This function prints a string with leading 0s')
    numbers(list1)


if __name__ == '__main__':
    main()
