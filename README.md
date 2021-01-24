# Kindle Book Highlight Organiser
## About the application
I created this program because I love reading on my Kindle and over the years I collected significant amount of quotes and highligths from the books I read. However, Kindle stores all these highlights in a single text file, regardless of which book you highlighted them from, which makes it quite hard to find quotes later on. To make matters worse, Kindle floods this file with metadata before each end every quote. Reading this format is sluggish and frustrating since the valuable text and the metadata visally blends together like this:

![Raw Note](/Images/Kindle_Notes_Raw.png)

This application parses through the text file saved by Kindle, and purges the notes from the metadata and line separators, then stores your highlights separately in text files named by the relevant book titles. This way revisiting your favourite quotes will be swift and easy. 

## Manual
1. Copy the file containing the highlights (**__My Clippings.txt__**) from your Kindle to a folder.
2. Copy the **__Kindle_Notes.py__** to the same foldder as above.
3. Run the **__Kindle_Notes.py__** with Python 3.
4. All the quotes and highlights are now separated by book titles and stored in standalone files.
