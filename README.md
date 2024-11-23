# ECM1400 - Programming - Continuous Assessment 2
**Author: Emre Acarsoy**


# Features

This Battleships game supports the following:
- Playing singleplayer, through the console
- Playing against an AI opponent, through the console
- Playing against AI opponent, through a web interface

This game also supports 3 algorithms for placing your ships:
- "simple", which places your ships horizontally, starting from the top left (0,0)
- "random", which places your ships in random positions
- "custom", which allows you to place your ships in a custom layout
Additionally, if playing using the web interface, there is an interactive placement option, please see [below](#3-against-ai-opponent---web-interface)  

---

# Build

**FOR ALL VERSIONS:**  

Please specify which ships you would like to have in the game, using the `battleships.txt` file.  
Here is an example battleships.txt file:
```
Aircraft_Carrier:5
Battleship:4
Cruiser:3
Submarine:3
Destroyer:2
```
In this example, 5 ships are in play, of lengths 5, 4, 3, 3, and 2 respectively. Please do not give duplicate names for ships.  

**NOTE:** for all versions, if you want to use the "custom" placement algorithm, please specify your desired ship placement in the `placement.json` file. Your file should look like the following template:  
```
{
  "Aircraft_Carrier":["0","0","h"],
  "Battleship":["2","2","v"],
  "Cruiser":["4","4","h"],
  "Submarine":["6","6","v"],
  "Destroyer":["8","8","h"]
}
```
"Ship":[start_x, start_y, "horizontal / vertical"]  


### 1. Singleplayer - command line interface
To play the singleplayer version, run the game_engine.py file:
```
python game_engine.py
```
NOTE: specify simple / random / custom placement how??


### 2. Against AI opponent - command line interface

To play against the AI opponent, run the mp_game_engine.py file:
```
python mp_game_engine.py
```

### 3. Against AI opponent - web interface
To play against the AI opponent through the web interface, run the main.py file:
```
python main.py
```
This will give you a local IP address, which you can access using a browser.  
By default your ships will be placed according to `placement.json`.  
**If you want to place the ships interactively using the web interface**, please add `/placement` to the end of your URL. Once the ship placement is complete, you can go back to the main game screen  by clicking the "send game" button.


# TODO:
- [x] AI does not repeat attacks
- [ ] Player allowed to repeat attacks?
- [ ] Random placement algorithm stall check
- [ ] How does user specify placement algorithm? Modifying source code seems like a bad option
- [ ] Implement AI difficulty options