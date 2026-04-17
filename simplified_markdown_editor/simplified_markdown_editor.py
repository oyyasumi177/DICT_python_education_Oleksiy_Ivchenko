formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line", "ordered-list", "unordered-list"]
special_commands = ["!help", "!done"]
full_content = ""

while True:
    user_input = input("Choose a formatter: ")

    if user_input == "!done":
        with open("output.md", "w", encoding="utf-8") as f:
            f.write(full_content)
        break

    elif user_input == "!help":
        print("Available formatters:", " ".join(formatters))
        print("Special commands:", " ".join(special_commands))
        continue

    elif user_input not in formatters:
        print("Unknown formatting type or command")
        continue

    if user_input == "header":
        level = int(input("Level: "))
        if not (1 <= level <= 6):
            print("The level should be within the range of 1 to 6")
            continue
        text = input("Text: ")
        full_content += "#" * level + " " + text + "\n"

    elif user_input in ["ordered-list", "unordered-list"]:
        while True:
            n_rows = int(input("Number of rows: "))
            if n_rows > 0:
                break
            print("The number of rows should be greater than zero")

        for i in range(1, n_rows + 1):
            row_text = input(f"Row #{i}: ")
            if user_input == "ordered-list":
                full_content += f"{i}. {row_text}\n"
            else:
                full_content += f"* {row_text}\n"

    elif user_input == "plain":
        full_content += input("Text: ")
    elif user_input == "bold":
        full_content += f"**{input('Text: ')}**"
    elif user_input == "italic":
        full_content += f"*{input('Text: ')}*"
    elif user_input == "inline-code":
        full_content += f"`{input('Text: ')}`"
    elif user_input == "link":
        full_content += f"[{input('Label: ')}]({input('URL: ')})"
    elif user_input == "new-line":
        full_content += "\n"

    print(full_content)