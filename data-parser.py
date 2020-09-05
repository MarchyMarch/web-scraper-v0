from bs4 import BeautifulSoup

cardLinks = []

for fileNumber in range(15):
    print("--- Processing file {} ---".format(fileNumber))

    if fileNumber == 0:
        pass
    else:
        fileObj = open("listingObjs-{}.txt".format(fileNumber), "r")
        fileIn = fileObj.read()
        content = BeautifulSoup(fileIn, "html.parser")
        currentCardLinks = content.find_all(class_="list-card-link")

        # print(currentCardLinks)
        cardLinks.extend(currentCardLinks)

print("--- Writing Links to File ---")
with open("card-links.txt", "w") as f:
    for link in cardLinks:
        f.write("{}\n".format(link))

print("--- Done Parsing Links ---")
