def get_digits(prompt):
    while True:
        digits = input(prompt)
        if len(digits) == 5 and all(d.isdigit() for d in digits):
            return [int(d) for d in digits]
        print("Please enter exactly five digits.")

def guess_digits():
    # Step 1
    step1_digits = get_digits("Enter the first five digits (last digit must be >= 2): ")
    if step1_digits[-1] < 2:
        raise ValueError("The last digit of the first step must be at least 2")
    
    guessed_sum = [2] + step1_digits[:-1] + [step1_digits[-1] - 2]
    guessed_sum = ''.join(map(str, guessed_sum))
    print(f"This should be the end result: {guessed_sum}")

    # Step 2
    step2_digits = get_digits("Enter the second five digits: ")

    # Step 3 (calculate digits that sum to 9 with step 2 digits)
    step3_digits = [9 - d for d in step2_digits]
    print(f"Step 3 digits: {''.join(map(str, step3_digits))}")

    # Step 4
    step4_digits = get_digits("Enter the fourth five digits: ")

    # Step 5 (calculate digits that sum to 9 with step 4 digits)
    step5_digits = [9 - d for d in step4_digits]
    print(f"Step 5 digits: {''.join(map(str, step5_digits))}")


    # final sum logic
    final_sum = int(''.join(map(str, step1_digits))) + int(''.join(map(str, step2_digits))) + \
            int(''.join(map(str, step3_digits))) + int(''.join(map(str, step4_digits))) + \
            int(''.join(map(str, step5_digits)))

    print(f"Final sum: {final_sum}")

    if final_sum == int(guessed_sum):
        print("The final sum matches the guessed digits.")
    else:
        print("fixing the code, brb")

guess_digits()
