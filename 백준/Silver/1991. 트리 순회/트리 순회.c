#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct TreeNode
{
    char key;
    struct TreeNode * left, *right;
}TreeNode;

TreeNode* makeNode(char key)
{
    TreeNode * node = (TreeNode *)malloc(sizeof(TreeNode));
    node -> key = key;
    node->left = node->right =NULL;
    return node;
}

TreeNode* findNode(TreeNode * root, char key)
{
    TreeNode * p =root;
    if(root == NULL)
        return NULL;
    if(root->key == key)
        return root;
    p = findNode(root->left,key);
    if(p)
        return p;
    return findNode(root->right, key);
}

TreeNode * insertNode(TreeNode *root,char key,char left,char right)
{
    root ->key = key;
    if(left != '.')
        root->left = makeNode(left);
    if(right != '.')
        root->right = makeNode(right);
}

void preOrder(TreeNode *root) 
{
    if(root)
    {
        printf("%c",root->key);
        preOrder(root->left);
        preOrder(root->right);
    }

}

void inOrder(TreeNode *root)
{
    if(root)
    {
        inOrder(root->left);
        printf("%c",root->key);
        inOrder(root->right);
    }
}

void postOrder(TreeNode *root)
{
    if(root)
    {
        postOrder(root->left);
        postOrder(root->right);
        printf("%c",root->key);
    }
}

int main()
{
    int n;
    TreeNode *root = makeNode(NULL);
    TreeNode * tmp;
    char key, left, right;

    scanf("%d",&n);
    getchar();
    for(int i= 0; i<n; i++)
    {
        scanf("%c %c %c",&key,&left,&right);
        getchar();
        tmp = findNode(root,key);
        if(tmp != NULL)
            insertNode(tmp,key,left,right);
        else
            insertNode(root,key,left,right);

    }
    preOrder(root);
    printf("\n");
    inOrder(root);
    printf("\n");
    postOrder(root);

    return 0;
}