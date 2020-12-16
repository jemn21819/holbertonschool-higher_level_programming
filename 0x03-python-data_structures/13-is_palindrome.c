#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *current;
	size_t size, i, flag = 1;
	int *pal_arr;

	if (*head == NULL)
		return (1);
	current = *head;
	for (size = 0; current; size++)
		current = current->next;
	pal_arr = malloc(sizeof(int) * size);
	if (!pal_arr)
		return (1);
	current = *head;
	for (i = 0; i < size; i++)
	{
		pal_arr[i] = current->n;
		current = current->next;
	}
	for (i = 0; i < size; i++, size--)
	{
		if (pal_arr[i] != pal_arr[size - 1])
			flag = 0;
	}
	free(pal_arr);
	if (flag == 0)
		return (0);
	return (1);
}
