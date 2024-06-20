import numpy as np


books = np.array([['Coffee Break NumPy', 4.6],
                  ['Lord of the Rings', 5.0],
                  ['Harry Potter', 4.3],
                  ['Winnie-the-Pooh', 3.9],
                  ['The Clown of God', 2.2],
                  ['Coffee Break Python', 4.7]])


predict_bestseller = lambda x, y : x[x[:,1].astype(float) > y]

print(predict_bestseller(books, 3.9))