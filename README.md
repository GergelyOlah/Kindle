# Kindle Book Highlight Organiser

![Raw Note](/Images/Kindle.PNG)

## About the application
I created this program because I love reading on my Kindle and over the years I collected significant amount of quotes and highligths from the books I read. However, Kindle stores all these highlights in a single text file, regardless of which book you highlighted them from, which makes it quite hard to find quotes later on. To make matters worse, Kindle floods this file with metadata before each end every quote. Reading this format is sluggish and frustrating since the valuable text and the metadata visually blends together like this:

![Raw Note](/Images/Kindle_Notes_Raw.PNG)

This application parses through the text file saved by Kindle, and purges the notes from the metadata and line separators, then stores your highlights separately in text files named by the relevant book titles. This way revisiting your favourite quotes will be swift and easy:

![Raw Note](/Images/Kindle_Notes_Purged.PNG)

## How to use
1. Copy the file containing the highlights (**_My Clippings.txt_**) from your Kindle to a folder.
2. Copy the **_Kindle_Notes.py_** to the same folder as above.
3. Run the the below command with with _Python Version 3.0+_:
```
    python3 Kindle_Notes.py
``` 
4. All the quotes and highlights are now separated by book titles and stored in standalone files.
