import string
import timeit
import os
start = timeit.timeit()

#Title simplifier:
def simplifier(words):
    """Removes special characters."""    
    for character in string.punctuation:
        words = words.replace(character, "")
    return(words)

#Open note:
notes = input("Type the name of the file containing your highlights if it is different from the default (My Clippings.txt). Otherwise hit ENTER. \n")
if len(notes) < 1: notes = "My Clippings.txt" 

with open(notes, errors="ignore") as note_file:

#Convert file into a list:
    note_list = []
    for line in note_file:
        note_list.append(line.rstrip())

#Extract book tiltes:
    book_titles = set()
    for i in range(len(note_list)):
        if note_list[i].startswith("- Your"):
            book_title = note_list[i-1]
            book_titles.add(book_title)

#Create destination directory:
    try:
        os.makedirs("Highlights")
    except OSError:
        pass

#Create separate note files:
    for title in book_titles:
        
        file_name = simplifier(title) + ".txt"
        path = os.path.join(os.getcwd(), "Highlights", file_name)

        with open (path, "w") as fhandle:
            for i in range(len(note_list)):
                #pop for removing lines from the list
                j = i
                if note_list[i].startswith("{}".format(title)):
                    while True:
                        j += 1
                        if note_list[j].startswith("- Your"):
                            continue
                        elif note_list[j].startswith("==="):
                            fhandle.write("\n")
                            fhandle.write(60*"=")
                            break
                        else:
                            fhandle.write(note_list[j])
                            fhandle.write("\n")
                else:
                    continue

end = timeit.timeit()

print("Your Kindle highlights are in the following folder: {}\n".format(os.path.join(os.getcwd(), "Highlights")))
print("Time elapsed: {} s".format(round(end - start,5)))