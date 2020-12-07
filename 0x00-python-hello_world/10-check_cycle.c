#include "lists.h"
/**
 * check_cycle - hecks if a singly linked list has a cycle in it
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *list_aux = current;

	while (current && list_aux && current->next)
	{
		list_aux = list_aux->next;
		current = current->next->next;
		if (current == list_aux)
			return (1);
	}
	return (0);
}

