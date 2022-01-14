import unittest
import sqlite3

class Test(unittest.TestCase):
    def test_db(self):
        connection = sqlite3.connect('cards.db')
        self.assertIsNot(connection, 0)
        cursor = connection.cursor()
        cursor.execute("select number, amount from cards limit 3") # выбор 3 строк из таблицы
        record = cursor.fetchall()
        self.assertGreater(len(record), 0)
        cursor.close()

if __name__ == '__main__':
    unittest.main()
