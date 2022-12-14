from unittest import TestCase, mock
import unittest
import Inventory_client
from get_book_titles import Get_Book_Titles

def fakeGetBook(self, id):
    class object:
        title = "We are testing"
    return object
    
class test(TestCase):
    @mock.patch.object(Inventory_client.InventoryClient, 'GetBook', fakeGetBook)
    def test_get_book_titles(self):
        getbook = Get_Book_Titles()
        ISBNs = ["1"]
        self.assertEqual(getbook.GetBookTilte(ISBNs), ["We are testing"])

    def test_get_book_tilles_with_server(self):
        getbook = Get_Book_Titles()
        ISBNs = ["1"]
        self.assertEqual(getbook.GetBookTilte(ISBNs), ["life is miserable"])

if __name__ == "__main__":
    unittest.main()