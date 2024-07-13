import turtle
import pandas

screen = turtle.Screen()
screen.title("World countries")
image = "world_countries.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("countries.csv")
all_countries = data.country.to_list()
guessed_countries = []

while len(guessed_countries) < 195:
    answer_country = screen.textinput(title=f"{len(guessed_countries)}/195 Guess a country", prompt="What is the other country name?").title()
    #Guess if the country is in the file of countries.csv
    if answer_country in all_countries:
        guessed_countries.append(answer_country)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.country == answer_country]
        t.goto(int(country_data.x), int(country_data.y))
        t.write(country_data.country.item())





screen.exitonclick()