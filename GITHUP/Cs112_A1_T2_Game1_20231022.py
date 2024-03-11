# File : Cs112_A1_T2_Game1_20231022.py
""" Purpose : that game is plying by 2 players each player choose a number from 1 to 10 and who reaches 100
at first wins """
# Author : Asmaa Sayed Mohammed
# ID : 20231022
# Initialize the sum of numbers
sum = 0
# Welcome message and display the game information
print("Welcome to the 100 game! Have a nice time.")
print("The sum is currently 0.")
# The game loop continues until the sum reaches or exceeds 100
while sum < 100:
    # Player 1's turn
    plyer1_num = input("Player 1: Please insert a number from 1 to 10: ")
    # Check if the input is a valid number
    if not plyer1_num.isdigit():
        print("Please insert a valid number.")
        continue
    plyer1_num = int(plyer1_num)
    # Check if the input number is within the valid range
    if plyer1_num > 10 or plyer1_num < 1:
        print("Please insert a valid number between 1 and 10.")
        continue
    # Add the input number to the sum
    sum += plyer1_num
    print(f'Now we have {sum}')
    # Check if Player 1 has reached 100 and declare them as the winner
    if sum == 100:
        print("Player 1 is the winner!")
        exit()
    # Check if the sum exceeds 100, and adjust the sum accordingly
    while sum > 100:
        sum -= plyer1_num
        print('The sum must be less than or equal to 100.')
        plyer1_num = int(input('Please insert a number which is smaller than the previous number: '))
        sum += plyer1_num
        if sum == 100:
            print('Player 1 is the winner!')
            exit()
    # Player 2's turn
    while True:
        player2_num = input("Player 2: Please insert a number from 1 to 10: ")
        if not player2_num.isdigit():
            print("Please insert a valid number.")
            continue
        player2_num = int(player2_num)
        # Check if the input number is within the valid range
        if player2_num > 10 or player2_num < 1:
            print("Please insert a valid number between 1 and 10.")
            continue
        else:
            break
    # Add the input number to the sum
    sum += player2_num
    print(f'Now we have {sum}')
    # Check if Player 2 has reached 100 and declare them as the winner
    if sum == 100:
        print("Player 2 is the winner!")
        exit()
    # Check if the sum exceeds 100, and adjust the sum accordingly
    while sum > 100:
        sum -= player2_num
        print('The sum must be less than or equal to 100.')
        player2_num = int(input('Please insert a number which is smaller than the previous number: '))
        sum += player2_num
        if sum == 100:
            print('Player 2 is the winner!')
            exit()
