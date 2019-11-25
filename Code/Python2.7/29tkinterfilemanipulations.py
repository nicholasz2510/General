import Tkinter
import tkMessageBox
import re


def longest_line(s):
    longest = ""
    for line in s:
        if len(line) > len(longest):
            longest = line
    return longest


def longest_token(s):
    longest = ""
    for line in s:
        for token in re.split('\W+|-', line):
            if len(token) > len(longest):
                longest = token
    return longest


def token_count(s, t):
    count = 0
    for line in s:
        for token in re.split('\W+|,|;|\.', line):
            if token == t:
                count += 1
    return count


def token_line_count(s, n):
    count = 0
    for line in s:
        if len(re.split('\W+|,|;|\.', line)) == n:
            count += 1
    return count


def first_vowel_index(s):  # For convert_to_pig_latin(); from 27methodlibrary.py
    if len([False for x in s if x not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]) == len(s):
        return -1
    return [x for x in range(len(s)) if s[x] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']][0]


def to_pig_latin(s):  # For convert_to_pig_latin(); from 27methodlibrary.py
    if len([False for x in s if x not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]) == len(s):
        return s
    elif s[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        return s + "way"
    else:
        return s[first_vowel_index(s):len(s)] + s[:first_vowel_index(s)] + "ay"


def convert_to_pig_latin(words):  # Not in original assignment; from 27methodlibrary.py
    final_words = ""
    for x in words.split():
        final_words += to_pig_latin(x) + " "
    return final_words


def increment_relationship_graph(characters, graph, indices):
    for character in characters:
        for c in characters:
            if character != c:
                graph[indices[character]][indices[c]] += 1
                graph[indices[c]][indices[character]] += 1


def relationship_graph(characters, f):
    text = ""
    graph = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]
    character_numbers = {"Harry": 0, "Hermione": 1, "Ron": 2, "Malfoy": 3, "Dumbledore": 4, "Snape": 5}
    for line in f:
        text += line
    for sentence in re.split("\.+|,", text):
        characters_in_sentence = set()
        for word in re.split("\W+|,|-|;|\"", sentence):
            if word in characters:
                characters_in_sentence |= {word}
        increment_relationship_graph(characters_in_sentence, graph, character_numbers)
    graph_in_text = ""
    for character in characters:
        for c in characters:
            if c != character and c + " + " + character not in graph_in_text:
                graph_in_text += character + " + " + c + ": " + str(
                    graph[character_numbers[character]][character_numbers[c]]) + "\n"
    return graph_in_text


file1 = '29(file1)'
file2 = '29(file2)'
file3 = '29(file3)'

f1 = open(file1)
f2 = open(file2)
f3 = open(file3)

top = Tkinter.Tk()

top.wm_title("File Manipulations")
top.wm_minsize(500, 450)

var1 = Tkinter.StringVar()
var2 = Tkinter.StringVar()
var3 = Tkinter.StringVar()
var4 = Tkinter.StringVar()
var5 = Tkinter.StringVar()
var6 = Tkinter.StringVar()
var7 = Tkinter.StringVar()
var8 = Tkinter.StringVar()
label1 = Tkinter.Message(top, textvariable=var1, width=1000)
label2 = Tkinter.Message(top, textvariable=var2, width=1000)
label3 = Tkinter.Message(top, textvariable=var3, width=1000)
label4 = Tkinter.Message(top, textvariable=var4, width=1000)
label5 = Tkinter.Message(top, textvariable=var5, width=1000)
label6 = Tkinter.Message(top, textvariable=var6, width=1000)
label7 = Tkinter.Message(top, textvariable=var7, width=1000)
label8 = Tkinter.Message(top, textvariable=var8, width=1000)


def longest_line_call_back_f1():
    f1.seek(0)
    tkMessageBox.showinfo("Longest line in \"Pride and Prejudice\"", longest_line(f1))


def longest_line_call_back_f2():
    f2.seek(0)
    tkMessageBox.showinfo("Longest line in \"A Tale of Two Cities\"", longest_line(f2))


def longest_token_call_back_f1():
    f1.seek(0)
    tkMessageBox.showinfo("Longest token in \"Pride and Prejudice\"", longest_token(f1))


def longest_token_call_back_f2():
    f2.seek(0)
    tkMessageBox.showinfo("Longest token in \"A Tale of Two Cities\"", longest_token(f2))


def token_count_call_back(title, f):
    f1.seek(0)
    new_window1 = Tkinter.Tk()
    new_window1.wm_title("Input a token")
    entry = Tkinter.Entry(new_window1, bd=5)
    entry.pack(side=Tkinter.RIGHT)

    def message():
        tkMessageBox.showinfo("Times a token appears in \"" + title + "\"",
                              str(token_count(f, entry.get())) + " times")
        new_window1.destroy()

    entry_label = Tkinter.Label(new_window1, text="What token would you like to search for?")
    entry_label.pack(side=Tkinter.LEFT)
    enter_button = Tkinter.Button(new_window1, text="Enter", command=message)
    enter_button.pack(side=Tkinter.RIGHT)
    new_window1.mainloop()


def token_count_call_back_f1():
    token_count_call_back("Pride and Prejudice", f1)


def token_count_call_back_f2():
    token_count_call_back("A Tale of Two Cities", f1)


def token_line_count_callback(title, f):
    f1.seek(0)
    new_window1 = Tkinter.Tk()
    new_window1.wm_title("Input an integer")
    entry = Tkinter.Entry(new_window1, bd=5)
    entry.pack(side=Tkinter.RIGHT)

    def message():
        tkMessageBox.showinfo("Times a line with " + entry.get() + " tokens appears in \"" + title + "\"",
                              str(token_line_count(f, int(entry.get()))) + " times")
        new_window1.destroy()

    entry_label = Tkinter.Label(new_window1, text="What is the length of the lists would you like to search for?")
    entry_label.pack(side=Tkinter.LEFT)
    enter_button = Tkinter.Button(new_window1, text="Enter", command=message)
    enter_button.pack(side=Tkinter.RIGHT)
    new_window1.mainloop()


def token_line_count_call_back_f1():
    token_count_call_back("Pride and Prejudice", f1)


def token_line_count_call_back_f2():
    token_count_call_back("A Tale of Two Cities", f2)


def convert_to_pig_latin_call_back_f1():
    f1.seek(0)
    file_in_pig_latin = open('Idepray andway Ejudicepray.txt', 'w')
    for line in f1:
        file_in_pig_latin.write(convert_to_pig_latin(line) + "\n")


def relationship_graph_call_back_f3():
    tkMessageBox.showinfo("Relationship graph for \"Harry Potter and the Sorcerer's Stone\"",
                          relationship_graph({"Harry", "Hermione", "Ron", "Malfoy", "Dumbledore", "Snape"}, f3))


var1.set("Please click a button")
var2.set("Find the longest line:")

longest_line_button_f1 = Tkinter.Button(top, text="Find longest line in \"Pride and Prejudice\"",
                                        command=longest_line_call_back_f1)
longest_line_button_f2 = Tkinter.Button(top, text="Find longest line in \"A Tale of Two Cities\"",
                                        command=longest_line_call_back_f2)

var3.set("Find the longest token:")

longest_token_button_f1 = Tkinter.Button(top, text="Find longest token in \"Pride and Prejudice\"",
                                         command=longest_token_call_back_f1)
longest_token_button_f2 = Tkinter.Button(top, text="Find longest token in \"A Tale of Two Cities\"",
                                         command=longest_token_call_back_f2)

var4.set("Find the number of appearances of a token:")

token_count_button_f1 = Tkinter.Button(top, text="Find number of appearances of a token in \"Pride and Prejudice\"",
                                       command=token_count_call_back_f1)
token_count_button_f2 = Tkinter.Button(top, text="Find number of appearances of a token in \"A Tale of Two Cities\"",
                                       command=token_count_call_back_f2)

var5.set("Find the number of lines with a number of tokens:")

token_line_count_button_f1 = Tkinter.Button(top,
                                            text="Find number of lists with the same number of tokens in \"Pride and Prejudice\"",
                                            command=token_line_count_call_back_f1)

token_line_count_button_f2 = Tkinter.Button(top,
                                            text="Find number of lists with the same number of tokens in \"A Tale of Two Cities\"",
                                            command=token_line_count_call_back_f2)

var6.set("Create a new file in Pig Latin:")

convert_to_pig_latin_button_f1 = Tkinter.Button(top, text="Convert \"Pride and Prejudice\" into Pig Latin",
                                                command=convert_to_pig_latin_call_back_f1)

var7.set("Create a relationship graph with all the characters:")

relationship_graph_button_f3 = Tkinter.Button(top, text="\"Harry Potter and the Sorcerer's Stone\" Relationship Graph",
                                              command=relationship_graph_call_back_f3)

label1.pack()
label2.pack()
longest_line_button_f1.pack()
longest_line_button_f2.pack()
label3.pack()
longest_token_button_f1.pack()
longest_token_button_f2.pack()
label4.pack()
token_count_button_f1.pack()
token_count_button_f2.pack()
label5.pack()
token_line_count_button_f1.pack()
token_line_count_button_f2.pack()
label6.pack()
convert_to_pig_latin_button_f1.pack()
label7.pack()
relationship_graph_button_f3.pack()
top.mainloop()

f1.close()
f2.close()
f3.close()
