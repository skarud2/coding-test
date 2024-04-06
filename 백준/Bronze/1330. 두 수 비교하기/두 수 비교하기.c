#include <stdio.h>

void compare(int a, int b)
{		
		if (a > b)
		{
			printf(">");
		}
		else if (a < b)
		{
			printf("<");
		}
		else
		{
			printf("==");
		}
}

int main(void)
{
	int a, b;
	scanf("%d %d", &a, &b);

	if (a<=10000 && a>=-10000 && b<=10000 && b>=-10000)
	{
		compare(a, b);
	}
	else
		printf("-10,000 이상 10,000 이하의 정수를 입력하시오");

	return 0;
}