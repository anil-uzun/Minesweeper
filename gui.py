import game_logic
from tkinter import *


root = Tk()
root.configure(bg='black')

screen_height = int(root.winfo_screenheight())


borderless = Frame(root, background='black')

flag_button = Button(root, font="bold", text=game_logic.fbt, fg='white', bg=game_logic.fbc, height=int(screen_height/600), width=int(screen_height/600), borderwidth=0,
                     command=lambda: [game_logic.flag_mode(),
                                      flag_button.configure(bg=game_logic.fbc, text=game_logic.fbt)])


game_logic.main()


flags0 = Label(root, font="bold", text="F", fg='red', bg='black', height=int(screen_height/600), width=int(screen_height/600), borderwidth=0)
flags = Label(root, font="bold", text=f"{game_logic.flags}", fg='red', bg='black', height=int(screen_height/600), width=int(screen_height/600), borderwidth=0, padx=12*int(screen_height/600))
flag_button.grid(row=0, column=0)
flags0.grid(row=0, column=1)
flags.place(y=6, x=72)


summoned = []
colors = ['#71D6C6', '#9AE06F', '#B80000', '#C57EDE', '#FFEF82', '#EB0A82', '#90ABEB', 'gray']


def button_list_gen():
    global button_list, summoned
    button_list = []
    summoned = []
    for y in range(game_logic.size_y):
        summoned.append([])
        button_list.append([])
        for x in range(game_logic.size_x):
            summoned[y].append([])
            button_list[y].append([])


def update_buttons():
    for a in range(game_logic.size_y):
        for b in range(game_logic.size_x):
            if game_logic.board[a][b][0] == " ":
                button_list[a][b].destroy()
            if game_logic.board[a][b][0] not in [' ', 'M', 'F', 'X'] and not summoned[a][b]:
                button_list[a][b].destroy()
                text_color = colors[int(game_logic.board[a][b][0])-1]
                button_list[a][b] = Button(root, height=int(screen_height/600), width=int(screen_height/600), highlightcolor="orange", highlightthickness=0, borderwidth=0, fg=text_color, bg='black', font="bold",
                                           text=game_logic.board[a][b][0],
                                           command=lambda a=a, b=b: [game_logic.left_click(a + 1, b + 1),
                                                                     update_buttons()])
                button_list[a][b].grid(row=a + 1, column=b)
                summoned[a][b] = True
            if game_logic.board[a][b][0] == 'F' and not summoned[a][b]:
                button_list[a][b].destroy()
                flags.configure(text=game_logic.flags)
                button_list[a][b] = Button(root, height=int(screen_height/600), width=int(screen_height/600), font="bold", text="F", bg='black', fg='red', borderwidth=0,
                                           command=lambda a=a, b=b: [game_logic.left_click(a + 1, b + 1),
                                                                     s_remove(a, b),
                                                                     update_buttons()])
                button_list[a][b].grid(row=a + 1, column=b)
                summoned[a][b] = True
            if game_logic.board[a][b][0] == 'X':
                button_list[a][b].configure(text=" ")
                flags.configure(text=game_logic.flags)


def s_remove(row, column):
    global summoned
    if game_logic.board[row][column] == ["X"]:
        summoned[row][column] = False


def buttons():
    for a in range(game_logic.size_y):
        for b in range(game_logic.size_x):
            if game_logic.board[a][b][0] == 'X':
                button_list[a][b] = Button(root, height=int(screen_height/600), width=int(screen_height/600), bg='black', text=" ", font="bold", highlightcolor='orange', borderwidth=0,
                                           command=lambda a=a, b=b: [game_logic.left_click(a + 1, b + 1),
                                                                     update_buttons()])
                button_list[a][b].grid(row=a + 1, column=b)


def main():
    button_list_gen()
    buttons()
    root.mainloop()


main()
