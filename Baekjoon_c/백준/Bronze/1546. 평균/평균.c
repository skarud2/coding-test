#include <stdio.h>
#include <stdlib.h>

int main(void) {

	//1.과목 개수 n 입력받기
	int n;
	scanf("%d", &n);

	//2.과목 개수만큼 성적 입력 받기 
	float* arr = (float*)malloc(sizeof(float)*n);
	float score;

	for (int i = 0; i < n; i++) {
		scanf("%f", &score);
		//2-1.배열에 저장 
		arr[i] = score;
	}

	//3.새로운 성적 계산
	//3-1.최대값 max 찾기
	float max=0;
	for (int i = 0; i < n; i++) {
		if (arr[i] > max)
			max = arr[i];
	}
	//3-2.새로운 성적 배열에 저장
	float newScore;
	for (int i = 0; i < n; i++) {
		newScore = arr[i] / max * 100;
		arr[i] = newScore;
	}
	//4.새로운 평균 계산 후 출력
	float plusScore = 0;
	for (int i = 0; i < n; i++) {
		plusScore += arr[i];
	}

	printf("%f", (float)plusScore / n);

	free(arr);
	return 0;
}