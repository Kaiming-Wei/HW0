#Kaiming Wei
#Afternoon 1pm



from tkinter import *
from turtle import *

interface = Tk()
interface.resizable(width = False, height = False)
interface.geometry('{}x{}'.format(250, 250))

# Add widgets
title = "Word Frequency Chart"
about = Label(interface, text =title)
about.grid(row=0, column=0, padx=(25), pady=(10, 10))
instruction = Label(interface, text ="Enter n below:\n(0 <= n <= 54)")
instruction.grid(row=1, column=0, padx=(25), pady=(10, 10))
entry = Entry(interface, bd = 5)
entry.grid(row=2, column=0, padx=(25), pady=(10, 10))

n = 0

def submit():
    global n
    n = int(entry.get())
    interface.destroy()

button = Button(interface, text ="Draw Pie chart", command = submit)
button.grid(row=3, column=0, padx=(25), pady=(10, 10))
interface.mainloop()

# Sort a dictionary by word frequency
def sort_dict_by_occurence(unsorted_dict):
    sorted_dict = sorted(unsorted_dict.items(), key = lambda t: t[1], reverse = True)
    return sorted_dict

lower_chars = "abcdefghijklmnopqrstuvwxyz"
upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_counts = {}

with open("Words.txt", 'r') as f:
    word_list = f.readlines()

for line in word_list:
    for c in line:
        if c == ' ' or c == '\n' or c == '\t':
            continue
        if c in lower_chars or c in upper_chars:
            c = c.lower()
        if c in letter_counts:
            letter_counts[c] += 1
        else:
            letter_counts[c] = 1

letter_counts = sort_dict_by_occurence(letter_counts)

# Add up all frequencies.
sum_of_freq = 0
for key in letter_counts:
    sum_of_freq += key[1]

n_freqs = {}
other_prob = 1
for i in range(n):
    probability = letter_counts[i][1]/sum_of_freq
    other_prob -= probability
    n_freqs[letter_counts[i][0]] = probability

n_freqs = sort_dict_by_occurence(n_freqs)
#---------------------------------------------------------------------

' Construction of pie chart '
#---------------------------------------------------------------------
' radius of the pie chart circle and color choices for 26 letters '
r = 130
colors = ["peachpuff", "aquamarine", "lightgoldenrodyellow",
          "pink", "yellow", "sandybrown", "cornflowerblue", "lightgreen",
          "greenyellow", "lightcoral", "mediumpurple", "steelblue",
          "khaki", "powderblue", "lightsalmon", "lime", "hotpink",
          "burlywood", "violet", "skyblue", "tan", "palegreen",
          "silver", "coral", "beige", "palegoldenrod"]

# draws the initial circle
penup()
goto(0,-r)
pendown()
circle(r)
penup()
up()
goto(0,0)
pendown()

if n >= 1: #segment drawing for n = 1
    fillcolor(colors[0])
    begin_fill()
    fd(r)
    left(90)
  # calculation of arc length is divided by 2 to
  # label the segment in the center of the arc '''
    # half arc is drawn
    circle(r, n_freqs[0][1]*360/2)
    # segment labeled at that point
    if xcor() > 0:
        write(n_freqs[0][0]+", "+str(n_freqs[0][1]), align="left", font=("Arial", 11, "bold"))
    else:
        write(n_freqs[0][0]+", "+str(n_freqs[0][1]), align="right", font=("Arial", 11, "bold"))
    # second half of arc is drawn
    circle(r, n_freqs[0][1]*360/2)
    position = pos()
    goto(0,0)
    end_fill()
    if n > 1: #segment drawings for n > 1
        for i in range(1, n):
            fillcolor(colors[i])
            begin_fill()
            goto(position)
            circle(r, n_freqs[i][1]*360/2)
            if xcor() > 0:
                write(n_freqs[i][0]+", "+str(n_freqs[i][1]), align="left", font=("Arial", 11, "bold"))
            else:
                write(n_freqs[i][0]+", "+str(n_freqs[i][1]), align="right", font=("Arial", 11, "bold"))
            circle(r, n_freqs[i][1]*360/2)
            position = pos()
            goto(0,0)
            end_fill()
    # drawing of "All other characters" segment
    if other_prob != 0:
        fillcolor('lightgrey')
        begin_fill()
        goto(position)
        circle(r, other_prob*360/2)
        if xcor() > 0:
            write("All other letters, "+str(other_prob), align="left", font=("Arial", 11, "bold"))
        else:
            write("All other letters, "+str(other_prob), align="right", font=("Arial", 11, "bold"))
        circle(r, other_prob*360/2)
        position = pos()
        goto(0,0)

else: #construction of pie chart if n = 0
    penup()
    fd(r)
    left(90)
    pendown()
    fillcolor('lightgrey')
    begin_fill()
    circle(r)
    write("All other letters, "+str(other_prob), align="left", font=("Arial", 11, "bold"))
# End drawing pie chart

#ends the drawing of final segment
end_fill()
done()
