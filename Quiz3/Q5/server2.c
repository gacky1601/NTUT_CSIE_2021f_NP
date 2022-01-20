#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
//Server – pis.c, gcc pis.c -o simples -lunp
#include <math.h>
double getPi(int x, int y)
{
    x = y / 2;
    double pi = 0, sign = -1;
    if (x % 2 == 0)
        sign = 1;
    else
        sign = -1;
    for (int i = x; i < y; i++)
    {
        pi = pi + sign * (1 / (2.0 * i + 1));
        sign = sign * (-1);
    }
    return 4 * pi;
}
double gete(int n){
    int i,n;
    double sum =1,t=1 ,t1=1,sum1=1;
    for(i=1;i<=n;i++)
    {
        t=t*i;
        sum= sum+1/t;
    }
    n = n/2;
    for(i=1;i<=n;i++)
    {
        t1=t1*i;
        sum1= sum1+1/t1;
    }
    sum =sum-sum1;
    return sum;
}


int main(int argc, char *argv[])
{
    double r = 0;
    int y = 0;
    char message[256], inputBuffer[256];
    int sockfd = 0, clientSockfd = 0; //socket的建立
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1)
    {
        printf("Fail to create a socket.");
    }
    struct sockaddr_in serverInfo, clientInfo; //socket的連線
    int addrlen = sizeof(clientInfo);
    bzero(&serverInfo, sizeof(serverInfo));
    serverInfo.sin_family = AF_INET;
    serverInfo.sin_addr.s_addr = INADDR_ANY;
    serverInfo.sin_port = htons(8900);
    bind(sockfd, (struct sockaddr *)&serverInfo, sizeof(serverInfo));
    listen(sockfd, 8);
    while (1)
    {
        clientSockfd = accept(sockfd, (struct sockaddr *)&clientInfo, &addrlen);
        recv(clientSockfd, inputBuffer, sizeof(inputBuffer), 0);
        y = atoi(inputBuffer);
        r = gete(y);
        snprintf(message, sizeof(message), "%.12f", r);
        printf("Get:=>%s,%.12f\n", inputBuffer, r);
        send(clientSockfd, message, sizeof(message), 0);
    }
    return 0;
}