# Higher Lower Game

- **TASK 1** : Print logo and welcome screen
- **TASK 2** : Get the first data to compare form the data.py module and store it in a variable - *data1*
- **TASK 3** : Get the second data to compare form the data.py module and store it in a variable - *data2*
- **TASK 4** : Print the VS. logo from art.py module
- **TASK 5** : Print the 'name', 'description', and 'country from data1 to compare against data2
- **TASK 6** : Print the 'name', 'description', and 'country from data2 to compare against data1
- **TASK 7** : Display a prompt: Who's more popular? Type 'A' or 'B':


## My solution
```
def get_random_data(data=game_data, check=[]):
    pick_data = random.choice(data)
    while pick_data in check:
        pick_data = random.choice(data)
    item = pick_data    
    return item

game_over = False
compared_data = []

data1 = get_random_data(check=compared_data)
compared_data.append(data1)
data2 = get_random_data(check=compared_data)
compared_data.append(data2)

score = 0 

while not game_over:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo[1])
    if score:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {data1['name']}, a {data1['description']}, from {data1['country']}.")
    print(logo[3])
    print(f"Against B: {data2['name']}, a {data2['description']}, from {data2['country']}.")
    user_choice = input("Who's more popular? Type 'A' or 'B': ").upper()


    if data1['follower_count'] == data2['follower_count']:
        result = 'win'
    elif data1['follower_count'] > data2['follower_count']:
        result = 'A'
    elif data1['follower_count'] < data2['follower_count']:
        result = 'B'

    # check if user win
    if user_choice == result:
        score += 1
        data1 = data2
        data2 = get_random_data(check=compared_data)
        compared_data.append(data2)
    elif result == 'win':
        score += 1
        data1 = data2
        data2 = get_random_data(check=compared_data)
        compared_data.append(data2)
    else:
        os.system('cls')
        print(logo[1])
        print(f"Oops, that's wrong. Final score: {score}")
        game_over = True



```
