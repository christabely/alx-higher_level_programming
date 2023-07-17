#include "lists.h"
/**
 * reverse - reverses a linked list
 * @hhd: pointer
 * Return: pointer to 1st node
 */

void reverse(listint_t **hhd)
{
	listint_t *prev, *curr, *nxt;

	prev = NULL;
	curr = *hhd;

	while (curr != NULL)
	{
		nxt = curr->next;
		curr->next = prev;
		prev = curr;
		curr = nxt;
	}

	*hhd = prev;
}

/**
 * compare - compares each int of list
 * @hd1: head of the 1st half
 * @hd2: head of the 2nd half
 * Return: 1 if equals,otherwise 0
 */
int compare(listint_t *hd1, listint_t *hd2)
{
	listint_t *temp1;
	listint_t *temp2;

	temp1 = hd1;
	temp2 = hd2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (temp1 == NULL && temp2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks for palindrome
 * @head: pointer to head of list
 * Return: 0 if not a palindrome, else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *secHalf, *middle;
	int isPal;

	slow = fast = prev_slow = *head;
	middle = NULL;
	isPal = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		secHalf = slow;
		prev_slow->next = NULL;
		reverse(&secHalf);
		isPal = compare(*head, secHalf);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = secHalf;
		}
		else
		{
			prev_slow->next = secHalf;
		}
	}
	return (isPal);
}
