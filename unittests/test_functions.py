import unittest
import operator

# To run tests, enter 'python3 unittests/test_functions.py' into the terminal

class TestFunctions(unittest.TestCase):
    
    def test_sort(self):
        scores = [15,9,36,21,30]
        sort = sorted(scores, reverse=True)
        
        """ Tests that the sort function is working """
        self.assertEqual(sort, [36,30,21,15,9])
        self.assertNotEqual(sort, [9,15,21,30,36])
    
    def test_score_update(self):
        
        """ Tests score and question number function is working """
        
        user_score = 24
        question_number = 11
        question = 'Who holds the record for the most own goals scored in the Premier League?'
        reveal = 'With 10 own goals, Richard Dunne is the only player in Premier League history to hit double figures.'
        guess = 'richard dunne'.strip(' \t\n\r').lower()
        correct_answer = 'Richard Dunne'.strip(' \t\n\r').lower()
        
        if guess == correct_answer:
            user_score += 3
            question_number += 1
            reveal = "Correct! " + reveal
        else:
            user_score += 0
            question_number += 1
            reveal = "Unlucky. " + reveal
        
        """ Tests score count function is working """
        self.assertNotEqual(user_score, 24)
        self.assertEqual(user_score, 27)
        
        """ Tests question number count function is working """
        self.assertNotEqual(question_number, 11)
        self.assertEqual(question_number, 12)
        
        """ Tests reveal returns correct outcome """
        self.assertNotEqual(reveal, 'Unlucky. With 10 own goals, Richard Dunne is the only player in Premier League history to hit double figures.')
        self.assertEqual(reveal, 'Correct! With 10 own goals, Richard Dunne is the only player in Premier League history to hit double figures.')
    
    def test_score_reset(self):
        
        question_number = 15
        user_score = 33
        
        if question_number >= 1:
            question_number = None
    
        if user_score >= 0:
            user_score = None
        
        """ Tests to ensure end quiz score reset function is working """
        self.assertNotEqual(question_number, 15)
        self.assertNotEqual(user_score, 33)
        self.assertEqual(question_number, None)
        self.assertEqual(user_score, None)
    
    def test_score_summary(self):
        
        user_score = 27
        
        if user_score >= 36:
            display_score = "Congratulations! With {0} points...".format(user_score)
        elif user_score < 11:
            display_score = "Oh dear. {0} points would have...".format(user_score)
        elif user_score < 25:
            display_score = "{0} points means guaranteed...".format(user_score)
        else:
            display_score = "Not bad. It's unlikely that {0}...".format(user_score)
        
        """ Tests to ensure score summary is correct """
        self.assertEqual(display_score, "Not bad. It's unlikely that 27...")
        self.assertNotEqual(display_score, "Congratulations! With 27 points...")
        self.assertNotEqual(display_score, "Oh dear. 27 points would have...")
        self.assertNotEqual(display_score, "27 points means guaranteed...")
    

if __name__ == '__main__':
    unittest.main()