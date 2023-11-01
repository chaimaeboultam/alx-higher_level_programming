#include "lists.h"
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
    listint_t *current = *head;
    listint_t *new_node = malloc(sizeof(listint_t));

    if (!new_node)
        return NULL;

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL || number < current->n)
    {
        new_node->next = *head;
        *head = new_node;
        return new_node;
    }

    while (current->next && number > current->next->n)
    {
        current = current->next;
    }

    new_node->next = current->next;
    current->next = new_node;

    return new_node;
}
