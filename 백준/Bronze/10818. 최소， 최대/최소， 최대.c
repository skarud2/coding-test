#include <stdlib.h>
#include <stdio.h>


int main(void)
{
	// 정수 개수 n 입력
	int n;
	scanf("%d", &n);

	//동적할당 배열 생성
	int* arr = (int*)malloc(sizeof(int) * n);

	//정수 n개 입력
	int num=0;
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &num);
		arr[i] = num;
	}

	int max = arr[0];
	int min=arr[0];

	for (int i = 1; i < n; i++)
	{
		//최댓값 찾기
		if (arr[i] > max)
			max = arr[i];

		//최솟값 찾기
		if (arr[i] < min)
			min = arr[i];
	}

	printf("%d %d", min, max);

    free(arr);

	return 0;
}