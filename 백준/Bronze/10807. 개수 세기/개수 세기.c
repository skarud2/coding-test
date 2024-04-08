#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	//배열의 크기 입력 받기
	int n;
	scanf("%d", &n);

	//n 범위 제한
	if (n < 1 || n>100)
	{
		printf("1보다 크거나 같고 100보다 작거나 같은 정수 입력 \n");
		scanf("%d", &n);
	}

	//배열 생성
	int* arr = (int*)malloc(sizeof(int) * n);
    
	for (int i = 0; i < n; i++)
	{
		int num;
		scanf("%d", &num);
		arr[i] = num;

		//num 범위 제한
		if (num < -100 || num>100)
		{
			printf("-100보다 크거나 같고 100보다 작거나 같은 정수 입력 \n");
			i--;
		}

	}

	//구하려는 정수 v 입력
	int v;
	scanf("%d", &v);

	//v 범위 제한
	if (v < -100 || v>100)
	{
		printf("-100보다 크거나 같고 100보다 작거나 같은 정수 입력 \n");
		scanf("%d", &v);
	}

	//v 찾기
	int count = 0;	//v 개수 세기

	for (int i = 0; i < n; i++)
	{
		if (arr[i] == v)
			count++;
	}

	//v 개수 출력
	printf("%d", count);

	return 0;
}