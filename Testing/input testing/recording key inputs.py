import keyboard
recorded_events = keyboard.record("esc")
keyboard.play(recorded_events)

print(list(keyboard.get_typed_strings(recorded_events)))
