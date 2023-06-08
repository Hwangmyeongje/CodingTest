#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int front = -1, rear =-1;
void push(int *q,int x)
{
    q[++rear] = x;
}

int pop(int *q)
{
    if(front == rear)
        return -1;
    return q[++front];
}

int size()
{
    return rear - front;
}

int empty()
{
    if(front == rear)
        return 1;
    else
        return 0;
}

int frontcheck(int *q)
{
    if(front == rear)
        return -1;
    return q[front+1];  
}

int backcheck(int *q)
{
    if(front == rear)
        return -1;
    return q[rear];
}

int main()
{
    int n,x;
    scanf("%d",&n);
    getchar();
    int queue[2000000];
    for(int i= 0; i<n; i++)
    {
        char command[6];
        scanf("%s",command);
        if(!strcmp(command,"push"))
        {
            scanf("%d\n",&x);
            push(queue,x);
        }
        else if(!strcmp(command,"pop"))
            printf("%d\n",pop(queue));
        else if(!strcmp(command,"size"))
            printf("%d\n",size());
        else if(!strcmp(command,"empty"))
            printf("%d\n",empty());
        else if(!strcmp(command,"front"))
            printf("%d\n",frontcheck(queue));
        else if(!strcmp(command,"back"))
            printf("%d\n",backcheck(queue));
    }
    return 0;
}