if __name__ == '__main__':
    N = int(input())  # Number of commands
    my_list = []

    for _ in range(N):
        command = input().split()
        action = command[0]

        if action == "insert":
            position = int(command[1])
            element = int(command[2])
            my_list.insert(position, element)

        elif action == "print":
            print(my_list)

        elif action == "remove":
            element = int(command[1])
            my_list.remove(element)

        elif action == "append":
            element = int(command[1])
            my_list.append(element)

        elif action == "sort":
            my_list.sort()

        elif action == "pop":
            my_list.pop()

        elif action == "reverse":
            my_list.reverse()
