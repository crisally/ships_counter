# Ships Counter
Script for counting the number of ships on the sea-battle board

## How to run:

1) Clone the project

2) Run this commands in terminal:
```
docker build -t image_ship_counter ./
docker run -d --name container_ship_counter -p 8000:8000 image_ship_counter
```

3) Take a data from resources/data, or generate using board_generator in data_generator.py, or generate by yourself

For example:
```json
{"board": "##--------\n--########\n----------\n#-----##-#\n#-##-#---#\n#----#---#\n#----#--#-\n#-##-#--#-\n--------#-\n-######---"}
```

4) Make a post-request to http://localhost:8000/counter

5) You'll get a result:
```json
{"count_ships": 10}
```
