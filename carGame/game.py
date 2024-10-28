print("Enter help")
help = input()
if help == "help":
    print("start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit")

    steps = 3
    current_step = 0
    while current_step < steps:
        step_input = str(input())
        if step_input == "start":
           current_step += 1
           print("Car started ... Ready to go!")
        elif step_input == "stop":
            current_step += 1
            print("Car stopped")
        elif step_input == "quit":
             break
        else:
            print("I don't understand that!")
