import numpy as np
import pandas as pd
from collections import Counter
from itertools import combinations, permutations

class Die():
    def __init__(self,faces):
        # Takes a NumPy array of faces as an argument. Throws a TypeError if not a NumPy array.
        if not isinstance(faces, np.ndarray):
            raise TypeError("Must be a Numpy Array for Faces")
        
        # The array’s data type dtype may be strings or numbers
        if not (np.issubdtype(faces.dtype, np.number) or np.issubdtype(faces.dtype, np.str_) or np.issubdtype(faces.dtype, np.object_)):
            raise TypeError("Numpy Array Must be String or Numbers Datatypes")
        
        # The array’s values must be distinct. Tests to see if the values are distinct and raises a ValueError if not
        if np.unique(faces).shape[0] != faces.shape[0]:
            raise ValueError("Values Must be Distinct")
        
        self.faces = faces
        self.n_faces = self.faces.shape[0]
        
        # Internally initializes the weights to 1 for each face.
        self.wts = np.ones(self.n_faces)
        
        # Saves both faces and weights in a private data frame with faces in the index.
        self.__die_df = pd.DataFrame(
            data=self.wts,
            index=self.faces,
            columns = ['wt'])
        
    # Takes two arguments: the face value to be changed and the new weight.
    def set_wts(self,which_face,new_wt):
        
        # Checks to see if the face passed is valid value, i.e. if it is in the die array. If not, raises an IndexError.
        if which_face not in self.faces:
            raise IndexError("Invalid Value for Die Face")
        
        # Checks to see if the weight is a valid type, i.e. if it is numeric (integer or float) or castable as numeric. If not, raises a TypeError.
        try:
            new_wt = float(new_wt)
        except (ValueError, TypeError):
            raise TypeError("Updated Weight is Not a Valid Type")
            
        self.__die_df.loc[which_face,'wt'] = new_wt
        
    #Takes a parameter of how many times the die is to be rolled; defaults to 1                   
    def roll(self,n_rolls = 1):
        #This is essentially a random sample with replacement, from the private die data frame, that applies the weights.
        
        # Returns a Python list of outcomes
        # Does not store internally these results
        return list(np.random.choice(
            a = self.__die_df.index.values,
            p = self.__die_df['wt']/self.__die_df['wt'].sum(),
            size=n_rolls) )
    
    def get_die_wts(self):
        return self.__die_df
                     
class Game():
    # Takes a single parameter, a list of already instantiated similar dice.
    def __init__(self,die):
        # Ideally this would check if the list actually contains Die objects
        if isinstance(die,list) != True:
            get_die = list()
            get_die.append(die)
        if not all([isinstance(d,Die) for d in die]):
            raise TypeError("All Dice Must be Dice Type")
        # and that they all have the same faces, but this is not required for this project.
        if len(die) > 1:
            if all([all(die[i].faces == die[i+1].faces) for i in range(len(die)-1)]) == False:
                raise IndexError("All Dice Must Have the Same Faces")
        self.dice = die
    
    # Takes an integer parameter to specify how many times the dice should be rolled.
    def play(self, n_rolls):
        
        # Saves the result of the play to a private data frame.
        #The data frame should be in wide format
        self.__play_df = pd.DataFrame(
            # i.e. have the roll number as a named index,
            columns = range(n_rolls),
            # columns for each die number (using its list index as the column name)
            index = range(len(self.dice)),
            # and the face rolled in that instance in each cell.
            data = [d.roll(n_rolls) for d in self.dice])
        
        self.__play_df.columns.names = ['roll_number']
        self.__play_df.index.names = ['die_number']
        self.__play_df = self.__play_df.T
        
    # This method just returns a copy of the private play data frame to the user.
    # Takes a parameter to return the data frame in narrow or wide form which defaults to wide form.
    def get_most_recent_play(self,form='wide'):
        
        if form == 'wide':
            return self.__play_df
        elif form == 'narrow':
            # The narrow form will have a MultiIndex, comprising the roll number and the die number (in that order), and a single column with the outcomes (i.e. the face rolled).
            return self.__play_df.reset_index().melt(
                id_vars='roll_number',
                var_name='die_number',
                value_name='face_rolled').set_index(['roll_number','die_number'])
        else:
            # This method should raise a ValueError if the user passes an invalid option for narrow or wide.
            raise ValueError("Form for Play Data is Invalid")
        
    
class Analyzer():
    def __init__(self,game):
        if not isinstance(game,Game):
            # Takes a game object as its input parameter. Throw a ValueError if the passed value is not a Game object.
            raise ValueError("Passed Value Not a Game Object")
        
        self.game = game
    
    def jackpot_count(self):
        # Computes how many times the game resulted in a jackpot.
        # Returns an integer for the number of jackpots.
        return sum([self.game.get_most_recent_play().iloc[n,:].nunique() == 1 for n in range(len(self.game.get_most_recent_play()))])
    
    def face_count(self):
        # Computes how many times a given face is rolled in each event. For example, if a roll of five dice has all sixes, then the counts for this roll would be 5 for the face value 6 and 0 for the other faces.
        # Returns a data frame of results.
        # The data frame has an index of the roll number, face values as columns, and count values in the cells (i.e. it is in wide format).
        return self.game.get_most_recent_play().apply(lambda row: row.value_counts().reindex(self.game.dice[0].faces).fillna(0).astype(int), axis=1)
    
    #Computes the distinct combinations of faces rolled, along with their counts.
    def combination_count(self):
        cts = dict(
            sum(
                [Counter(combinations(roll,2)) for roll in self.game.get_most_recent_play().values],
                Counter()
            )
        )
        # Returns a data frame of results.
        #The data frame should have an MultiIndex of distinct combinations and a column for the associated counts.
        return pd.DataFrame(
            index=cts.keys(),
            data=cts.values()
        ).sort_index().rename({0:"n_combinations"},axis=1)
    
    # Computes the distinct permutations of faces rolled, along with their counts.
    def permutation_count(self):
        cts = dict(
            sum(
                [Counter(permutations(roll,2)) for roll in self.game.get_most_recent_play().values],
                Counter()
            )
        )
        # Returns a data frame of results.
        #The data frame should have an MultiIndex of distinct permutations and a column for the associated counts.
        return pd.DataFrame(
            index=cts.keys(),
            data=cts.values()
        ).sort_index().rename({0:"n_permutations"},axis=1)