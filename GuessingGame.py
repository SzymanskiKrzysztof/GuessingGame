import random

print("Hello in Guesses Game!")
print("Rules:")
print("Give int number from 1 to 100")
print("Check how many takes it You")

# Start program
winner_num = random.randint(1, 101)
num_player = int(input("Give You number: "))

count = [num_player]
if winner_num == num_player:
    print(f"You Win and it takes only {len(count)} guess!")
elif 0 < abs(winner_num - num_player) <= 10:
    print("WARM")
else:
    print("COLD")

while num_player != winner_num:
    num_player = int(input("Give You next number: "))
    count.append(num_player)

    if num_player < 1 or num_player > 100:
        print("OUT OF BOUNDS")
    else:
        if num_player == winner_num:
            print(f"You Win and it takes only {len(count)} guess!")
            break
        elif abs(winner_num - num_player) <= abs(winner_num - count[-2]):
            print("WARMER")
        else:
            print("COLDER")
