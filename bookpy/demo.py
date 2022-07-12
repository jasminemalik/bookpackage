import pandas as pd
from booklover import BookLover

jaslibrary3 = BookLover('jas2','jas.com','mys')
jaslibrary3.add_book('test1',1)
jaslibrary3.num_books_read()
jaslibrary3.add_book('test5',5)
jaslibrary3.fav_books()