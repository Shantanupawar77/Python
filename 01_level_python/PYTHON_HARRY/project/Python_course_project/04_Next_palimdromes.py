
def reverse_it(input_number):
    # This is a function to reverse any number
    input_number = str(input_number)
    rev_number = input_number[::-1]
    return int(rev_number)


if __name__ == '__main__':
    n = int(input("How many numbers to input? "))
    inp = []
    for i in range(n):
        inp.append(int(input("Enter any number: ")))

    for number in inp:
        org_number = number
        while True:
            rev_number = reverse_it(org_number)
            if org_number == rev_number:
                break
            else:
                org_number += 1
        print("The next Palindrome number of", number, "is", rev_number)