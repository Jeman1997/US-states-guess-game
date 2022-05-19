import pandas
import turtle
scr = turtle.Screen()
scr.title('U.S States')
scr.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')
dt = pandas.read_csv('50_states.csv')
stlis=list(dt.state)
corrects=[]
while len(corrects)!=len(stlis):
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    ans=scr.textinput(title=str(len(corrects))+"/50",prompt="Type a state's name")
    if ans.title() in stlis:
        xc=dt[dt['state']==ans.title()]['x']
        yc=dt[dt['state']==ans.title()]['y']
        corrects.append(ans.capitalize())
        t.setpos(float(xc),float(yc))
        t.write('*'+ans.title())
        print('right answer')
        print(ans.title())
    if ans.title()=='Exit':
        break
    else:
        pass
dic={
    'States you dont know':[x for x in stlis if x not in corrects]
    }
unkdt=pandas.DataFrame(dic)
print(unkdt)
unkdt.to_csv('UnknownStates')
print(dir(pandas))