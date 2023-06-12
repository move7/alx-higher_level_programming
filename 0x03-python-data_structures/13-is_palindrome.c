#include "lists.h"
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return(1);
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;
	listint_t *head_dup = *head;

	while(fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	while(slow->next)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	while(prev && head_dup)
	{
		if (prev->n != head_dup->n)
			return(0);
		prev = prev->next;
		head_dup = head_dup->next;
	}
	return(1);
	
}
