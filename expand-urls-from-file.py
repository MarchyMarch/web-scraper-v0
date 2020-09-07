expanded_URLs = []

print("--- Expanding URLs ---")

with open("urls-to-expand.txt", "r") as f:
    for line in f:
        strippedLine = line.strip()
        print("----- Expanding {} ------".format(strippedLine))
        for i in range(15):
            if i ==0:
                pass
            elif i == 1:
                expanded_URLs.append(strippedLine)
            else:
                url = strippedLine + "pg-{}".format(i)
                expanded_URLs.append(url)

with open("expanded-urls.txt", "w") as f:
    for url in expanded_URLs:
        f.write("{}\n".format(url))

print("---- Done Expanding ----")
