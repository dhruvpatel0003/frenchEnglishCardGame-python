from tkinter import *
import pandas as pd
import random as r
COLOR = '#B1DDC6'
############################### Modification #############################################################

window = Tk()
window.config(bg=COLOR,pady=10,padx=10)
window.title('FR-EN')
random_word = 0
newWord,newTitle = None,None

data = pd.read_csv('french_words.csv')
new_french_word = data['French'].to_list()
new_english_word = data['English'].to_list()

canvas = Canvas(width=800,height=526)
image_ = PhotoImage(file='card_front.png')
canvas.create_image(400,263,image=image_)
canvas.config(bg=COLOR,highlightthickness=0)
canva_title = canvas.create_text(400, 150, text='Welcome To Game', font=('Arial', 20, 'bold'))
canva_text = canvas.create_text(400, 263, text='Press Green Button to Start', font=('Arial', 20, 'bold'))
canvas.grid(row=0, column=1)
flage = True
change_i = None
new_dict = {}
new_list_f = []
new_list_e = []
change_flage = True

def know():


    new_f = new_french_word.pop(random_word)
    new_e = new_english_word.pop(random_word)
    new_list_f.append(new_f)
    new_list_e.append(new_e)
    dict = pd.DataFrame({'French': new_list_f, 'English': new_list_e})
    dict.to_csv('modify.csv')
    window.after(5000,func=french)


def stop():

    global flage
    flage = False
    go_(flage)

def french():

    go_(flage)

def go_(flage):

    if flage:
        global random_word,newWord,newTitle
        random_word = r.randint(0,len(new_french_word)-1)
        newWord = new_french_word[random_word]
        newTitle ='French'
        change_image('card_back', newTitle, newWord)
        print('F',newWord)
        window.after(10000,func=change)
    else:
        canvas.destroy()
        window.destroy()

def change():

    newWord = new_english_word[random_word]
    newTitle = 'English'
    print('E', newWord)
    change_image('card_front',newTitle,newWord)
    window.after(5000,func=french)

def change_image(side,title,text):

    global canva_text, canva_title,image_
    image_ = PhotoImage(file=f'{side}.png')
    canvas.create_image(400,263,image=image_)
    canvas.config(bg=COLOR, highlightthickness=0)
    canvas.create_text(400, 150, text=f'{title}', font=('Arial', 20, 'bold'))
    canvas.create_text(400, 263, text=f'{text}', font=('Arial', 20, 'bold'))
    canvas.grid(row=0, column=1)
    return


# window.after(10000,func=go_)
button_0 = PhotoImage(file='wrong.png')
cross_button = Button(image=button_0,highlightthickness=0,highlightcolor=COLOR )
cross_button.grid(row=1,column=0)

button_remember = Button(text="It's known",command= know)
button_remember.grid(row=2,column=1)
button_stop = Button(text='Stop',command=stop)
button_stop.grid(row=1,column=1)

button_1 = PhotoImage(file='right.png')
check_button = Button(image=button_1,highlightthickness=0,highlightcolor=COLOR,command=french)
check_button.grid(row=1,column=2)

window.resizable(FALSE,FALSE)
window.config(pady=20,padx=20)
window.mainloop()