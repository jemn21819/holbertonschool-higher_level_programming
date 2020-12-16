#include "lists.h"
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	int size;
	int optns[2048];
	int i;

	size = 0;
	if (!head || !*head)
		return (1);

	while(*head != NULL)
	{
		size++;
		optns[size - 1] = (*head)->n;
		head = &(*head)->next;
	}

	for (i = 0; i < size / 2; i++)
	{
		if (optns[i] != optns[size - i - 1])
			return (0);
	}

	return (1);
}
