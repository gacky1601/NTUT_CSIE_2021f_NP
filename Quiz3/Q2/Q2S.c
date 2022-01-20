#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <unistd.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <netinet/in.h> 
double getCard(); 
int main(int argc , char *argv[]){ 
    
    char message[256] = {"Hi, this is server.\n"}; 
    double player_score = 0; 
    int sockfd = 0;
    sockfd = socket(AF_INET , SOCK_STREAM , 0); 
    if (sockfd == -1){ printf("Fail to create a socket."); } 
    struct sockaddr_in serverInfo; 
    
    bzero(&serverInfo,sizeof(serverInfo)); 
    serverInfo.sin_family = AF_INET; 
    serverInfo.sin_addr.s_addr = INADDR_ANY; 
    serverInfo.sin_port = htons(8700); 
    bind(sockfd,(struct sockaddr *)&serverInfo,sizeof(serverInfo)); 
    listen(sockfd, 8); 
    
    struct sockaddr_in clientInfo;
    int clientSockfd;
    while (1){
        int addrlen = sizeof(clientInfo); 
        bzero(&clientInfo,sizeof(clientInfo)); 
        clientSockfd = accept(sockfd,(struct sockaddr*) &clientInfo, &addrlen); 
        char receiveMessage[256] = {};
        int pid=fork();
        if(pid==0){
            send(clientSockfd, message, sizeof(message),0); 
            while(1){ 
                recv(clientSockfd, receiveMessage, sizeof(receiveMessage),0); 
                printf("Client said: %s\n",receiveMessage); 
                if(strcmp("more",receiveMessage)==0){ 
                    player_score = player_score + getCard(); 
                    if(player_score<10.5){ 
                        sprintf(message,"%lf",player_score); 
                    }else if (player_score==10.5){ 
                        strcpy(message,"you win, 10.5 get"); 
                    }else{ 
                        strcpy(message,"you lose , greater than 10.5");
                    } 
                    send(clientSockfd, message, sizeof(message),0); 
                } 
                else if(strcmp("end",receiveMessage)==0){ 
                    break; 
                } 
            } 
            printf("%s, close Socket\n", receiveMessage); 
            close(clientSockfd); 
            return 0; 
        }
    }
    
} 
double getCard() { 
srand( time(NULL)); 
/* 指定亂數範圍 */ 
int min = 1; 
int max = 13; 
/* 產生 [min , max] 的整數亂數 */ 
int card = rand() % (max - min + 1) + min; 
double point = (double)card; 
if (point >10.0) point = 0.5; 
return point; 
} 
