import random

while True:
    all_pieces = []
    for i in range(7):
        for j in range(i, 7):
            all_pieces.append([i, j])

    random.shuffle(all_pieces)

    stock = all_pieces[:14]
    computer = all_pieces[14:21]
    player = all_pieces[21:28]

    highest_core = -1
    status = ""
    start_piece = []

    for piece in computer:
        if piece[0] == piece[1]:
            if piece[0] > highest_core:
                highest_core = piece[0]
                start_piece = piece
                status = "player"

    for piece in player:
        if piece[0] == piece[1]:
            if piece[0] > highest_core:
                highest_core = piece[0]
                start_piece = piece
                status = "computer"

    if status != "":
        if start_piece in computer:
            computer.remove(start_piece)
        else:
            player.remove(start_piece)
        snake = [start_piece]
        break

while True:
    print("======================================================================")
    print("Stock size: " + str(len(stock)))
    print("Computer pieces: " + str(len(computer)))
    print("")

    if len(snake) <= 6:
        snake_string = ""
        for piece in snake:
            snake_string = snake_string + str(piece)
        print(snake_string)
    else:
        first_three = ""
        for i in range(3):
            first_three = first_three + str(snake[i])
        last_three = ""
        for i in range(len(snake) - 3, len(snake)):
            last_three = last_three + str(snake[i])
        print(first_three + "..." + last_three)

    print("")
    print("Your pieces:")
    item_number = 1
    for piece in player:
        print(str(item_number) + ":" + str(piece))
        item_number = item_number + 1
    print("")

    if len(player) == 0:
        print("Status: The game is over. You won!")
        break
    if len(computer) == 0:
        print("Status: The game is over. The computer won!")
        break

    is_draw = False
    if snake[0][0] == snake[-1][1]:
        search_num = snake[0][0]
        count = 0
        for piece in snake:
            if piece[0] == search_num:
                count = count + 1
            if piece[1] == search_num:
                count = count + 1
        if count == 8:
            is_draw = True

    if is_draw:
        print("Status: The game is over. It's a draw!")
        break

    if status == "player":
        print("Status: It's your turn to make a move. Enter your command.")
        user_input = input().strip()

        is_valid = True
        if not user_input:
            is_valid = False
        else:
            if user_input[0] == "-":
                if not user_input[1:].isdigit():
                    is_valid = False
            else:
                if not user_input.isdigit():
                    is_valid = False

        if not is_valid:
            print("Invalid input. Please try again.")
            continue

        move = int(user_input)
        if move < -len(player) or move > len(player):
            print("Invalid input. Please try again.")
            continue

        if move == 0:
            if len(stock) > 0:
                player.append(stock.pop(0))
            status = "computer"
        else:
            left_end = snake[0][0]
            right_end = snake[-1][1]

            if move > 0:
                chosen = player[move - 1]
                if chosen[0] == right_end:
                    player.pop(move - 1)
                    snake.append(chosen)
                    status = "computer"
                elif chosen[1] == right_end:
                    player.pop(move - 1)
                    chosen[0], chosen[1] = chosen[1], chosen[0]
                    snake.append(chosen)
                    status = "computer"
                else:
                    print("Illegal move. Please try again.")
                    continue
            else:
                chosen = player[abs(move) - 1]
                if chosen[1] == left_end:
                    player.pop(abs(move) - 1)
                    snake.insert(0, chosen)
                    status = "computer"
                elif chosen[0] == left_end:
                    player.pop(abs(move) - 1)
                    chosen[0], chosen[1] = chosen[1], chosen[0]
                    snake.insert(0, chosen)
                    status = "computer"
                else:
                    print("Illegal move. Please try again.")
                    continue

    else:
        print("Status: Computer is about to make a move. Press Enter to continue...")
        input()

        counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        for piece in computer:
            counts[piece[0]] = counts[piece[0]] + 1
            counts[piece[1]] = counts[piece[1]] + 1
        for piece in snake:
            counts[piece[0]] = counts[piece[0]] + 1
            counts[piece[1]] = counts[piece[1]] + 1

        scored_pieces = []
        for i in range(len(computer)):
            piece = computer[i]
            score = counts[piece[0]] + counts[piece[1]]
            scored_pieces.append([score, i, piece])

        for i in range(len(scored_pieces)):
            for j in range(i + 1, len(scored_pieces)):
                if scored_pieces[i][0] < scored_pieces[j][0]:
                    scored_pieces[i], scored_pieces[j] = scored_pieces[j], scored_pieces[i]

        left_end = snake[0][0]
        right_end = snake[-1][1]

        moved = False
        for item in scored_pieces:
            orig_index = item[1]
            p = item[2]

            if p[0] == right_end or p[1] == right_end:
                computer.pop(orig_index)
                if p[0] != right_end:
                    p[0], p[1] = p[1], p[0]
                snake.append(p)
                moved = True
                break
            elif p[0] == left_end or p[1] == left_end:
                computer.pop(orig_index)
                if p[1] != left_end:
                    p[0], p[1] = p[1], p[0]
                snake.insert(0, p)
                moved = True
                break

        if not moved:
            if len(stock) > 0:
                computer.append(stock.pop(0))

        status = "player"