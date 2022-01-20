#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <unistd.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <netinet/in.h> 
int main(int argc , char *argv[]) { 
    char message[256] = {"Hi Server, this is client.\n"}, receiveMessage[256] = {}; 
    int sockfd = 0; 
    sockfd = socket(AF_INET , SOCK_STREAM , 0); 
    if (sockfd == -1){ printf("Fail to create a socket."); } 
    struct sockaddr_in info; 
    bzero(&info,sizeof(info)); 
    info.sin_family = PF_INET; 
    info.sin_addr.s_addr = inet_addr("127.0.0.1"); 
    info.sin_port = htons(8700); 
    int err = connect(sockfd,(struct sockaddr *)&info,sizeof(info)); 
    if(err==-1){ printf("Connection error"); } 
    send(sockfd, message, sizeof(message),0); 
    while(1){ 
        recv(sockfd, receiveMessage, sizeof(receiveMessage),0); 
        printf("Server said: %s\n", receiveMessage); 
        if(strcmp("end",receiveMessage)==0 ||strcmp("you win, 10.5 get",receiveMessage)==0 || strcmp("you lose , greater than 10.5",receiveMessage)==0 ){ 
            break; 
        } 
        printf("Input 'more' to get more card, input 'end' to stop the program. \n"); 
        printf("Please input message send to sever:\n"); 
        scanf("%s",&message); 
        send(sockfd, message, sizeof(message),0); 
        if(strcmp("end",message)==0){ 
            strcpy(receiveMessage,"end"); 
            break; 
        } 
    } 
    printf("%s, close Socket\n", receiveMessage); 
    close(sockfd); 
    return 0; 
} 