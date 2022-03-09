#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * main - check the code
 *
 * Return: Always EXIT_SUCCESS.
 */

int infinite_while(void);

int main(void)
{
	int i = 0;
	pid_t child_pid;

	while (i < 5)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else
		{
			exit(0);
		}
		i++;
	}

	infinite_while();
	return (0);
}


/**
 * infinite_while- function that stops the execution
 * of a group of zombie processes
 * Return: Always 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
