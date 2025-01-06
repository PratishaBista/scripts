def get_digits(prompt):
    """
    Prompt the user to enter exactly five digits and ensure they are valid.
    
    Args:
        prompt (str): The message displayed to the user.

    Returns:
        list: A list of five integers entered by the user.
    """
    while True:
        digits = input(prompt)
        if len(digits) == 5 and all(d.isdigit() for d in digits):
            return [int(d) for d in digits]
        print("Please enter exactly five digits.\n")

def guess_digits():
    """
    A program that predicts the sum of digits based on user inputs and generated numbers.
    
    Steps:
    1. User enters five digits (last digit must be >= 2).
    2. Program predicts the sum of digits.
    3. User enters another set of five digits.
    4. Program calculates a new set of digits summing to 9 with the previous input.
    5. User enters another set of five digits.
    6. Program calculates another set of digits summing to 9 with the most recent input.
    7. Program calculates the final sum and checks if it matches the prediction.
    """
    print(
        "This program tries to guess the sum of digits the user enters!\n\n"
        "Step 1: Enter 5 digits. The last digit must be 2 or more.\n"
        "Step 2: The program will predict the sum of all digits based on your input.\n"
        "Step 3: Enter another set of 5 digits.\n"
        "Step 4: The program generates digits that sum to 9 with your input.\n"
        "Step 5: Repeat this process for more inputs and calculations.\n"
        "Step 6: At the end, the program will calculate the final sum and check if it matches the prediction!\n"
        "Let's start!!\n")
    
     # Step 1
    while True:
        step1_digits = get_digits("Enter the first five digits (last digit must be >= 2): ")
        if step1_digits[-1] >= 2:
            break
        print("The last digit of the first step must be at least 2\n")
            
    guessed_sum = [2] + step1_digits[:-1] + [step1_digits[-1] - 2]
    guessed_sum = ''.join(map(str, guessed_sum))
    print(f"This should be the end result (predicted sum): {guessed_sum}") 

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
