import tkinter as tk 
from saver import *
from encryption.caesar import *
from encryption.azby import *
from encryption.onetimepad import *
from encryption.vigenere import *
import pyperclip as pc
from randomwords import* 
import time
from time import strftime

game_right_solved = False
page_left_solved = False
page_leftdown_solved = False
buttonright_game = None
buttonleft_game = None
buttonleftdown_game = None

def open_cypher_ui_1():  
    global root_1  
    root_1 = tk.Tk()  
    root_1.resizable(False, False)
    root_1.title('your friendly neighborhood cypher ui')
    root_1.configure(bg='lightgray')
    root_1.geometry("1000x600")

    
    w = tk.Label(root_1, text='hello sharon and leon, welcome to my  ui', bg='lightgray')
    w.pack(pady=20)
    leave_button = tk.Button(root_1,)

    buttonin = tk.Button(root_1,text='to the actual encryption station',width=25,activebackground="blue",activeforeground="white",command=open_cypher_ui_2)
    buttonin.pack(pady=10)

    buttonde = tk.Button(root_1,text='to the actual decryption station',width=25,activebackground="blue",activeforeground="white",command=open_decypher_ui_2)
    buttonde.pack(pady=10)


    
    buttongame = tk.Button(root_1,text='to the descriptive murder mystery front page',width=35,activebackground="blue",activeforeground="white",command=open_smm)
    buttongame.pack(pady=10)

    leaderboard_button = tk.Button(root_1,text='show leaderboard',width=25,activebackground="blue",activeforeground="white",command=open_leaderboard)
    leaderboard_button.pack(pady=10)

    img = tk.PhotoImage(file="image\\download.png")
    mini_img=img.subsample(2, 2)
    mini_img_label = tk.Label(root_1, image=mini_img, bg='lightgray')
    mini_img_label.image = mini_img
    mini_img_label.pack(pady=10)

    root_1.mainloop() 
def open_decypher_ui_2():  
    global Lb
    global result
    global entry1
    global entry2 

    
    root_1.destroy()

    root_2 = tk.Tk() 
    root_2.resizable(False, False)
    root_2.title('decryption station')
    root_2.geometry("1000x600")
    root_2.configure(bg='lightgray')

    imgde = tk.PhotoImage(file="image\\decryption.png")
    mini_imgde=imgde.subsample(2, 2)
    mini_imgde_label = tk.Label(root_2, image=mini_imgde, bg='lightgray')
    mini_imgde_label.image = mini_imgde
    mini_imgde_label.pack(pady=10)

    button = tk.Button(root_2,text='back to first page',activebackground="red", activeforeground="white",width=30,command=lambda: [root_2.destroy(), open_cypher_ui_1()])
    button.place(x=10, y=570, anchor='sw')

    button_se = tk.Button(root_2,text="decrypt",activebackground="blue",activeforeground="white",command=on_button_clickde)
    button_se.place(x=600, y=300)

    label = tk.Label(root_2, text="key here if needed:")
    label.place(x=150, y=320)
    entry1 = tk.Entry(root_2, selectbackground="lightblue", selectforeground="black")
    entry1.place(x=150, y=350)

    label = tk.Label(root_2, text="encrypt here:")
    label.place(x=300, y=320)
    
    entry2 = tk.Entry(root_2, selectbackground="lightblue", selectforeground="black")
    entry2.place(x=300, y=350)

    result = tk.StringVar()
    result.set("result for decrypt")

    result_label = tk.Label(root_2,textvariable=result,bg='white',relief='sunken',width=40,anchor='w')
    result_label.place(x=300, y=380)

    label = tk.Label(root_2, text="result here:")
    label.place(x=220, y=380)

    Lb = make_cipher_listbox(root_2, entry1, result, x=10, y=300)
    update_key_field_state(entry1, Lb)
  
    button_copy = tk.Button(root_2,text="copy to clipboard",activebackground="green",activeforeground="white",command=lambda: pc.copy(result.get()))
    button_copy.place(x=600, y=380)
   
    def open_info_ui_1():
        root_info = tk.Tk() 
        root_info.resizable(False, False)
        root_info.title('info abput the ciphers')
        root_info.configure(bg='lightgray')
        root_info.geometry("820x270")
        azbbytext = "azby The Atbash cipher is a simple substitution cipher where the alphabet is reversed. A becomes Z, B becomes Y, and so on.\n Logic: For any letter, replace it with its symmetric partner in the alphabet.\n\n"
        casertext = "The Caesar cipher is a monoalphabetic substitution cipher where each letter in the text is shifted a fixed number of positions down the alphabet.\nLogic: Shift every character by a specific number.\n\n"
        vigeneretext = " Vigenère Cipher This is a polyalphabetic cipher that uses a keyword to shift letters. Unlike Caesar, the shift changes depending on the letter of the keyword.\n Logic: If the keyword is KEY, the first letter of your message shifts by K (10), the second by E (4), the third by Y (24), and then it repeats.\n\n"
        onetimepadtext = " One-Time Pad This is theoretically unbreakable if used correctly. It uses a key that is at least as long as the message, consisting of truly random data.\n Logic: Each character of the plaintext is XORed (exclusive OR) with a character of the key.\n\n"
        infohere = tk.Label(root_info, text='info page for the ciphers:'+'\n\n'+azbbytext+casertext+vigeneretext+onetimepadtext, bg='white')
        infohere.pack()
    button_info = tk.Button(root_2,text="info",activebackground="green",activeforeground="white",command=open_info_ui_1 )
    button_info.place(x=10, y=250)
    root_2.mainloop()
def update_key_field_state(entry, listbox):
    current_selection = listbox.curselection()
    if not current_selection:
        return
    selected_cipher = listbox.get(current_selection[0])
    if selected_cipher == 'azby':
        entry.config(state='normal')
        entry.delete(0, tk.END)
        entry.config(state='disabled')
    else:
        entry.config(state='normal')
        entry.focus_set()


def safe_int(value):
    if isinstance(value, str) and value.isdigit():
        return int(value)
    if isinstance(value, (int, float)):
        return int(value)
    return 0


def on_button_clickde():
    selected_cipher = Lb.get(Lb.curselection()[0])
    sentence = entry2.get()
    if selected_cipher == 'azby':
        answer = azby_decrypt(sentence)
    elif selected_cipher == 'caesar':
        key = safe_int(entry1.get())
        answer = caser_decrypt(sentence, key)
    elif selected_cipher == 'vigenere':
        key = entry1.get()
        answer = vigenere_decrypt(sentence, key)
    elif selected_cipher == 'one_time_pad':
        keyword = entry1.get()
        answer = one_time_pad_decrypt(sentence, keyword)
    else:
        answer = "Unknown cipher"
    result.set(answer)  
def open_cypher_ui_2():  
    global Lb
    global result
    global entry1
    global entry2   

    
    root_1.destroy()

    root_2 = tk.Tk()  
    root_2.resizable(False, False)
    root_2.title('encryption station')
    root_2.geometry("1000x600")
    root_2.configure(bg='lightgray')

    imgen = tk.PhotoImage(file="image\\encryption.png")
    mini_imgen=imgen.subsample(2, 2)
    mini_imgen_label = tk.Label(root_2, image=mini_imgen, bg='lightgray')
    mini_imgen_label.image = mini_imgen
    mini_imgen_label.pack(pady=10)

    button = tk.Button(
        root_2,
        text='back to first page',
        activebackground="red",
        activeforeground="white",
        width=30,
        command=lambda: [root_2.destroy(), open_cypher_ui_1()]
    )
    button.place(x=10, y=570, anchor='sw')

    button_se = tk.Button(
        root_2,
        text="encrypt",
        activebackground="blue",
        activeforeground="white",
        command=on_button_clickin
    )
    button_se.place(x=600, y=300)

    label = tk.Label(root_2, text="key here if needed:")
    label.place(x=150, y=320)
    entry1 = tk.Entry(root_2, selectbackground="lightblue", selectforeground="black")
    entry1.place(x=150, y=350)

    label = tk.Label(root_2, text="sentence here:")
    label.place(x=300, y=320)
    
    entry2 = tk.Entry(root_2, selectbackground="lightblue", selectforeground="black")
    entry2.place(x=300, y=350)

    result = tk.StringVar()
    result.set("result for encrypt")

    result_label = tk.Label(root_2,textvariable=result,bg='white',relief='sunken',width=40,anchor='w')
    result_label.place(x=300, y=380)

    label = tk.Label(root_2, text="result here:")
    label.place(x=220, y=380)

    Lb = make_cipher_listbox(root_2, entry1, result, x=10, y=300)
    update_key_field_state(entry1, Lb)
    
    button_copy = tk.Button(root_2,text="copy to clipboard",activebackground="green",activeforeground="white",command=lambda: pc.copy(result.get()))
    button_copy.place(x=600, y=380)
 
    def open_info_ui_1():
        root_info = tk.Tk()  
        root_info.title('info abput the ciphers')
        root_info.configure(bg='lightgray')
        root_info.geometry("820x270")
        azbbytext = "azby The Atbash cipher is a simple substitution cipher where the alphabet is reversed. A becomes Z, B becomes Y, and so on.\n Logic: For any letter, replace it with its symmetric partner in the alphabet.\n\n"
        casertext = "The Caesar cipher is a monoalphabetic substitution cipher where each letter in the text is shifted a fixed number of positions down the alphabet.\nLogic: Shift every character by a specific number.\n\n"
        vigeneretext = " Vigenère Cipher This is a polyalphabetic cipher that uses a keyword to shift letters. Unlike Caesar, the shift changes depending on the letter of the keyword.\n Logic: If the keyword is KEY, the first letter of your message shifts by K (10), the second by E (4), the third by Y (24), and then it repeats.\n\n"
        onetimepadtext = " One-Time Pad This is theoretically unbreakable if used correctly. It uses a key that is at least as long as the message, consisting of truly random data.\n Logic: Each character of the plaintext is XORed (exclusive OR) with a character of the key.\n\n"
        infohere = tk.Label(root_info, text='info page for the ciphers:'+'\n\n'+azbbytext+casertext+vigeneretext+onetimepadtext, bg='white')
        infohere.pack()
    button_info = tk.Button(root_2,text="info",activebackground="green",activeforeground="white",command=open_info_ui_1 )
    button_info.place(x=10, y=250)
    root_2.mainloop() 
    
 
def on_button_clickin():


    
    selected_cipher = Lb.get(Lb.curselection()[0])
    sentence = entry2.get()
    if selected_cipher == 'azby':
        answer = azby(sentence)
    elif selected_cipher == 'caesar':
        key = safe_int(entry1.get())
        answer = caser(sentence, key)
    elif selected_cipher == 'vigenere':
        key = entry1.get()
        answer = encrypt_vigenere(sentence, key)
    elif selected_cipher == 'one_time_pad':
        keyword = entry1.get()
        answer = one_time_pad(sentence, keyword)
    else:
        answer = "Unknown cipher"
    result.set(answer)


def open_leaderboard():
    entries = load_leaderboard_sorted()
    root_lb = tk.Tk()
    root_lb.resizable(False, False)
    root_lb.title('Leaderboard')
    root_lb.configure(bg='lightgray')
    root_lb.geometry('520x450')

    title = tk.Label(root_lb, text='Leaderboard', font=('Arial', 16, 'bold'), bg='lightgray')
    title.pack(pady=10)

    if not entries:
        empty_label = tk.Label(root_lb, text='No leaderboard entries yet.', bg='lightgray')
        empty_label.pack(pady=20)
        return

    header = tk.Label(root_lb, text='Rank    Name               Difficulty    Time', font=('Arial', 11, 'bold'), bg='lightgray', anchor='w')
    header.pack(fill='x', padx=10)

    frame = tk.Frame(root_lb, bg='lightgray')
    frame.pack(fill='both', expand=True, padx=10, pady=10)

    listbox = tk.Listbox(frame, font=('Courier New', 10), width=70, height=18)
    
    for idx, entry in enumerate(entries, start=1):
        name = entry['name'] or 'Unknown'
        diff = entry['diff'] or 'Unknown'
        time_text = entry['time'] or 'did not finish'
        listbox.insert('end', f"{idx:>2}. {name:<18} {diff:<12} {time_text}")
    listbox.pack(side='left', fill='both', expand=True)

    scrollbar = tk.Scrollbar(frame, orient='vertical', command=listbox.yview)
    scrollbar.pack(side='right', fill='y')
    listbox.config(yscrollcommand=scrollbar.set)


def open_smm():
    global v
    global full
    global root_smm
    try:
        root_1.destroy()
    except Exception:
        pass
    root_smm = tk.Tk()  
    root_smm.resizable(False, False)
    root_smm.title('the descriptive murder mystery front page')
    root_smm.configure(bg='lightgray')
    root_smm.geometry("600x600")
    buttonin = tk.Button(root_smm,text='back',width=25,activebackground="red",activeforeground="white",command= lambda: [root_smm.destroy(), open_cypher_ui_1()] )
    buttonin.place(x=10, y=560)
    
    full = tk.Entry(root_smm)
    startgame = tk.Button(root_smm,text='start the game',width=15,height=5,activebackground="lightgreen",activeforeground="white",command=lambda:[game_rules()])
    startgame.pack(pady=10)
    v = tk.IntVar()
    tk.Radiobutton(root_smm, text=" easy ", variable=v, value=1).pack(pady=1)
    tk.Radiobutton(root_smm, text="normal", variable=v, value=2).pack(pady=1)
    tk.Radiobutton(root_smm, text=" hard ", variable=v, value=3).pack(pady=1)
    tk.Label(root_smm, text=" full name").pack()
    full.pack()

def open_smm_game():
    global game_right_solved, page_left_solved, page_leftdown_solved
    global buttonright_game, buttonleft_game, buttonleftdown_game
    global root_game
    game_right_solved = False
    page_left_solved = False
    page_leftdown_solved = False
    root_game = tk.Tk() 
    root_game.resizable(False, False)
    root_game.title('game')
    root_game.configure(bg='lightgray')
    root_game.geometry("850x450")
    bg_img = tk.PhotoImage(file="image\\room.png")
    bg_label = tk.Label(root_game, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_img
    buttonright_game = tk.Button(root_game,text='click here',width=7,activebackground="blue",activeforeground="white", command=on_buttonright)
    buttonright_game.place(x=700, y=150)
    buttonleft_game = tk.Button(root_game,text='click here',width=7,activebackground="blue",activeforeground="white", command=on_buttonleft)
    buttonleft_game.place(x=50, y=85)
    buttonleftdown_game = tk.Button(root_game,text='click here',width=7,activebackground="blue",activeforeground="white", command=on_buttonleftdown)
    buttonleftdown_game.place(x=150, y=350)
    buttondoor = tk.Button(root_game,text='open the door',width=15,activebackground="blue",activeforeground="white", command=dooropen)
    buttondoor.place(x=362, y=230)

    def close_game_windows():
        try:
            if roott.winfo_exists():
                roott.destroy()
        except Exception:
            pass
        try:
            if root_game.winfo_exists():
                root_game.destroy()
        except Exception:
            pass

    root_game.protocol("WM_DELETE_WINDOW", close_game_windows)


def dooropen():
    if game_right_solved and page_left_solved and page_leftdown_solved:
        savescore(strftime("%M:%S", time.gmtime(time.time() - start_time)))
        roott.destroy()
        root_game.destroy()
        root_door = tk.Tk()
        root_door.resizable(False, False)
        imgen = tk.PhotoImage(file="image\\duck.png")
        mini_imgen=imgen.subsample(2, 2)
        mini_imgen_label = tk.Label(root_door, image=mini_imgen, bg='lightgray')
        mini_imgen_label.image = mini_imgen
        mini_imgen_label.pack(pady=10)

        root_door.title('good job!')
        root_door.configure(bg='lightgray')
        root_door.geometry("400x450")
        label = tk.Label(root_door,text="congratulations, you solved the mystery and escaped the room! take this rubber duck as a prize", bg='lightgray')
        label.pack(pady=20)
        button = tk.Button(root_door,text='back to the main page',width=25,activebackground="blue",activeforeground="white", command=lambda: [root_door.destroy(), open_cypher_ui_1()])
        button.pack(pady=10)
        

def on_buttonright():
    global root_btr, game_right_solved
    if game_right_solved:
        return
    root_btr = tk.Tk()
    root_btr.resizable(False, False)
    root_btr.title('game right botton')
    root_btr.configure(bg='lightgray')
    root_btr.geometry("400x450")
   
    enc = encryptionnum()
    word = artrandomword()
    key = keyrandom()
    if enc == "azby":
        key = None
    label = tk.Label(root_btr, text=encryptionpicknum(enc, word, key))
    label.pack(pady=20)
    if key is None:
        labeltoo = tk.Label(root_btr, text=f"the cypher is {enc}\nEnter your answer:")
    else:
        labeltoo = tk.Label(root_btr, text=f"the cypher is {enc} and the key is {key}\nEnter your answer:")
    labeltoo.pack(pady=15)
    entry1 = tk.Entry(root_btr, selectbackground="lightblue", selectforeground="black")
    entry1.pack(pady=10)
    buttonright = tk.Button(root_btr,text='guess',width=7,activebackground="blue",activeforeground="white", command=lambda: on_buttontry(entry1, word, root_btr, 'right'))
    buttonright.pack(pady=12)

def on_buttonleft():
    global root_btl, page_left_solved
    if page_left_solved:
        return
    root_btl = tk.Tk()
    root_btl.resizable(False, False)
    root_btl.title('game left botton')
    root_btl.configure(bg='lightgray')
    root_btl.geometry("400x450")
   
    enc_s = encryptionstring()
    word = scaryrandomword()
    key = stringkeyrandom()
    label = tk.Label(root_btl, text=encryptionpickstring(enc_s, word, key))
    label.pack(pady=20)
    if key is None:
        labeltoo = tk.Label(root_btl, text=f"the cypher is {enc_s}\nEnter your answer:")
    else:
        labeltoo = tk.Label(root_btl, text=f"the cypher is {enc_s} and the key is {key}\nEnter your answer:")
    labeltoo.pack(pady=15)
    entry1 = tk.Entry(root_btl, selectbackground="lightblue", selectforeground="black")
    entry1.pack(pady=10)
    buttonright = tk.Button(root_btl,text='guess',width=7,activebackground="blue",activeforeground="white", command=lambda: on_buttontry(entry1, word, root_btl, 'left'))
    buttonright.pack(pady=12)


def on_buttonleftdown():
    global root_btlb, page_leftdown_solved
    if page_leftdown_solved:
        return
    root_btlb = tk.Tk()
    root_btlb.resizable(False, False)
    root_btlb.title('game left botton down')
    root_btlb.configure(bg='lightgray')
    root_btlb.geometry("400x450")
    enc_o = encryptionforone_time_pad()
    word = toysrandomword()
    key = keyforone_time_pad(word)
    label = tk.Label(root_btlb, text=forone_time_pad(enc_o, word, key))
    label.pack(pady=20)
    if key is None:
        labeltoo = tk.Label(root_btlb, text=f"the cypher is {enc_o}\nEnter your answer:")
    else:
        labeltoo = tk.Label(root_btlb, text=f"the cypher is {enc_o} and the key is {key}\nEnter your answer:")
    labeltoo.pack(pady=15)
    entry1 = tk.Entry(root_btlb, selectbackground="lightblue", selectforeground="black")
    entry1.pack(pady=10)
    buttonright = tk.Button(root_btlb,text='guess',width=7,activebackground="blue",activeforeground="white", command=lambda: on_buttontry(entry1, word, root_btlb, 'leftdown'))
    buttonright.pack(pady=12)


def on_buttontry(entry1, answer, window, source):
    global game_right_solved, page_left_solved, page_leftdown_solved
    global buttonright_game, buttonleft_game, buttonleftdown_game
    user_answer = entry1.get()
    if user_answer.lower() == answer.lower():
        if source == 'right':
            game_right_solved = True
            if buttonright_game is not None:
                buttonright_game.configure(state='disabled')
        elif source == 'left':
            page_left_solved = True
            if buttonleft_game is not None:
                buttonleft_game.configure(state='disabled')
        elif source == 'leftdown':
            page_leftdown_solved = True
            if buttonleftdown_game is not None:
                buttonleftdown_game.configure(state='disabled')
        window.destroy()
        


def encryptionpicknum(encryption,text,key):
    if encryption == "azby":
        return azby(text)
    elif encryption == "caesar":
        try:
            key = int(key)
        except (TypeError, ValueError):
            key = 0
        return caser(text, key)
    return text
def forone_time_pad(encryption,text,key):
    if encryption== "one_time_pad":
        return one_time_pad(text, key)

    
def encryptionpickstring(encryption,text,textkey):
    if encryption== "vigenere":
        return encrypt_vigenere(text, textkey)
    
import tkinter as tk


def make_cipher_listbox(root, entry_for_key, result_var=None, x=10, y=300):
    lb = tk.Listbox(root, height=5)
    for item in ('azby', 'caesar', 'vigenere', 'one_time_pad'):
        lb.insert('end', item)
    lb.place(x=x, y=y)
    lb.select_set(0)
    lb.bind('<<ListboxSelect>>', lambda event, e=entry_for_key, l=lb: update_key_field_state(e, l))
    return lb


def format_cipher_label(enc, key):
    if key is None:
        return f"the cypher is {enc}\nEnter your answer:"
    return f"the cypher is {enc} and the key is {key}\nEnter your answer:"

def start_timer(seconds):
    global start_time
    global roott
    start_time = time.time()
    roott = tk.Tk()
    roott.resizable(False, False)
    roott.title("Timer")
    roott.geometry("300x200")

    timer_label = tk.Label(roott, text="", font=("Arial", 50))
    timer_label.pack(expand=True)

    def count_down(time_left):
       
        mins, secs = divmod(max(time_left, 0), 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")

        if time_left > 0:
           
            roott.after(1000, count_down, time_left - 1)
        else:
            timer_label.config(text="00:00", fg="red")
            try:
                from tkinter import messagebox
                messagebox.showinfo("Timer", "Time's up!")
            except Exception:
                pass
            try:
                if roott.winfo_exists():
                    roott.destroy()
            except Exception:
                pass
            try:
                if root_game.winfo_exists():
                    root_game.destroy()
            except Exception:
                pass
            try:
                open_smm()
            except Exception:
                pass

    count_down(seconds)
    roott.mainloop()
   

def game_rules():
    name_to_save = full.get()
    difficulty_idx = v.get()

    if name_to_save != "" and difficulty_idx != 0:
        savename(name_to_save)
        
        diff_map = {1: "easy", 2: "normal", 3: "hard"}
        savediff(diff_map.get(difficulty_idx, "unknown"))
        
        if difficulty_idx == 1:
            totime = 300
        if difficulty_idx == 2:
            totime = 180
        if difficulty_idx == 3:
            totime = 90
        
        root_smm.destroy()
        open_smm_game()
        start_timer(totime)
open_cypher_ui_1()


