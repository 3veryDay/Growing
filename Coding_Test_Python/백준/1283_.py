N = int(input())
set_of_words = set()
dic ={}
answer =''
for _ in range(N) :
    option = input()
    print_with_brackets = ''
    not_printed = True
    for word in option.split() :
        if not_printed and word[0].lower() not in set_of_words :
            print_with_brackets += f'[{word[0]}]{word[1:]} '
            not_printed = False
            set_of_words.add(word[0].lower())
        else :
            print_with_brackets +=word + " "
    if not_printed :
        print_with_brackets = ''
        for char in option :
            if char == " " :
                print_with_brackets += " "
                continue
            if not_printed and char.lower() not in set_of_words :
                print_with_brackets += f'[{char}]'
                not_printed = False
                set_of_words.add(char.lower())
            else :
                print_with_brackets += char
    dic[option] = print_with_brackets
    answer += (print_with_brackets) + '\n'
print(answer)
