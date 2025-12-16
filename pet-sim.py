health = 100
hunger = 20
happiness = 70
actions = ["eat", "sleep", "play", "exit"]
action = ""
while True:
    action = ""
    if health <= 0: break
    if hunger == 100:
        health -= 15
        happiness -= 10
    if happiness < 25: health -= 10
    if hunger < 0: hunger = 0
    if happiness < 0: happiness = 0
    print(f"health: {health} hunger: {hunger} happiness: {happiness}")
    while action not in actions: action = input('what do you want to do? (eat) (sleep) (play) (exit) ')
    if action == "eat":
        hunger -= 5
        happiness -= 5
    if action == "play":
        happiness += 15
        hunger += 10
    if action == "sleep":
        health += 5
        hunger += 15
    if action == "exit": break