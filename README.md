# **Converter .𝗽𝗻𝗴 to .𝗶𝗰𝗼**

**A just converter .𝗽𝗻𝗴 to .𝗶𝗰𝗼 simple**
![background](https://cdn.discordapp.com/attachments/1060604037394870403/1066448148492455997/image.png)

# __INSTALLATION__
>### [Developper Portal](https://discord.com/developers/applications/) (Create Application)
>## ```pip install pypresence```
>### ![background](https://cdn.discordapp.com/attachments/1047918302841798718/1059956075492814848/image.png) (Add Image)


# EXEMPLE
```py
from pypresence import Presence
import time

client_id = '123456789123'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

print(RPC.update(state="Lookie Lookie", details="A test of qwertyquerty's Python Discord RPC wrapper, pypresence!"))  # Set the presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds
```

## __Build__
* [Pypresence](https://pypi.org/project/pypresence/)
* [Python](https://www.python.org/)
