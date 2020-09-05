finalURLs = []

with open("sf-house-links-relator.txt", "r") as f:
    i = 1
    for line in f:
        if (i % 3) == 0:
            strippedLine = line.strip()
            finalURLs.append(strippedLine)
            i = 1
        else:
            i += 1

with open("final-sf-house-links-relator.txt", "w") as file:
    for url in finalURLs:
        file.write("https://www.realtor.com{}\n".format(url))
        
