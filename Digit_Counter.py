num = int(input("Enter a number: "))
def digits(n):
    digit_counter = 0
    string = ""
    for i in range(1, n, 1):
        string += str(i)
        i += 1
    return len(string)
print(digits(num))