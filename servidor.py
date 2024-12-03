import grpc
from concurrent import futures
import time

import holamundo_pb2
import holamundo_pb2_grpc

# Implementación del servicio HolaMundoService
class HolaMundoService(holamundo_pb2_grpc.HolaMundoServiceServicer):
    def DecirHola(self, request, context):
        # Lógica del servicio: devolver un mensaje con el nombre recibido
        return holamundo_pb2.HolaResponse(mensaje=f"Hello, {request.nombre} from Python!")

# Iniciar el servidor
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    holamundo_pb2_grpc.add_HolaMundoServiceServicer_to_server(HolaMundoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor en ejecución...")
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
