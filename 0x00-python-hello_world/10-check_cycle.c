#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - a function that checks if a singly linked list has a cycle in it.
 * @list: a linked list that we will work with
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
                fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
