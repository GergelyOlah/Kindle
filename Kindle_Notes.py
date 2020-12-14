note_file = open("My_Notes.txt")


for line in note_file:
    print(type(line))
        
note_file.close()