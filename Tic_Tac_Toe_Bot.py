#                                        IMPORTING THE LIBRARIES

import numpy as np
from numpy import unravel_index
from tkinter import *
from time import sleep
import random


#                                         CREATING THE FRAMES

win = Tk()
win.iconbitmap('D:/User/Desktop/ttt.ico')
win.title('"YOU" V/S "BOT"')
win.geometry('500x308+10+100')
frame = Frame(win)
frame_indicator = Frame(win)
frame_score = Frame(win)
restart_b = Frame(win)


'''                    >>>>>>>>>>>>>>        DISPLAY  Control  Structure      >>>>>>>>>>>>>>>                        '''

score_x = 0
score_y = 0
main_botton='light green'
main_botton_acl='yellow'
main_botton_acb='yellow'
background='light blue'
score_back='light blue'
score_font='black'
restart_bg ='red'
restart_fg='black'
player_no_bg='light blue'
player_no_fg='black'

'''                                >>>>>>>>>>>>        FUNCTION'S          >>>>>>>>>>>>>                             '''

class tic_tac_toe:

    def __init__(self):

        '''     >>>>>>>>>>>                  INITILIZING EVERY FRAME                            >>>>>>>>>>>>         '''


        self.set = 0
        self.set2 = 0
        self.m = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        self.count = 0

        #                                         PLAYER INDICATOR                                                     #

        self.l = Label(frame_indicator, text='Player X', font=('Bradley Hand ITC', 20, 'italic'), bg='gray')
        self.l.pack()

        #                                          RESTART BUTTON                                                      #

        self.re = Button(restart_b, text='Restart', bg='red', font=('Algerian'), height=4, command=lambda: self.start())
        self.re.pack(fill=BOTH)

        #                                          SCORE   INDICATOR                                                   #

        self.sco = Label(frame_score, text="SCORE X    {} ".format(score_x), font=('Bauhaus 93', 25, 'italic'),
                         bg='gray')
        self.sco.pack()
        self.sco2 = Label(frame_score, text="SCORE Y    {} ".format(score_y), font=('Bauhaus 93', 25, 'italic'),
                          bg='gray')
        self.sco2.pack()

        #                                          TIC_TAC_TOE Button                                                  #

        for i in range(3):
            for j in range(3):
                self.b = Button(frame, bg=main_botton, fg='white', width=12, height=6, cursor='arrow',
                                command=lambda row=i, column=j: self.onclick(row, column)
                                )
                self.b.grid(row=i, column=j)


        ##                                MAKING DIRECT CHANGES TO THE FRAMES                                        ##

        win.config(bg='orange')
        self.re.config(bg=restart_bg, fg=restart_fg)
        self.sco.config(bg=score_back, fg=score_font)
        self.sco2.config(bg=score_back, fg=score_font)
        self.l.config(bg=player_no_bg, fg=player_no_fg)

    def start(self):
        self.l = Label(frame_indicator, text='Player {}'.format('Y'), font=('Bradley Hand ITC', 20, 'italic'),
                        bg=player_no_bg)
        self.l.pack()
        self.set = 0
        self.sco2.destroy()
        self.sco.destroy()
        self.l.destroy()
        self.l2.destroy()
        self.re.destroy()
        self.__init__()


    '''                            >>>>>>>>>     BOT  ALGORITHM        >>>>>>>>>>                                   '''


    def updatearray(self,M, C):
        for i in range(3):
            for j in range(3):
                if M[i][j] == 'X':
                    C[i, j] = 1
                elif M[i][j] == 'Y':
                    C[i, j] = -1
        return C

    def NextMove(self,l,l2):

        play='Y'

        def count_d(p, l):

            s = sum(l)
            if p == 'X':
                m = 1
            else:
                m = -1
            val = (s * m) / 3
            return val


##                                      Getting  The  Probability  Matrix                                             ##

        def Win_Mov(p, l, l2):

            for i in range(3):
                h = l[[i], :][0]
                v = l2[:, [i]].reshape((1, 3))[0]
                val_v = count_d(p, v)
                val_h = count_d(p, h)

                for j in range(3):
                    if v[j] == 0:
                        l2[j, i] = val_v
                    if h[j] == 0:
                        l[i, j] = val_h

            l3 = l2
            #print('\n\n>>>>>>>>>>>>>>         Horizontal MATRIX           >>>>>>>>>>>>>>>>>>\n\n', l)
            #print('\n\n>>>>>>>>>>>>>>         Vertical  MATRIX           >>>>>>>>>>>>>>>>>>\n\n', l2)

            for i in range(3):
                for j in range(3):

                    if l[i][j] != -1 and l[i][j] != 1:
                        if abs(l[i][j]) < abs(l2[i][j]):
                            l[i][j] = l2[i][j] * 100
                            l3[i][j] = l2[i][j]
                        elif abs(l[i][j]) > abs(l2[i][j]):
                            l[i][j] = l[i][j] * 100
                            l3[i][j] = l2[i][j]
                        elif l[i][j] == l2[i][j]:
                            l3[i][j] = l[i][j]
                            l[i][j] = l[i][j] * 100
                        elif abs(l[i][j]) == abs(l2[i][j]):
                            l3[i][j] = abs(l[i][j])
                            l[i][j] = abs(l[i][j]) * 100
                        elif abs(l2[i][j]) >= abs(l[i][j]):
                            l3[i][j] = l2[i][j]
                            l[i][j] = l2[i][j] * 100

            d = np.diag(l3)
            ad = np.fliplr(l3).diagonal()



            nummm = 2.0 / 3
            if list(d).count(1) == 2 and sum(d)!=1 and sum(d)!=-1:
                for nn in range(3):
                    if d[nn] != 1.0:
                        l[nn][nn] = -nummm * 100
            if list(d).count(-1) == 2 and sum(d)!=1 and sum(d)!=-1:
                for nn in range(3):
                    if d[nn] != -1.0:
                        l[nn][nn] = +nummm * 100
            if list(ad).count(1) == 2 and sum(ad)!=1 and sum(ad)!=-1:
                for nn in range(3):
                    if ad[nn] != 1.0:
                        l[nn][2 - nn] = -nummm * 100
            if list(ad).count(-1) == 2 and sum(ad)!=1 and sum(ad)!=-1:
                for nn in range(3):
                    if ad[nn] != -1.0:
                        l[nn][2 - nn] = +nummm * 100

            #print('\n\n>>>>>>>>>>>>>>         PROBABILITY MATRIX           >>>>>>>>>>>>>>>>>>\n\n', l/100)
            #print(l)
            if np.amax(abs(l)) == np.amax(l):
                corx, cory = unravel_index(l.argmax(), l.shape)
            elif np.amax(l) < np.amax(abs(l)):
                corx, cory = unravel_index(abs(l).argmax(), l.shape)
            else:
                corx, cory = unravel_index(l.argmax(), l.shape)

            opt = []
            for ij1 in range(3):
                for ji1 in range(3):
                    if l[ij1][ji1] == l[corx][cory]:
                        opt.append((ij1, ji1))

            corx, cory = random.choice(opt)

            #print('>>>>>>>>>>>>>>>>>>>    NEXT MOVE COORDINATES   >>>>>>>>>>>>>>>>>>>>>>>>\n',corx,cory)
            if np.count_nonzero(abs(l) == 1)<=8:
                self.onclick(corx,cory)
        Win_Mov(play, l, l2)


    '''                           >>>>>>>>>      CHECKING  THE  WINNING  CONDITION       >>>>>>>>>                   '''

    def Conditions(self, l, player):

        global main_botton_acl, main_botton_acb
        color = main_botton_acb
        color2 = main_botton_acl
        know = 0

        for ii in range(3):

            c = 0
            v = 0
            d = 0
            di = 0

            if l[ii][0] == player and l[ii][1] == player and l[ii][2] == player:
                for _ in range(3):
                    Button(frame, bg=color, fg='white', width=12, height=6,
                           ).grid(row=ii, column=c)
                    Label(frame, text=player, bg=color2, fg='black', font=("Courier", 40)).grid(row=ii, column=c)
                    c = c + 1
                know = 1
                break

            if l[0][ii] == player and l[1][ii] == player and l[2][ii] == player:
                for _ in range(3):
                    Button(frame, bg=color, fg='white', width=12, height=6,
                           ).grid(row=v, column=ii)
                    Label(frame, text=player, bg=color2, fg='black', font=("Courier", 40)).grid(row=v, column=ii)
                    v = v + 1
                know = 1
                break

            if l[0][0] == player and l[1][1] == player and l[2][2] == player:
                for _ in range(3):
                    Button(frame, bg=color, fg='white', width=12, height=6,
                           ).grid(row=d, column=d)
                    Label(frame, text=player, bg=color2, fg='black', font=("Courier", 40)).grid(row=d, column=d)
                    d = d + 1
                know = 1
                break

            if l[0][2] == player and l[1][1] == player and l[2][0] == player:
                for _ in range(3):
                    Button(frame, bg=color, fg='white', width=12, height=6,
                           ).grid(row=di, column=2 - di)
                    Label(frame, text=player, bg=color2, fg='black', font=("Courier", 40)).grid(row=di, column=2 - di)
                    di = di + 1
                know = 1
                break

        if know == 1:
            if player=='X':
                self.set=1
            else:
                self.set=0
            self.Score(player)
            return 1
        return 0


##                                           DISPLAY    THE     SCORE                                                 ##


    def Score(self, player):

        global score_x, score_y
        if player == 'X':
            self.sco.destroy()
            self.l2.destroy()

            score_x = score_x + 1
            self.sco = Label(frame_score, text="SCORE X {}".format(score_x), font=('Bauhaus 93', 25, 'italic'),
                             bg=score_back)
            self.sco.pack()
        else:
            self.sco2.destroy()
            self.l.destroy()
            if self.set != 1:
                score_y = score_y + 1
            self.sco2 = Label(frame_score, text="SCORE Y {}".format(score_y), font=('Bauhaus 93', 25, 'italic'),
                              bg=score_back)
            self.sco2.pack()
            self.set = 1


    def onclick(self, row, column):
        ccz = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        ccy = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        self.count = self.count + 1

        if self.count % 2 != 0:
            text = 'X'
            self.l.destroy()
            self.l2 = Label(frame_indicator, text='Player {}'.format('Y'),font=('Bradley Hand ITC',20,'italic'), bg=player_no_bg)
            self.l2.pack()
            self.m[row][column] = 'X'
            ccz = self.updatearray(self.m, ccz)
            ccy = self.updatearray(self.m, ccy)
           #print('\n>>>>>>>>>>>>>>>>>>    TIC TAC TOE MATRIX    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n',ccz)
            p = 'X'

        else:
            text = 'Y'
            self.l2.destroy()
            self.l = Label(frame_indicator, text='Player {}'.format('X'), font=('Bradley Hand ITC',20,'italic'), bg=player_no_bg)
            self.l.pack()
            self.m[row][column] = 'Y'
            ccz = self.updatearray(self.m, ccz)
            #print('yyy', ccz)
            p = 'Y'

        self.b = Button(frame, bg='white', fg='white', width=12, height=6,
                        )
        self.b.grid(row=row, column=column)
        self.b1 = Label(frame, text=text, bg='white', fg='black', font=("Courier", 40)
                        )
        self.b1.grid(row=row, column=column)
        self.Conditions(self.m, p)
        if self.count <= 8:
            if self.set != 1 and p=='X':
                self.NextMove(ccz, ccy)

        frame.update()



'''                              >>>>>>>>>    CLASS THE CLASS OBJECT   >>>>>>>>>>                                    '''

o = tic_tac_toe()

'''                                 >>>>>>>>>>    PLACING THE OBJECT    >>>>>>>>>>>>                                 '''


frame.pack(side=LEFT)
frame_indicator.pack(side=TOP, ipadx=5)
restart_b.pack(side=BOTTOM,fill=BOTH)
frame_score.pack(side=RIGHT)
mainloop()


