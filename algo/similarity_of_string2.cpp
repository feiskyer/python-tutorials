#include <iostream>
#include <string.h>
using namespace std;

int
getSim (char *str1, char *str2)
{
  if (*str1 == '\0' || *str2 == '\0')
    return 0;
  if (*str1 != *str2)
    return 0;
  if (*str1 == *str2)
    return 1 + getSim (str1 + 1, str2 + 1);
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
