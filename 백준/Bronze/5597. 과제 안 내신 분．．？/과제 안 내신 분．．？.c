#include <stdlib.h>
#include <stdio.h>	

#define size 28	//과제 제출한 사람 수

//선택정렬
void selsort(int arr[], int n) {
	int maxIdx;
	int temp;

	for (int i = 0; i < n - 1; i++) {
		maxIdx = i;

		for (int j = i + 1; j < n; j++)
			if (arr[j] < arr[maxIdx])
				maxIdx = j;

		temp = arr[i];
		arr[i] = arr[maxIdx];
		arr[maxIdx] = temp;

	}
}

//이진탐색
int BSearch(int arr[], int len, int target)
{
	//인덱스 값
	int first = 0;
	int last = len - 1;
	int mid;

	while (first<=last)
	{
		mid = (first + last) / 2;

		if (target == arr[mid])
			return 0;
		else
		{
			if (target < arr[mid])
				last = mid - 1;
			else
				first = mid + 1;
		}
	}
	return -1; //탐색실패
}

int main(void)
{
	int arr[30];
	int num = 0;

	//과제 낸 사람 번호를 배열에 저장
	for (int i = 0; i < size; i++)
	{
		scanf("%d", &num);
		arr[i] = num;
	}

	//과제 낸 사람 번호 오름차순 정렬
	selsort(arr, size);

	// 1부터 30까지 이진 탐색 
	// 실패 시 타겟 값 출력
	for (int i = 1; i <= 30; i++)
	{
		int t;
		t=BSearch(arr, size, i);
		if (t==-1)
		printf("%d\n",i);
	}

	return 0;
}