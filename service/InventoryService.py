import inventory_pb2 
import inventory_pb2_grpc
import grpc
from concurrent import futures






class InventoryService(inventory_pb2_grpc.InventoryServiceServicer):
    # When create book is called, the data is stored in the dictionary data
    # A message indicating creation success will be returned
    def CreateBook(self, request, context):
        title = request.title
        author = request.author
        genre = request.genre
        PublishYear = request.PublishYear
        id = len(data) + 1
        data[str(id)] = {"title": title, "author": author, "genre": genre, "PublishYear": PublishYear}
        return inventory_pb2.BookCreateResponse(created="book created successfully!")

    def GetBook(self, request, context):
        return inventory_pb2.Book(**data.get(request.id, {}))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

data = {
   "1": {"title": "life is miserable", "author": "James", "genre": "Fiction", "PublishYear": 2022},
   "2": {"title": "I am graduating", "author": "Lebron", "genre": "Fiction", "PublishYear": 2021},
   "3": {"title": "Who I am", "author": "Kobe", "genre": "Fiction", "PublishYear": 2020},
}


if __name__ == '__main__':
    print("running the gRPC server")
    serve()