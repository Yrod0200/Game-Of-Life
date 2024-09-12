import game
import screen
import threading

start = screen.StartGame()

player = start.start()

events = screen.terminal_events(player)
