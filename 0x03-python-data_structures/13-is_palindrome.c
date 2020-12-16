#include "lists.h"

/**
 * linkedlist_pal - verify if a linked list can be palindrome
 * @tmp: temporal head
 * @h: head of the list
 * Return: 1 if it is a linked list, 0 if not
 */

int linkedlist_pal(listint_t **tmp, listint_t *h)
{
	if (!h)
		return (1);
	while (linkedlist_pal(tmp, h->next) == 1 && (*tmp)->n == h->n)
	{
		*tmp = (*tmp)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int p;

	if (!head || !*head || !(*head)->next)
		return (1);
	p = linkedlist_pal(head, *head);
	return (p);
