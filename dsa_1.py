import streamlit as st

def get_program_code(number):
    solutions = {
        1: """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#define SIZE 20

// Stack structure
struct stack {
    int top;
    char data[SIZE];
};

typedef struct stack STACK;

// Push function
void push(STACK *s, char item) {
    s->data[++(s->top)] = item;
}

// Pop function
char pop(STACK *s) {
    return s->data[(s->top)--];
}

// Function to determine the precedence of operators
int precedence(char symbol) {
    switch (symbol) {
        case '^': return 3;
        case '*':
        case '/': return 2;
        case '+':
        case '-': return 1;
        default: return 0;
    }
}

// Function to convert infix to postfix
void infixToPostfix(STACK *s, char infix[SIZE]) {
    int i, j = 0;
    char postfix[SIZE], temp, symbol;

    for (i = 0; infix[i] != '\0'; i++) {
        symbol = infix[i];

        if (isalnum(symbol)) { // If the symbol is an operand
            postfix[j++] = symbol;
        } else { // If the symbol is an operator or parenthesis
            switch (symbol) {
                case '(':
                    push(s, symbol);
                    break;
                case ')':
                    temp = pop(s);
                    while (temp != '(') {
                        postfix[j++] = temp;
                        temp = pop(s);
                    }
                    break;
                case '+':
                case '-':
                case '*':
                case '/':
                case '^':
                    while (s->top != -1 && precedence(s->data[s->top]) >= precedence(symbol)) {
                        postfix[j++] = pop(s);
                    }
                    push(s, symbol);
                    break;
                default:
                    printf("\nInvalid character in expression.\n");
                    exit(1);
            }
        }
    }

    // Pop remaining operators from the stack
    while (s->top != -1) {
        postfix[j++] = pop(s);
    }
    postfix[j] = '\0';

    printf("\nPostfix expression: %s\n", postfix);
}

int main() {
    STACK s;
    s.top = -1;
    char infix[SIZE];

    printf("Enter infix expression: ");
    scanf("%s", infix);

    infixToPostfix(&s, infix);
    return 0;
}
""",
        2: """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <string.h>
#define SIZE 20

// Stack structure
struct stack {
    int top;
    float data[SIZE];
};

typedef struct stack STACK;

// Push function
void push(STACK *s, float item) {
    s->data[++(s->top)] = item;
}

// Pop function
float pop(STACK *s) {
    return s->data[(s->top)--];
}

// Function to perform an operation
float operate(float op1, float op2, char symbol) {
    switch (symbol) {
        case '+': return op1 + op2;
        case '-': return op1 - op2;
        case '*': return op1 * op2;
        case '/': return op1 / op2;
        case '^': return pow(op1, op2);
        default:
            printf("\nInvalid operator!\n");
            exit(1);
    }
}

// Function to evaluate a prefix expression
float evaluatePrefix(STACK *s, char prefix[SIZE]) {
    int i;
    char symbol;
    float res, op1, op2;

    // Start evaluating from the end of the prefix expression
    for (i = strlen(prefix) - 1; i >= 0; i--) {
        symbol = prefix[i];

        if (isdigit(symbol)) { // If the symbol is an operand
            push(s, symbol - '0'); // Convert char to int
        } else { // If the symbol is an operator
            op1 = pop(s);
            op2 = pop(s);
            res = operate(op1, op2, symbol);
            push(s, res);
        }
    }
    return pop(s); // Final result
}

int main() {
    char prefix[SIZE];
    STACK s;
    float result;

    s.top = -1;

    printf("Enter prefix expression: ");
    scanf("%s", prefix);

    result = evaluatePrefix(&s, prefix);
    printf("The result of the prefix expression is: %.2f\n", result);

    return 0;
}""",
        3: """ #include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 5

// Queue structure
struct queue {
    int front, rear;
    char data[SIZE][20]; // Array to store messages
};

typedef struct queue QUEUE;

// Function to send a message (enqueue)
void send(QUEUE *q, char item[20]) {
    if (q->front == (q->rear + 1) % SIZE) {
        printf("\nQueue is full. Cannot send the message.\n");
    } else {
        q->rear = (q->rear + 1) % SIZE;
        strcpy(q->data[q->rear], item);
        if (q->front == -1) {
            q->front = 0;
        }
        printf("\nMessage sent: %s\n", item);
    }
}

// Function to receive a message (dequeue)
char *receive(QUEUE *q) {
    char *message;

    if (q->front == -1) {
        printf("\nQueue is empty. No messages to receive.\n");
        return NULL;
    } else {
        message = q->data[q->front];
        if (q->front == q->rear) { // If only one element is present
            q->front = -1;
            q->rear = -1;
        } else {
            q->front = (q->front + 1) % SIZE;
        }
        return message;
    }
}

// Function to display the messages in the queue
void display(QUEUE q) {
    int i;

    if (q.front == -1) {
        printf("\nQueue is empty.\n");
    } else {
        printf("\nMessages in the queue:\n");
        for (i = q.front; i != q.rear; i = (i + 1) % SIZE) {
            printf("%s\n", q.data[i]);
        }
        printf("%s\n", q.data[i]); // Print the last element
    }
}

int main() {
    int choice;
    char message[20];
    char *receivedMessage;
    QUEUE q;
    q.front = -1;
    q.rear = -1;

    while (1) {
        printf("\n1. Send Message\n2. Receive Message\n3. Display Messages\n4. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);
        getchar(); // To consume the newline character after choice input

        switch (choice) {
            case 1:
                printf("Enter the message to send: ");
                fgets(message, sizeof(message), stdin);
                message[strcspn(message, "\n")] = 0; // Remove the newline character
                send(&q, message);
                break;
            case 2:
                receivedMessage = receive(&q);
                if (receivedMessage != NULL) {
                    printf("\nMessage received: %s\n", receivedMessage);
                }
                break;
            case 3:
                display(q);
                break;
            case 4:
                exit(0);
            default:
                printf("\nInvalid choice. Try again.\n");
        }
    }

    return 0;
}
""",
        4: """  #include <stdio.h>
#include <stdlib.h>

// Node structure for polynomial
struct node {
    int coeff;   // Coefficient
    int power;   // Power of the variable
    struct node *next;
};

typedef struct node *NODE;

// Function to insert a term at the end
NODE insertEnd(NODE start, int coeff, int power) {
    NODE temp, cur;
    temp = (NODE)malloc(sizeof(struct node));
    temp->coeff = coeff;
    temp->power = power;
    temp->next = NULL;

    if (start == NULL) {
        return temp;
    }

    cur = start;
    while (cur->next != NULL) {
        cur = cur->next;
    }
    cur->next = temp;
    return start;
}

// Function to display the polynomial
void display(NODE start) {
    if (start == NULL) {
        printf("Polynomial is empty\n");
        return;
    }

    NODE temp = start;
    while (temp != NULL) {
        if (temp->coeff > 0 && temp != start)
            printf("+");
        printf("%dx^%d ", temp->coeff, temp->power);
        temp = temp->next;
    }
    printf("\n");
}

// Function to add a term to the resultant polynomial
NODE addTerm(NODE result, int coeff, int power) {
    NODE temp, cur;
    temp = (NODE)malloc(sizeof(struct node));
    temp->coeff = coeff;
    temp->power = power;
    temp->next = NULL;

    // If the term already exists, add the coefficients
    cur = result;
    while (cur != NULL) {
        if (cur->power == power) {
            cur->coeff += coeff;
            free(temp);
            return result;
        }
        cur = cur->next;
    }

    // If the term doesn't exist, insert it at the end
    return insertEnd(result, coeff, power);
}

// Function to multiply two polynomials
NODE multiplyPolynomials(NODE poly1, NODE poly2) {
    NODE result = NULL, p1, p2;

    for (p1 = poly1; p1 != NULL; p1 = p1->next) {
        for (p2 = poly2; p2 != NULL; p2 = p2->next) {
            result = addTerm(result, p1->coeff * p2->coeff, p1->power + p2->power);
        }
    }

    return result;
}

int main() {
    NODE poly1 = NULL, poly2 = NULL, result = NULL;
    int n1, n2, coeff, power;

    printf("Enter the number of terms for the first polynomial: ");
    scanf("%d", &n1);

    printf("Enter the coefficients and powers of the terms for the first polynomial:\n");
    for (int i = 0; i < n1; i++) {
        printf("Term %d: ", i + 1);
        scanf("%d %d", &coeff, &power);
        poly1 = insertEnd(poly1, coeff, power);
    }

    printf("Enter the number of terms for the second polynomial: ");
    scanf("%d", &n2);

    printf("Enter the coefficients and powers of the terms for the second polynomial:\n");
    for (int i = 0; i < n2; i++) {
        printf("Term %d: ", i + 1);
        scanf("%d %d", &coeff, &power);
        poly2 = insertEnd(poly2, coeff, power);
    }

    printf("First Polynomial: ");
    display(poly1);

    printf("Second Polynomial: ");
    display(poly2);

    result = multiplyPolynomials(poly1, poly2);

    printf("Resultant Polynomial after Multiplication: ");
    display(result);

    return 0;
}
 """,
        5: """ #include <stdio.h>
#include <stdlib.h>

#define SIZE 5

int count = 0;

// Node structure for circular linked list
struct node {
    int data;
    struct node *next;
};

typedef struct node *NODE;

// Function to insert an element at the end (enqueue)
NODE insertEnd(NODE last, int item) {
    if (count >= SIZE) {
        printf("\nQueue is full\n");
        return last;
    }

    NODE temp = (NODE)malloc(sizeof(struct node));
    temp->data = item;

    if (last == NULL) {
        temp->next = temp; // Circular link
        count++;
        return temp;
    }

    temp->next = last->next; // New node points to the first node
    last->next = temp;       // Last node points to the new node
    count++;
    return temp;             // Return new last node
}

// Function to delete an element from the beginning (dequeue)
NODE deleteBegin(NODE last) {
    if (last == NULL) {
        printf("\nQueue is empty\n");
        return NULL;
    }

    NODE temp = last->next;

    if (last == temp) { // Only one element in the queue
        printf("\nElement deleted: %d\n", temp->data);
        free(temp);
        count--;
        return NULL;
    }

    last->next = temp->next; // Last node points to the next of the first node
    printf("\nElement deleted: %d\n", temp->data);
    free(temp);
    count--;
    return last;
}

// Function to display the queue
void display(NODE last) {
    if (last == NULL) {
        printf("\nQueue is empty\n");
        return;
    }

    NODE temp = last->next; // Start from the first node
    printf("\nQueue contents:\n");
    do {
        printf("%d ", temp->data);
        temp = temp->next;
    } while (temp != last->next); // Loop until we reach the first node again
    printf("\n");
}

int main() {
    NODE last = NULL;
    int choice, item;

    while (1) {
        printf("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter the element to enqueue: ");
                scanf("%d", &item);
                last = insertEnd(last, item);
                break;

            case 2:
                last = deleteBegin(last);
                break;

            case 3:
                display(last);
                break;

            case 4:
                exit(0);

            default:
                printf("\nInvalid choice. Try again.\n");
        }
    }

    return 0;
}""",
        6: """  #include <stdio.h>
#include <stdlib.h>
#define SIZE 10

struct hashTable {
    int data[SIZE];
    int flag[SIZE]; // 0 for empty, 1 for occupied
};

typedef struct hashTable HASH;

void initTable(HASH *table) {
    for (int i = 0; i < SIZE; i++) {
        table->data[i] = -1;
        table->flag[i] = 0;
    }
}

int hash(int key) {
    return key % SIZE;
}

void insert(HASH *table, int key) {
    int index = hash(key);
    int originalIndex = index;
    while (table->flag[index] == 1) {
        index = (index + 1) % SIZE;
        if (index == originalIndex) {
            printf("\nHash table is full\n");
            return;
        }
    }
    table->data[index] = key;
    table->flag[index] = 1;
    printf("\n%d inserted at index %d\n", key, index);
}

void search(HASH *table, int key) {
    int index = hash(key);
    int originalIndex = index;
    while (table->flag[index] != 0) {
        if (table->data[index] == key) {
            printf("\n%d found at index %d\n", key, index);
            return;
        }
        index = (index + 1) % SIZE;
        if (index == originalIndex) break;
    }
    printf("\n%d not found\n", key);
}

void deleteKey(HASH *table, int key) {
    int index = hash(key);
    int originalIndex = index;
    while (table->flag[index] != 0) {
        if (table->data[index] == key) {
            table->data[index] = -1;
            table->flag[index] = 0;
            printf("\n%d deleted from index %d\n", key, index);
            return;
        }
        index = (index + 1) % SIZE;
        if (index == originalIndex) break;
    }
    printf("\n%d not found to delete\n", key);
}

void display(HASH *table) {
    printf("\nHash Table:\n");
    for (int i = 0; i < SIZE; i++) {
        if (table->flag[i] == 1)
            printf("Index %d: %d\n", i, table->data[i]);
        else
            printf("Index %d: Empty\n", i);
    }
}

int main() {
    HASH table;
    initTable(&table);
    int choice, key;

    while (1) {
        printf("\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit\nEnter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter key to insert: ");
                scanf("%d", &key);
                insert(&table, key);
                break;
            case 2:
                printf("Enter key to search: ");
                scanf("%d", &key);
                search(&table, key);
                break;
            case 3:
                printf("Enter key to delete: ");
                scanf("%d", &key);
                deleteKey(&table, key);
                break;
            case 4:
                display(&table);
                break;
            case 5:
                exit(0);
            default:
                printf("\nInvalid choice\n");
        }
    }

    return 0;
}""",
        7: """  #include <stdio.h>
#include <stdlib.h>

#define MAX 10

// Function to heapify a subtree with the root at given index
void heapify(int arr[], int n, int i) {
    int largest = i; // Initialize largest as root
    int left = 2 * i + 1; // Left child
    int right = 2 * i + 2; // Right child

    // If left child is larger than root
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // If right child is larger than largest so far
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // If largest is not root
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;

        // Recursively heapify the affected subtree
        heapify(arr, n, largest);
    }
}

// Function to build a max heap
void buildHeap(int arr[], int n) {
    // Start from the last non-leaf node and heapify each node
    for (int i = (n / 2) - 1; i >= 0; i--)
        heapify(arr, n, i);
}

// Function to extract the maximum element
int extractMax(int arr[], int *n) {
    if (*n == 0) {
        printf("\nHeap is empty\n");
        return -1;
    }

    // Get the maximum element
    int max = arr[0];

    // Replace the root with the last element
    arr[0] = arr[*n - 1];
    (*n)--;

    // Heapify the root
    heapify(arr, *n, 0);

    return max;
}

// Function to display the heap
void displayHeap(int arr[], int n) {
    if (n == 0) {
        printf("\nHeap is empty\n");
        return;
    }

    printf("\nHeap elements:\n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int heap[MAX], n = 0, choice, element;

    while (1) {
        printf("\n1. Insert\n2. Extract Max\n3. Display Heap\n4. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                if (n == MAX) {
                    printf("\nHeap is full\n");
                } else {
                    printf("Enter element to insert: ");
                    scanf("%d", &element);
                    heap[n] = element;
                    n++;
                    buildHeap(heap, n);
                }
                break;

            case 2:
                element = extractMax(heap, &n);
                if (element != -1)
                    printf("\nExtracted max element: %d\n", element);
                break;

            case 3:
                displayHeap(heap, n);
                break;

            case 4:
                exit(0);

            default:
                printf("\nInvalid choice. Try again.\n");
        }
    }

    return 0;
}
""",
        8: """  
#include <stdio.h> 
#include <stdlib.h> 
#include<ctype.h> 
struct node 
{ 
    char data; 
    struct node *left; 
    struct node *right; 
}; 
typedef struct node *NODE; 
 
struct stack 
{ 
    int top; 
    NODE data[10]; 
}; 
typedef struct stack STACK; 
 
void push(STACK *s,NODE item) 
{ 
    s->data[++(s->top)]=item; 
} 
 
NODE pop(STACK *s) 
{ 
    return s->data[(s->top)--]; 
} 
 
int preced(char symbol) 
{ 
  switch(symbol) 
  { 
      case '$':return 5; 
      case '*': 
      case '/':return 3; 
      case '+': 
      case '-':return 1; 
  } 
} 
 
NODE createnode(char item) 
{ 
    NODE temp; 
    temp=(NODE)malloc(sizeof(struct node)); 
    temp->data=item; 
    temp->left=NULL; 
    temp->right=NULL; 
    return temp; 
} 
 
void preorder(NODE root) 
{ 
    if(root!=NULL) 
    { 
        printf("%c",root->data); 
        preorder(root->left); 
        preorder(root->right); 
    } 
} 
 
void inorder(NODE root) 
{ 
    if(root!=NULL) 
    { 
        inorder(root->left); 
        printf("%c",root->data); 
        inorder(root->right); 
    } 
} 
 
void postorder(NODE root) 
{ 
    if(root!=NULL) 
    { 
        postorder(root->left); 
        postorder(root->right); 
        printf("%c",root->data); 
    } 
} 
 
NODE create_expr_tree(NODE root,char infix[10]) 
{ 
    STACK TS,OS; 
    TS.top=-1; 
    OS.top=-1; 
    int i; 
    char symbol; 
    NODE temp,t; 
    for(i=0;infix[i]!='\0';i++) 
    { 
        symbol=infix[i]; 
        temp=createnode(symbol); 
        if(isalnum(symbol)) 
            push(&TS,temp); 
        else 
        { 
            if(OS.top==-1) 
                push(&OS,temp); 
            else 
            { 
                while(OS.top!=-1 && preced(OS.data[OS.top]->data)>= 
preced(symbol)) 
                { 
                    t=pop(&OS); 
                    t->right=pop(&TS); 
                    t->left=pop(&TS); 
                    push(&TS,t); 
                } 
                push(&OS,temp); 
            } 
        } 
 
    } 
    while(OS.top!=-1) 
    { 
         t=pop(&OS); 
         t->right=pop(&TS); 
         t->left=pop(&TS); 
         push(&TS,t); 
    } 
    return pop(&TS); 
} 
int main() 
{ 
    char infix[10]; 
    NODE root=NULL; 
    printf("\n Read the infix expression :"); 
    scanf("%s",infix); 
    root=create_expr_tree(root,infix); 
    printf("\n The preorder traversal is\n"); 
    preorder(root); 
    printf("\n The inorder traversal is\n"); 
    inorder(root); 
    printf("\n The postorder traversal is\n"); 
    postorder(root); 
    return 0; 
} """,
        9: """  
#include <stdio.h> 
#include <stdlib.h> 
 
struct node 
{ 
    int data; 
    struct node *left; 
    struct node *right; 
}; 
typedef struct node *NODE; 
 
NODE create_node(int item) 
{ 
    NODE temp; 
    temp=(NODE)malloc(sizeof(struct node)); 
    temp->data=item; 
    temp->left=NULL; 
    temp->right=NULL; 
    return temp; 
} 
 
NODE insertleft(NODE root,int item) 
{ 
    root->left=create_node(item); 
    return root->left; 
} 
 
NODE insertright(NODE root,int item) 
{ 
    root->right=create_node(item); 
    return root->right; 
} 
 
void display(NODE root) 
{ 
    if(root!=NULL) 
    { 
        display(root->left); 
        printf("%d\t",root->data); 
        display(root->right); 
    } 
} 
 
int count_nodes(NODE root) 
{ 
   if (root == NULL) 
        return 0; 
   else 
    return (count_nodes(root->left) + count_nodes(root->right) + 1); 
} 
 
int height(NODE root) 
{ 
    int leftht,rightht; 
    if(root == NULL) 
        return -1; 
    else 
    { 
        leftht = height(root->left); 
        rightht = height(root->right); 
        if(leftht > rightht) 
         return leftht + 1; 
        else 
         return rightht + 1; 
    } 
} 
 
int leaf_nodes(NODE root) 
{ 
    if(root==NULL) 
        return 0; 
    else if(root->left == NULL && root->right == NULL) 
        return 1; 
    else 
        return leaf_nodes(root->left) + leaf_nodes(root->right); 
} 
 
int nonleaf_nodes(NODE root) 
{ 
    if(root==NULL || (root->left == NULL && root->right == NULL)) 
        return 0; 
    else 
        return nonleaf_nodes(root->left) + nonleaf_nodes(root
>right) + 1; 
} 
int main() 
{ 
    NODE root=NULL; 
    root=create_node(45); 
    insertleft(root,39); 
    insertright(root,78); 
    insertleft(root->right,54); 
    insertright(root->right,79); 
    insertright(root->right->left,55); 
    insertright(root->right->right,80); 
    printf("\n The tree(inorder) is\n"); 
    display(root); 
    printf("\n"); 
    printf("\n The total number of nodes is 
%d\n",count_nodes(root)); 
    printf("\n The height of the tree is %d\n",height(root)); 
    printf("\n The total number of leaf nodes is 
%d\n",leaf_nodes(root)); 
    printf("\n The total number of non-leaf nodes is 
%d\n",nonleaf_nodes(root)); 
    return 0; 
} """,
        10: """  
#include <stdio.h> 
#include <stdlib.h> 
struct node 
{ 
    int data; 
    struct node *left; 
    struct node *right; 
}; 
typedef struct node *NODE; 
 
NODE create_node(int item) 
{ 
    NODE temp; 
    temp=(NODE)malloc(sizeof(struct node)); 
    temp->data=item; 
    temp->left=NULL; 
    temp->right=NULL; 
    return temp; 
} 
 
NODE Insertbst(NODE root,int item) 
{ 
    NODE temp; 
    temp=create_node(item); 
    if(root==NULL) 
        return temp; 
    else 
    { 
       if(item < root->data) 
            root->left=Insertbst(root->left,item); 
        else 
            root->right=Insertbst(root->right,item); 
    } 
    return root; 
 
} 
 
void preorder(NODE root) 
{ 
    if(root!=NULL) 
    { 
        printf("%d\t",root->data); 
        preorder(root->left); 
        preorder(root->right); 
    } 
} 
 
void inorder(NODE root) 
{ 
    if(root!=NULL) 
    { 
        inorder(root->left); 
        printf("%d\t",root->data); 
        inorder(root->right); 
    } 
} 
 
void postorder(NODE root) 
{ 
    if(root!=NULL) 
    { 
        postorder(root->left); 
        postorder(root->right); 
        printf("%d\t",root->data); 
    } 
} 
 
NODE inordersuccessor(NODE root) 
{ 
    NODE cur=root; 
    while(cur->left != NULL) 
        cur = cur->left; 
    return cur; 
} 
 
NODE deletenode(NODE root,int key) 
{ 
    NODE temp; 
    if(root == NULL) 
        return NULL; 
    if(key<root->data) 
        root->left = deletenode(root->left,key); 
    else if(key > root->data) 
        root->right = deletenode(root->right,key); 
    else 
    { 
        if(root->left == NULL) 
        { 
            temp=root->right; 
            free(root); 
            return temp; 
        } 
        if(root->right == NULL) 
        { 
            temp=root->left; 
            free(root); 
            return temp; 
        } 
        temp=inordersuccessor(root->right); 
        root->data=temp->data; 
        root->right=deletenode(root->right,temp->data); 
    } 
    return root; 
} 
int main() 
{ 
    NODE root = NULL; 
    int ch,item,key; 
    for(;;) 
    { 
        printf("\n 1. Insert"); 
        printf("\n 2. Preorder"); 
        printf("\n 3. Inorder"); 
        printf("\n 4. Postorder"); 
        printf("\n 5. Delete"); 
        printf("\n 6. Exit"); 
        printf("\n Read ur choice:"); 
        scanf("%d",&ch); 
        switch(ch) 
        { 
            case 1:printf("\n Read element to be inserted :"); 
                scanf("%d",&item); 
                root=Insertbst(root,item); 
                break; 
            case 2:printf("\n The Preorder traversal is\n"); 
                 preorder(root); 
                 break; 
            case 3:printf("\n The Inorder traversal is\n"); 
                 inorder(root); 
                 break; 
            case 4:printf("\n The Postorder traversal is\n"); 
                 postorder(root); 
                 break; 
            case 5:printf("\n Read node to be deleted : "); 
                  scanf("%d",&key); 
                 root=deletenode(root,key); 
                 break; 
            default :exit(0); 
        } 
    } 
    return 0; 
} """

    }
    return solutions.get(number, "Program solution not available")

st.set_page_config(page_title="DSA Lab Solutions", layout="wide")
st.title("Data Structures Lab Programs")

program_number = st.selectbox(
    "Select Program Number",
    range(1, 11),
    format_func=lambda x: f"Program {x}: {get_program_name(x)}"
)

if program_number:
    st.subheader(f"Program {program_number}: {get_program_name(program_number)}")
    
    code = get_program_code(program_number)
    
    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        st.download_button(
            label="Download Solution",
            data=code,
            file_name=f"program_{program_number}.c",
            mime="text/plain"
        )
    
    with col2:
        # Using HTML/JavaScript for clipboard functionality
        st.markdown(f"""
            <button onclick="navigator.clipboard.writeText(`{code}`);alert('Code copied!')">
                Copy Code
            </button>
            """, 
            unsafe_allow_html=True
        )
    
    with st.expander("View Solution", expanded=True):
        st.code(code, language='c')

