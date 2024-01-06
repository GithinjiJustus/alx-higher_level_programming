#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * struct listint_s -  a singly linked list
 * @n: an integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for the Holberton Schoool project
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

void reverse_listint(listint_t **head);
void free_listint(listint_t *head);
listint_t *add_nodeint_end(listint_t **head, const int n);
size_t print_listint(const listint_t *h);
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
