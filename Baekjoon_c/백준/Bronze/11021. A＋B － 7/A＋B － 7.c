#include <stdio.h>
#include <stdlib.h>

int main(void)
{

	//테스트 케이스 개수 받기
	int t;
	scanf("%d", &t);

	//배열 크기 동적할당
	int* result = (int*)malloc(sizeof(int)*t);

	//변수 초기화
	int a, b;

	for (int i = 0; i < t; i++)
	{
		//두 정수 입력 받기
		scanf("%d %d", &a, &b);

		//a,b 범위 설정
		if (a >= 10 || a <= 0 || b >= 10 || b <= 0)
		{
			printf("0보다 크고 10보다 작은 정수를 입력하세요.\n");
			i--;
		} else
			result[i] = a + b ;		//a+b 결과 배열에 담기

	}

	//출력
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i + 1);
		printf("%d\n", result[i]);
	}
	

	free(result);
	return 0;
}