#include <stdio.h>
#include <stdlib.h>

int main() {

	//바구니 n개, 순서 바꾸기 m번
	int n, m;
	scanf("%d %d", &n, &m);

	int* arr = (int*)malloc(sizeof(int) * n);

	//배열에 숫자 넣기 1~n
	for (int k = 0; k < n; k++) {
		arr[k] = k + 1;
	}

	//바구니 순서 역순으로 바꾸기
	//배열의 인덱스 번호 ==  바구니 번호 -1
	//i~j -> j~i
	int i, j;	//바구니 번호
	int tmp;
	int r,l;

	for (int k = 0; k < m; k++) {
		scanf("%d %d", &i, &j);
		l = j;

		for (int q=0; q < (j - i); q++) {
			r = i - 1;
			
			for (int p = i; p < l; p++) {	//이웃한 번호 서로 바꾸기
				tmp = arr[r];
				arr[r] = arr[r+1];
				arr[r+1] = tmp;
				r++;

			}
			l--;

		}


	}
		for (int q = 0; q < n; q++) {
			printf("%d ", arr[q]);
		}

	return 0;
}