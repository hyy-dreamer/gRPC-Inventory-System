from Inventory_client import InventoryClient

class Get_Book_Titles(object):
    # return a list of titles
    def GetBookTilte(self, ISBNs):
        client = InventoryClient()
        booklist = []
        for id in ISBNs:
            booklist.append(client.GetBook(id).title)
        return booklist
        



if __name__ == "__main__":
    getbook = Get_Book_Titles()
    ISBNs = ["1", "2"]
    print(getbook.GetBookTilte(ISBNs))
    