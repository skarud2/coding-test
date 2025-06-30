#include <stdio.h>


int main(void)
{
	long long n;
	scanf("%d", &n);

	//n이 5일때
	//i=1 => j=2,3,4,5
	//i=2 => j=3,4,5
	//i=3 => j=4,5
	//i=4 => j=5

	printf("%lld\n",  n * (n - 1) / 2);
	printf("2");
	return 0;
}