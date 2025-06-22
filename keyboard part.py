from pynput.keyboard import Listener,Key

def listen_to_keyboard()
    typed_text = []
   def on_press():
      text = ""
      try:
         key = key.char
      except AttributeError:
        if key == Key.space:
          key = ' '
        if key == Key.enter:
            key = '\n'
      key_data = str(key)
      key_data = key_data.replace("' ", " ")
      text.append(key_data)
 
with Listener (on_press = on_press) as l:
       l.join()
typed_text.join(l)

return typed_text

