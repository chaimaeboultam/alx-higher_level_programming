#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to the linked list
 * @number: The number to be inserted
 *
 * Return: Address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node = *head, *new = malloc(sizeof(listint_t));
    
    if (!new)
        return NULL;

    new->n = number;
    new->next = NULL;

    if (!node || new->n < node->n)
    {
        new->next = node;
        *head = new;
        return *head;
    }

    while (node)
    {
        if (!node->next || new->n < node->next->n)
        {
            new->next = node->next;
            node->next = new;
            return node;
        }
        node = node->next;
    }
    return NULL;
}
