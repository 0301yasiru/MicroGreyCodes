// Program by: Yasiru Senerath Karunanayaka


#include <iostream>
#include <WS2tcpip.h>

#pragma comment (lib, "ws2_32.lib")

using namespace std;

int main(){
    cout << "Server Started ..." << endl;

    // initialize winsock
    WSADATA wsData;
    WORD ver = MAKEWORD(2,2);

    int wsOK = WSAStartup(ver, &wsData);

    if (wsOK != 0){
        cerr << "Can't initialize the winsocket. Quitting" << endl;
        return 0;
    }

    // create a socket

    SOCKET listening = socket(AF_INET, SOCK_STREAM, 0);
    if (listening == INVALID_SOCKET){
        cerr << "Cannot create a socket! Quiting";
        return 0;
    }


    // bind the socket to ip and port
    sockaddr_in hint;
    hint.sin_family = AF_INET;
    hint.sin_port = htons(9090);
    hint.sin_addr.S_un.S_addr = INADDR_ANY;

    bind(listening, (sockaddr*)&hint, sizeof(hint));

    // tell the winsock that this socket is for listening (server)
    listen(listening, SOMAXCONN);

    // wait for connection
    sockaddr_in client;
    int clientSize = sizeof(client);

    SOCKET clientSocket = accept(listening, (sockaddr*)&client, &clientSize);
    if (clientSocket == INVALID_SOCKET){
        cout << "Invalid client socket detected";
    }

    char host[NI_MAXHOST]; // client remote name
    char service[NI_MAXHOST]; // service port number

    ZeroMemory(host, NI_MAXHOST);
    // close listening socket







    // close the socket

    // shutdown the winsock

    return 0;
}// end of the main file
