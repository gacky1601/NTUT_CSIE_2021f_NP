#include <sys/types.h> // client - pic.c
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>  // Client – piclec.c
#include <stdlib.h> // gcc simplec.c -o simplec -lunp
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
int main(int argc, char *argv[])
{
    char message[256] = "50", receiveMessage[256]; //Send/receive a message to server;
    int sockfd = 0;
    struct sockaddr_in info; //socket的連線
    double value = 0, result = 0;
    pid_t pid;
    int fd[2];
    pipe(fd);
    scanf("%s", message);
    pid = fork(); //fork a child process
    if (pid < 0)
    { // error occurred
        fprintf(stderr, "Fork Failed");
        return 1;
    } //socket的建立
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1)
    {
        printf("Fail to create a socket.");
    }
    bzero(&info, sizeof(info));

    info.sin_family = PF_INET;
    info.sin_addr.s_addr = inet_addr("192.168.16.132"); //localhost test
    if (pid == 0)
    { // child process
        close(fd[0]);
        //strcpy(message, "400");
        info.sin_port = htons(8700);
        int err = connect(sockfd, (struct sockaddr *)&info, sizeof(info));
        if (err == -1)
        {
            printf("Connection error");
        }
        send(sockfd, message, sizeof(message), 0);
        recv(sockfd, receiveMessage, sizeof(receiveMessage), 0);
        printf("child Server: %s\n", receiveMessage);
        value = atof(receiveMessage);
        printf("child Server: %.12f\n", value);
        write(fd[1], &value, sizeof(value));
        close(fd[1]);
        printf("close Socket\n");
        close(sockfd);
    }
    else
    {
        info.sin_addr.s_addr = inet_addr("192.168.16.133"); //localhost test
        info.sin_port = htons(8900);
        int err = connect(sockfd, (struct sockaddr *)&info, sizeof(info));
        if (err == -1)
        {
            printf("Connection error");
        }
        //strcpy(message, "900");
        send(sockfd, message, sizeof(message), 0);
        recv(sockfd, receiveMessage, sizeof(receiveMessage), 0);
        pid = wait(NULL); //parent wait child complete
        printf("parent Server: %s\n", receiveMessage);
        printf("close Socket\n");
        close(sockfd);
        result = atof(receiveMessage);
        wait(NULL); // parent wait child complete
        read(fd[0], &value, sizeof(value));
        printf("parent Server: %.12f\n", result);
        printf("parent Server from child: %.12f\n", value);
        printf("parent Server total: %.12f\n", value + result);
        close(fd[0]);
    }
    return 0;
}