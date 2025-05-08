import gui
import cards as c


screen = gui.MainScreen()
path = screen.get_file()
print(path)
print(type(path))

cards = c.read_cards(path)
print(cards)

c.shuffle_cards(cards)

print(cards)

screen.load_cards(cards)
screen.start()
