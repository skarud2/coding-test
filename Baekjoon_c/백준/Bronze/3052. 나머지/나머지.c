#include <stdio.h>

int main() {

	int arr[42] = { 0, };
	int num;
	int count=0;

	for (int i = 0; i < 10; i++) {
		scanf("%d", &num);
		arr[num % 42] = 1;
	}

	for (int i = 0; i < 42; i++) {
		if (arr[i] == 1)
			count++;
	}

	printf("%d", count);
}
