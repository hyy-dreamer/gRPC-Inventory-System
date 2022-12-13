import grpc
import sys
sys.path.insert(0, '/Users/yuyanghuang/Desktop/API design/inventory/service')
import inventory_pb2_grpc
import inventory_pb2


class InventoryClient(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = inventory_pb2_grpc.InventoryServiceStub(self.channel)
    def GetBook(self, id):
        request = inventory_pb2.GetBookRequest(id=id)
        response = self.stub.GetBook(request)
        return response

    def CreateBook(self, Book):
        request = inventory_pb2.Book(title = Book["title"], author = Book["author"], genre = Book["genre"], PublishYear = Book["PublishYear"])
        response = self.stub.CreateBook(request)
        return response
        

if __name__ == "__main__":
    client = InventoryClient()
    Book = {"title": "Who are you", "author": "yuyang", "genre": "Fiction", "PublishYear": 2020}
    print(client.CreateBook(Book))
