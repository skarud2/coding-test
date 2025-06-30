#include <stdio.h>
#include <stdlib.h>


int main(void) {
	//1. 카드 개수 n, 최대 합 m 입력
	int n, m;
	scanf("%d %d", &n, &m);
	

	//2. 카드 담을 배열 생성
	int num;
	int arr[100];

	for (int i = 0; i < n; i++) {
		scanf("%d", &num);
		arr[i] = num;
	}

	//3. 합이 m을 넘지 않으면서 최대한 가까운 카드 3장 출력
	//	3-1. 숫자 3개 합 구하기 => sum
	//		3-1-1. 지난 합보다 크면 sum값 업데이트
	int sum = 0;
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			for (int k = j + 1; k < n; k++) {
				if ((m>= arr[i] + arr[j] + arr[k])&&(sum < arr[i] + arr[j] + arr[k]))
					sum = arr[i] + arr[j] + arr[k];
			}
		}
	}
	printf("%d", sum);

	return 0;
}