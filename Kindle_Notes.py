note_file = open("My_Notes.txt")

paragraph = []
extracted_notes = []

for line in note_file:
    if not line.startswith("==="):
        paragraph.append(line)
    else:
        for i in range(len(paragraph)-1,-1,-1):
            if not paragraph[i].startswith("- Your"):
                extracted_notes.append(paragraph[i])
            else:
                break

print(extracted_notes)

note_file.close()