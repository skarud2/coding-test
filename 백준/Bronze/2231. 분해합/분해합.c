#include <stdio.h>

int main(void) {
	int n;
	scanf("%d", &n);

	int sum = 0;
	int tmp = 0;

	for (int i = 1; i < n; i++) {
		sum = i;
		tmp = i;

		while (tmp != 0) {
			sum = sum + (tmp % 10);
			tmp = tmp / 10;
		}
		if (n == sum) {
			printf("%d", i);
			break;
		}
		
	}
	if (n!=sum)
		printf("0");

	return 0;
}