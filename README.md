# DS5100-2024-06-R
DS 5100 Programming for Data Science | Summer 2024 | Residential
##
# Metadata

**Package Name**: Montecarlo

**Description**: Play a Game of Rolling Dice, and Analyze the Results of Those Rolls.

**Version**: 1.0

**Author**: Finn Mokrzycki

**License**: MIT License

**Installation Instructions**:
```bash
pip install git+https://github.com/finnmok/DS5100-2024-06-R.git
```

**Dependencies**:
* Python (>= 3.12.3)
* Pandas (>= 2.2.2)
* Numpy (>= 2.0.0)


**For More Help and Information on Classes and Methods**:
```python
help(montecarlo)
```

##
# Synopsis

### Importing Necessary Libraries
Before using the classes, ensure that you imported the necessary libraries:

```python
import numpy as np
import pandas as pd
from collections import Counter
from itertools import combinations, permutations
```

## Creating a Die Object
To create a die with custom faces:

   ```python
   faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
   die = Die(faces)
   ```

### Setting Weights for Die Faces

For example, to set the weight of face 'A' to 3.0:
   ```python
   die.set_wts('A', 3.0) #All faces default to 1
   ```

### Rolling the Die
Roll the die a specified number of times (e.g. roll 10 times):
   ```python
   die.roll(10)
   ```

### Retrieving Die Weights
To get the current weights of the die faces:

   ```python
   die.get_die_wts()
   ```

## Creating a Game Object
To create a game with multiple dice, use Die objects in a list

   ```python
   dice = [
    Die(np.array([1, 2, 3, 4, 5, 6])), 
    Die(np.array([1, 2, 3, 4, 5, 6])) #All Dice Must Have Same Faces
    ]

   game = Game(dice)
   ```

### Playing the Game
To roll the dice a specified number of times (e.g. roll the dice 10 times):
   ```python
   game.play(10)
   ```

### Retrieving the Most Recent Play Results
To get the results of the most recent play:

Get the results in wide format pd.DataFrame (default):
   ```python
   game.get_most_recent_play(form='wide')
   ```

Or in narrow format:
   ```python
   game.get_most_recent_play(form='narrow')
   ```

## Creating an Analyzer Object
To analyze the results of a game:

   ```python
   analyzer = Analyzer(game)
   ```

### Counting Jackpots
To count the number of times the game resulted in a jackpot (i.e. all dice returned the same face in a roll):

Get the number of jackpots:
   ```python
   analyzer.jackpot_count()
   ```

### Counting Face Occurrences
To count how many times a given face is rolled in each event:

   ```python
   analyzer.face_count()
   ```

### Counting Combinations
To count the distinct combinations of faces rolled:
   ```python
   analyzer.combination_count() #Returns MultiIndex pd.DataFrame
   ```

### Counting Permutations
To count the distinct permutations of faces rolled:
   ```python
   analyzer.permutation_count()
   ```


##
# API Documentation


### Class: Die
A class representing a die with customizable faces and weights.

#### Initialization
```python
Die(faces: numpy.ndarray)
```
- **faces**: A NumPy array of faces for the die. Must be strings or numbers.

#### Methods

- `set_wts(which_face, new_wt)`
  ```python
  set_wts(which_face, new_wt)
  ```
  Sets the weight of a specified face.
  - **which_face**: The face value to be changed. Must exist in initialized faces and be of the same datatype as elements in the face array.
  - **new_wt**: The new weight for the specified face. Must be numeric or castable as numeric.

- `roll(n_rolls=1)`
  ```python
  roll(n_rolls=1)
  ```
  Rolls the die a specified number of times.
  - **n_rolls**: The number of times to roll the die. Defaults to 1.

- `get_die_wts()`
  ```python
  get_die_wts()
  ```
  Retrieves the current weights of the die faces.
  - **Returns**: A pandas DataFrame containing the weights of the die faces.

### Class: Game
A class representing a game played with multiple dice.

#### Initialization
```python
Game(dice: list)
```
- **dice**: A list of already instantiated Die objects.

#### Methods

- `play(n_rolls)`
  ```python
  play(n_rolls)
  ```
  Rolls the dice a specified number of times and saves the results.
  - **n_rolls**: The number of times the dice should be rolled.

- `get_most_recent_play(form='wide')`
  ```python
  get_most_recent_play(form='wide')
  ```
  Returns the most recent play results in the specified format.
  - **form**: The format of the returned data frame. Must be 'wide' or 'narrow'. Defaults to 'wide'.

### Class: Analyzer
A class for analyzing the results of a game played with multiple dice.

#### Initialization
```python
Analyzer(game: Game)
```
- **game**: A Game object to be analyzed.

#### Methods

- `jackpot_count()`
  ```python
  jackpot_count()
  ```
  Computes how many times the game resulted in a jackpot.
  - **Returns**: An integer for the number of jackpots.

- `face_count()`
  ```python
  face_count()
  ```
  Computes the number of times a given face is rolled in each event.
  - **Returns**: A pandas DataFrame with roll numbers as index, face values as columns, and count values in the cells.

- `combination_count()`
  ```python
  combination_count()
  ```
  Computes the distinct combinations of faces rolled, along with their counts.
  - **Returns**: A pandas DataFrame with a MultiIndex of distinct combinations and a column for the associated counts.

- `permutation_count()`
  ```python
  permutation_count()
  ```
  Computes the distinct permutations of faces rolled, along with their counts.
  - **Returns**: A pandas DataFrame with a MultiIndex of distinct permutations and a column for the associated counts.