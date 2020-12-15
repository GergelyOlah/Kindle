with open("My_Notes.txt") as note_file:

    paragraph = []
    extracted_notes = []
    book_titles = [] 

    for line in note_file:
        if not line.startswith("==="):
            paragraph.append(line)
        else:
            for i in range(len(paragraph)-1,-1,-1):
                if not paragraph[i].startswith("- Your"):
                    extracted_notes.append(paragraph[i])
                else:
                    break

    with open("Notes_Book_3.txt", "w") as extracted_file:
        for line in extracted_notes:
            extracted_file.write(line)
