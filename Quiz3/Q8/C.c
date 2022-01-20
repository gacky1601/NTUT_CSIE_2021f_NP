#include<stdio.h> //udpc.c
#include<string.h>
#include<stdlib.h>
#include<unistd.h>
#include<arpa/inet.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<netinet/in.h>
#define SERVER "127.0.0.1"
#define BUFLEN 255
#define PORT 8885
void die(char *s) { 
    perror(s);
    exit(1);
}
unsigned long fsize(char* file) {
    FILE * f = fopen(file, "r");
    fseek(f, 0, SEEK_END); 
    unsigned long len = (unsigned long)ftell(f);
    fclose(f);
    return len;
}
int main(void) {
    if(AF_INET==PF_INET){
        printf("QWEqweqweqweqweq\nqwweqweq\n");
    }
    struct sockaddr_in si_other;
    char message[BUFLEN], fname[20], str[10];
    FILE *f;
    int s, i;
    unsigned long size;
    s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (s == -1) { die("socket"); }
    memset((char *) &si_other, 0, sizeof(si_other));
    si_other.sin_family = AF_INET;
    si_other.sin_port = htons(PORT); 
    if (inet_aton(SERVER , &si_other.sin_addr) == 0) { // converts the specified string, 
        fprintf(stderr, "inet_aton() failed\n");
        exit(1);
    }
    
    strcpy(fname,"car.png");
    printf("%s\n",fname);
    sendto(s, fname, sizeof(fname), 0, (struct sockaddr *) &si_other, sizeof(si_other));
    
    memset(message,0,BUFLEN);
    size = fsize(fname); 
    printf("%ld",(size % BUFLEN)); 
    sprintf(str, "%ld", size);
    sendto(s, str, sizeof(str), 0 , (struct sockaddr *) &si_other, sizeof(si_other));
    f=fopen(fname,"rb");
    while (1){
        memset(message,0, sizeof(message));
        int nread=fread(message, 1,BUFLEN,f);
        printf("Bytes read %d \n", nread); 
        //printf("%s\n",message); 
        if(nread>0){
            if (sendto(s, message, nread , 0 , (struct sockaddr *) &si_other, sizeof(si_other))==-1) {die("sendto()");}
        }
        if(nread<BUFLEN){
            if(feof(f)){ printf("\nEnd of file\n"); break;}
            if(ferror(f)) {  printf("\nError reading\n");break;}
        }
    }
    fclose(f);
    close(s);
    return 0;
}
