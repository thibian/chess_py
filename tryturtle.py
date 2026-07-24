import turtle as t


t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break
t.end_fill()

t.mainloop()