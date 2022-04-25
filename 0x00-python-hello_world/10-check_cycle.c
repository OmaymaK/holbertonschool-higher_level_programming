#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *p;

	head = list;
	p = list->next;
	while (head != NULL && p != NULL && p->next)
	{
		if (head == p)
			return (1);
		head = head->next;
		p = p->next->next;
	}
	return (0);
}
