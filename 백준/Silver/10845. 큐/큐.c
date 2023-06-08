#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int front = -1, rear = -1;
void push(int *q,int data)
{
   q[++rear] = data;
}

int pop(int *q)
{
    if(front == rear)
        return -1;
    else
        return q[++front];
}   

int empty()
{
    if(front == rear)
        return 1;
    else
        return 0;
}

int size()
{
    return rear - front;
}


int frontcheck(int *q)
{
    if(front == rear)
        return -1;
    else
        return q[front +1];
}

int backcheck(int *q)
{
    if(front == rear)
        return -1;
    else 
        return q[rear];
}

int main(void)
{
    int n, push_data;
    scanf("%d",&n);

    getchar();
    char command[6];
    int q[10000];
    for(int i=0; i<n; i++)
    {
        scanf("%s",command);
        if(!strcmp(command,"push"))
        {
            scanf("%d",&push_data);
            push(q,push_data);
        }
        else if(!strcmp(command,"pop"))
        {
            printf("%d\n",pop(q));
        }
        else if(!strcmp(command,"size"))
            printf("%d\n",size());
        else if(!strcmp(command,"empty"))
            printf("%d\n",empty());
        else if(!strcmp(command,"front"))
            printf("%d\n",frontcheck(q));
        else if(!strcmp(command,"back"))
            printf("%d\n",backcheck(q));
    }
    return 0;
}