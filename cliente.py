import grpc
import holamundo_pb2
import holamundo_pb2_grpc

# Crear un canal de comunicación con el servidor gRPC
def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = holamundo_pb2_grpc.HolaMundoServiceStub(channel)

    # Enviar solicitud al servidor
    response = stub.DecirHola(holamundo_pb2.HolaRequest(nombre='World'))

    # Mostrar la respuesta del servidor
    print(f'Respuesta: {response.mensaje}')

if __name__ == '__main__':
    run()
