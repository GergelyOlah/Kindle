with open("My_Notes.txt") as note_file:

#Convert file into a list:
    note_list = []
    for line in note_file:
        note_list.append(line.rstrip())

#Extract book tiltes:
    book_titles = set()
    for i in range(len(note_list)):
        if note_list[i].startswith("- Your"):
            book_titles.add(note_list[i-1])

#Create separate note files:
    for title in book_titles:
        with open ("{}.txt".format(title), "w") as note_file:
            for i in range(len(note_list)):
                #pop for removing lines from the list
                if note_list[i].startswith(title):
                    while True:
                        j = i+1
                        if note_list[j].startswith("- Your"):
                            continue
                        elif note_list[j].startswith("==="):
                            break
                        else:
                            note_file.write(j)
                else:
                    continue

