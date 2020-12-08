#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: start of the list
 * @number: add to n
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *look = *head;
	listint_t *temp = NULL;

	temp = malloc(sizeof(listint_t));
	if (!temp)
		return (NULL);
	temp->n = number;
	temp->next = NULL;
	if (!head)
		return (NULL);
	if (*head == NULL)
	{
		*head = temp;
		return (temp);
	}
	if (number < look->n)
	{
		temp->next = look;
		*head = temp;
		return (temp);
	}
	while (look->next)
	{
		if (number < look->next->n)
		{
			temp->next = look->next;
			look->next = temp;
			return (temp);
		}
		look = look->next;
	}
	look->next = temp;
	return (temp);
}
