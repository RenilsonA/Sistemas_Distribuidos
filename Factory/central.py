import os
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "subscriber.json"

timeout = 2.0

subscriber = pubsub_v1.SubscriberClient()
subscription_path = 'projects/emergency-398719/subscriptions/factory'

def callback(message):
    print(f'data: {message.data[0]}')
    SENSOR_MACHINE_1 = 1
    SENSOR_MACHINE_2 = 2
    SENSOR_TEMPERATURE = 3
    SENSOR_PRESSURE = 4
    SENSOR_GAS = 5
    if(message.data[0] == SENSOR_MACHINE_1):
        if(message.data[1] == 1):
            print("Maquina 1 desligada")
        elif(message.data[1] == 2):
            print("Maquina 1 ligada com pouca carga.")
        elif(message.data[1] == 3):
            print("Maquina 1 ligada com carga recomendada.")
        elif(message.data[1] == 4):
            print("Maquina 1 ligada com muita carga.")
        else:
            print("Maquina 1 será desligada, risco de explosão.")
    elif(message.data[0] == SENSOR_MACHINE_2):
        if(message.data[1] == 1):
            print("Maquina 2 desligada")
        elif(message.data[1] == 2):
            print("Maquina 2 ligada com pouca carga.")
        elif(message.data[1] == 3):
            print("Maquina 2 ligada com carga recomendada.")
        elif(message.data[1] == 4):
            print("Maquina 2 ligada com muita carga.")
        else:
            print("Maquina 2 será desligada, risco de explosão.")
    elif(message.data[0] == SENSOR_TEMPERATURE):
        if(message.data[1] == 1):
            print("Temperatura baixa, desligar ar condicionado e ventiladores.")
        elif(message.data[1] == 2):
            print("Temperatura relativamente baixa, ligue ar condicionado em uma temperatura amena.")
        elif(message.data[1] == 3):
            print("Temperatura moderada, ligar ar condicionado em temperatura amena e ventiladores.")
        elif(message.data[1] == 4):
            print("Temperatura alta, ligar ar condicionado em baixa temperatura e ventiladores.")
        else:
            print("Temperatura muito alta, exiba em um letreiro para permanecer no local por no máximo 20 minutos e mande hidratarem-se.")
    elif(message.data[0] == SENSOR_PRESSURE):
        if(message.data[1] == 1):
            print("Pressão atmosférica.")
        elif(message.data[1] == 2):
            print("Pressão no estágio 1.")
        elif(message.data[1] == 3):
            print("Pressão no estágio 2.")
        elif(message.data[1] == 4):
            print("Pressão no estágio 3, diminuindo pressão.")
        else:
            print("Pressão excedendo o máximo permitido, desligando.")
    elif(message.data[0] == SENSOR_GAS):
        if(message.data[1] == 1):
            print("Sem gás no local.")
        else:
            print("Há gás no local. Ligar exaustores e abrir persianas.")
    message.ack()           

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f'Esperando dados: {subscription_path}')


with subscriber:                       
    try:
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel() 
        streaming_pull_future.result() 
