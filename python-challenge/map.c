#include<stdio.h>

int map(char c)
{
	if (c - 'a' >= 0 && c - 'a' < 26)
		return 'a' + ((c - 'a' + 2) % 26);
	else
		return c;
}

int main(void)
{
	int c;
	while (scanf("%c", &c) != EOF) {
		printf("%c", map(c));
	}
	return 0;
}
