def run():
    data = []
    with open("./data.txt", "r", encoding="utf-8") as word:
        for i in word:
            data.append(str(i))
    print(data)
    origin = {n:data[n] + str(len(data[n])) for n in range(len(data))}
    print(origin)


if __name__ == "__main__":
    run()    