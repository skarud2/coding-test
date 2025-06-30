#include <stdlib.h>
#include <stdio.h>

int main(void)
{
	//바구니 개수 n개, 공 바꾸기 m번
	int n, m;
	scanf("%d %d", &n, &m);



	//처음 바구니 배열 생성
	int* arr = (int*)malloc(sizeof(int) * n);

	for (int a = 0; a < n; a++)
	{
		arr[a] = a + 1;		
	}

	//인덱스 i,j 번째 배열값 m번 교환
	int i, j;
	int tmp;
	for (int a = 0; a < m; a++)
	{
		scanf("%d %d", &i, &j);	//교환할 바구니 번호 입력받기

		//바구니 번호는 1번부터 시작
		//배열의 인덱스는 0번부터 시작
		tmp = arr[i-1];			
		arr[i-1] = arr[j-1];
		arr[j-1] = tmp;
	}

	
	//배열 출력
	for (int a = 0; a < n; a++)
	{
		printf("%d ", arr[a]);
	}
	
	return 0;
}