#include <stdio.h>


int main(void)
{
	int score = 0;
	scanf("%d", &score);

	if (score >= 0 && score <= 100)
	{
		if (score >= 90)
		{
			printf("A");
		}
		else if (score >= 80)
		{
			printf("B");
		}
		else if (score >= 70)
		{
			printf("C");
		}
		else if (score >= 60)
		{
			printf("D");
		}
		else
			printf("F");
	}
	else
		printf("0 이상 100 이하의 점수를 입력하시오");

	return 0;
}