#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	int *ints, i;

	slow = *head;
	fast = *head;

	if (!*head || !(*head)->next)
		return (1);

	i = 0;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		i++;
	}
	i++;
	ints = malloc(sizeof(int) * i);
	if (!ints)
		return (0);
	i = 0;
	while (slow)
	{
		ints[i++] = slow->n;
		slow = slow->next;
	}
	i--;
	slow = *head;
	while (slow && i >= 0)
	{
		if (slow->n != ints[i])
		{
			free(ints);
			return (0);
		}
		i--;
		slow = slow->next;
	}
	free(ints);
	return (1);
}
