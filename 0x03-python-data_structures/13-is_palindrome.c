#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;
	listint_t *head_dup = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	slow = slow->next;
	if (fast->next)
		slow = slow->next;
	while (slow->next)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	while (prev && head_dup)
	{
		if (prev->n != head_dup->n)
			return (0);
		prev = prev->next;
		head_dup = head_dup->next;
	}
	return (1);
}
