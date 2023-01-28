def strip_punctuation_ru(data):
    data = data.replace(",", " ").replace("!", " ").replace(".", " ").replace("?", " ")
    data = data.split()
    ans = ""
    for i in range(len(data)):
        while data[i] and data[i][-1] in ".,?!-=":
            data[i] = data[i][:-1]
        if data[i]:
            ans += data[i] + " "
    return ans[:-1]


def check():
    flag = True
    data = (
        ("", ''),
        ("??????!!!!....,,,,,", ''),
        ("Привет! Чем занимаешься? Петя, пойдем гулять! Ты не пойдешь??!! Пока, Петя. Ты - бобр",
         "Привет Чем занимаешься Петя пойдем гулять Ты не пойдешь Пока Петя Ты бобр"),
    )
    for inp, ans in data:
        if flag:
            try:
                ans1 = strip_punctuation_ru(inp)
            except Exception:
                print("NO")
                flag = False
            else:
                if ans1 != ans:
                    print(inp, ans1, ans, sep="\n")
                    print("NO")
                    flag = False
    if flag:
        print("YES")

print(strip_punctuation_ru("jddsgd,sdfef.dfds"))
check()