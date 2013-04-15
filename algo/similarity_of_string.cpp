#include <iostream>
#include <string.h>
using namespace std;

int
getSim (char *str1, char *str2)
{
	int	n=0;

  if (str1 == NULL || str2 == NULL)
    return 0;

  while (*str1++ == *str2++)
    n++;
  return n;
}

int
main ()
{
  char *s = new char[100000];
  int N;
  cin >> N;
  for (int i = 0; i < N; i++)
    {
      int similarity = 0;
      cin >> s;
      similarity += strlen (s);
      for (int i = 1; i < strlen (s); i++)
	{
	  similarity += getSim (s, s + i);
	}
      cout << similarity << endl;
    }
}
