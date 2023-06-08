#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int top = -1;

void push(int *s,int data)
{
    s[++top] = data;
}

int pop(int *s)
{
    if(top == -1)
        return -1;
    return s[top--];
}

int size()
{
    return top +1;
}

int empty()
{
    if(top == -1)
        return 1;
    else return 0;
}

int topcheck(int *s)
{
    if(top == -1)
        return -1;
    return s[top];
}

int main()
{
    int n, push_data;
    scanf("%d",&n);
    getchar();
    int stack[10000];
    char command[6];
    for(int i=0; i<n; i++)
    {
        scanf("%s",command);
        if(!strcmp(command,"push"))
        {
            scanf("%d",&push_data);
            push(stack,push_data);
        }
        else if(!strcmp(command,"pop"))
        {
            printf("%d\n",pop(stack));
        }
        else if(!strcmp(command,"size"))
            printf("%d\n",size());
        else if(!strcmp(command,"empty"))
            printf("%d\n",empty());
        else if(!strcmp(command,"top"))
            printf("%d\n",topcheck(stack));
    }
    return 0;
}