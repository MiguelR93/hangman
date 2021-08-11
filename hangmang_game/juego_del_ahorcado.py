def run():
    data = []
    with open("./data.txt", "r", encoding="utf-8") as word:
        for i in word:
            width = len(i) - 1
            data.append(i[:width])
    print(data)
    origin = {n:data[n] for n in range(len(data))}
    print(origin)


if __name__ == "__main__":
    run()    