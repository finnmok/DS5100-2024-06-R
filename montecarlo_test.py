import unittest
import numpy as np
import pandas as pd
# from montecarlo.montecarlo import *
import montecarlo.montecarlo as mc

class MonteCarloTestDie(unittest.TestCase):

    def test_1_faces_isnt_numpy(self):
        """
        Check that input for faces is numpy array (input = list)
        """
        faces = ['a','b','c']
        with self.assertRaises(TypeError):
            mc.Die(faces)

    def test_2_faces_is_numpy(self):
        """
        Check that input for faces is numpy array (input = numpy array)
        """
        faces = np.array(['a','b','c'])
        try:
            mc.Die(faces)
        except TypeError:
            self.fail("Correct Input Numpy Array Resulting in Error")
    
    def test_3_faces_dtype_incorrect(self):
        """
        Check that input for faces is a string or number datatype (input = array with a dictionary)
        """
        faces = np.array(['a',1,'c',{'dictionary':'value'}])
        
        with self.assertRaises(TypeError):
            mc.Die(faces)

    def test_4_faces_dtype_correct(self):
        """
        Check that input for faces is a string or number datatype (input = array with strings and numerics)
        """
        faces = np.array(['a',1,'c',2.0])
        try:
            mc.Die(faces)
        except TypeError:
            self.fail("Correct Inputs Result in Error")

    def test_5_faces_not_unique(self):
        """
        Check that input for faces are unique values
        """
        faces = np.array([1,2,3,4,4])
        with self.assertRaises(ValueError):
            mc.Die(faces)

    def test_6_faces_unique(self):
        """
        Check that input for faces are unique values
        """
        faces = np.array([1,2,3])
        try:
            mc.Die(faces)
        except:
            self.fail("Values Unique and Resulting in Error")

    def test_7_set_wts_invalid_face(self):
        """Check setting weight for a face that doesn't exist"""
        faces = np.array([1, 2, 3])
        die = mc.Die(faces)
        with self.assertRaises(IndexError):
            die.set_wts(6, 2.0)

    def test_8_set_wts_invalid_weight(self):
        """Check setting weight to a non-numeric value"""
        faces = np.array([1, 2, 3])
        die = mc.Die(faces)
        with self.assertRaises(ValueError):
            die.set_wts(1, 'invalid')

    def test_9_set_wts_negative_weight(self):
        """Check setting weight to a negative value"""
        faces = np.array([1, 2, 3])
        die = mc.Die(faces)
        with self.assertRaises(ValueError):
            die.set_wts(1, -1.0)

    def test_10_set_wts_valid(self):
        """Check setting weight to a valid numeric value"""
        faces = np.array([1, 2, 3])
        die = mc.Die(faces)
        try:
            die.set_wts(1, 2.0)
        except:
            self.fail("Setting weight failed with valid inputs")

    def test_11_roll_invalid_n_rolls(self):
        """Check rolling die with non-integer number of rolls"""
        faces = np.array([1, 2, 3])
        die = mc.Die(faces)
        with self.assertRaises(TypeError):
            die.roll('invalid')

    def test_12_roll_valid_n_rolls(self):
        """Check rolling die with valid number of rolls"""
        faces = np.array([1, 2, 3])
        die = mc.Die(faces)
        try:
            die.roll(10)
        except:
            self.fail("Rolling the die failed with valid inputs")

    def test_13_get_die_wts(self):
        """Check getting die weights"""
        faces = np.array([1, 2, 3])
        die = mc.Die(faces)
        self.assertTrue(isinstance(die.get_die_wts(), pd.DataFrame))



class MonteCarloTestGame(unittest.TestCase):

    def setUp(self):
        self.die1 = mc.Die(np.array([1, 2, 3]))
        self.die2 = mc.Die(np.array([1, 2, 3]))

    def test_1_not_dice(self):
        """Check intial setting game with invalid dice list"""
        with self.assertRaises(TypeError):
            mc.Game(["not a die"])

    def test_2_init_different_faces(self):
        """Check initial setting game with different faced dice"""
        die3 = mc.Die(np.array([1, 2, 4]))
        with self.assertRaises(IndexError):
            mc.Game([self.die1, die3])

    def test_3_init_valid_dice(self):
        """Check list of dice in game object"""
        try:
            self.game = mc.Game([self.die1, self.die2])
        except:
            self.fail("Valid Dice in List Resulting in Error")

    def test_4_play_invalid_n_rolls(self):
        """Check playing game with non-integer number of rolls"""
        self.game = mc.Game([self.die1, self.die2])
        with self.assertRaises(TypeError):
            self.game.play("invalid")

    def test_5_play_valid_n_rolls(self):
        """Check playing game with valid number of rolls"""
        self.game = mc.Game([self.die1, self.die2])
        try:
            self.game.play(10)
        except:
            self.fail("Playing game failed with valid inputs")

    def test_6_invalid_form_most_recent_play(self):
        """Check retrieving play results with invalid form"""
        self.game = mc.Game([self.die1, self.die2])
        self.game.play(10)
        with self.assertRaises(ValueError):
            self.game.get_most_recent_play(form="WideOrNarrow")

    def test_7_valid_form_most_recent_play(self):
        """Check retrieving play results with valid form"""
        self.game = mc.Game([self.die1, self.die2])
        self.game.play(10)
        try:
            self.game.get_most_recent_play(form="wide")
            self.game.get_most_recent_play(form="narrow")
        except:
            self.fail("Retrieving play results failed with valid inputs")

class MonteCarloTestAnalyzer(unittest.TestCase):

    def setUp(self):
        self.die1 = mc.Die(np.array([1, 2, 3, 4, 5, 6]))
        self.die2 = mc.Die(np.array([1, 2, 3, 4, 5, 6]))
        self.game = mc.Game([self.die1, self.die2])
        self.game.play(10)

    def test_1_invalid_game(self):
        """Check initialization with invalid game object"""
        with self.assertRaises(ValueError):
            mc.Analyzer(self.die1)

    def test_2_valid_game(self):
        """Check initialization with valid game object"""
        try:
            mc.Analyzer(self.game)
        except:
            self.fail("Initializing Analyzer failed with valid inputs")
    
    def test_3_jackpot_count(self):
        """Check computing jackpot count"""
        self.analyzer = mc.Analyzer(self.game)
        try:
            self.analyzer.jackpot_count()
        except:
            self.fail("Computing jackpot count failed")

    def test_4_face_count(self):
        """Check face count"""
        self.analyzer = mc.Analyzer(self.game)
        try:
            self.analyzer.face_count()
        except:
            self.fail("Computing face count failed")

    def test_5_combination_count(self):
        """Check combination count"""
        self.analyzer = mc.Analyzer(self.game)
        try:
            self.analyzer.combination_count()
        except:
            self.fail("Computing combination count failed")

    def test_6_permutation_count(self):
        """Check permutation count"""
        self.analyzer = mc.Analyzer(self.game)
        try:
            self.analyzer.permutation_count()
        except:
            self.fail("Computing permutation count failed")
    

if __name__ == '__main__':
    unittest.main(verbosity=3)