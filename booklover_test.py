import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test1lib = BookLover('jas','jas.edu', 'mys')
        test1lib.add_book('book1',5)
        
        exp = True
        self.assertEqual(test1lib.has_read('book1'), exp)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        
        test2lib = BookLover('jas', 'jas.edu', 'mys')
        test2lib.add_book('book2',5)
        test2lib.add_book('book2',3)
        
        exp_num = 1
        self.assertEqual(test2lib.num_books_read(), exp_num)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        
        test3lib = BookLover('jas','jas.edu','mys')
        test3lib.add_book('book3',5)
        
        exp_3 = True
        self.assertEqual(test3lib.has_read('book3'), exp_3)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test4lib = BookLover('jas','jas.edu','mys')
        test4lib.add_book('book4',5)
        
        self.assertFalse(test4lib.has_read('nobook'))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        
        test5lib = BookLover('jas','jas.edu','mys')
        test5lib.add_book('book5',5)
        test5lib.add_book('book6',5)
        test5lib.add_book('book7',5)
        
        exp_num = 3
        self.assertEqual(test5lib.num_books_read(), exp_num)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        
        test6lib = BookLover('jas','jas.edu','mys')
        test6lib.add_book('book5',5)
        test6lib.add_book('book6',1)
        test6lib.add_book('book7',5)
        
        self.assertEqual(len(test6lib.fav_books()),2)
        

if __name__ == '__main__':
    unittest.main(verbosity=3)