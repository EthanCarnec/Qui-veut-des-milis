from guizero import App, Text, PushButton, TextBox, Box, Drawing, Picture

app = App(title="sponsored by redbull", width=1600, height=838)

entete=Drawing(app, height=120, width=1600)

entete.rectangle(0,0,1600,120, color="grey")
entete.image(750,4,image="img/img1.png")
entete.image(1370,15,image="img/img2.png")
entete.image(0,0,image="img/img5.png")

middle=Drawing(app, height=460, width=1600)

middle.rectangle(0,0,1600,460, color='blue')
middle.rectangle(1335,0,1600,460, color='purple')
middle.rectangle(750,0)
def clicked(event_data):
    print("widget clicked = " + event_data.widget)
    print("mouse position = " + event_data.x + "." + event_data.y)

widget.when_clicked = clicked


question=Drawing(app, height=258, width=1600)

question.rectangle(0,0,1600,258, color='black')

#img1= Picture(app, image="img")


app.display()