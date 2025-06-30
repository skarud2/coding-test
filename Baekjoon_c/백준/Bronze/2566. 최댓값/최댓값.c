#include <stdio.h>

int main(void) {
	//1. 9*9 행렬 입력받기
	int arr[9][9] = {};
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			scanf("%d", &arr[i][j]);
		}
	}
	//2. 최대값 찾기
	int max=-1;	//최대값
	int row;	//행
	int column;		//열

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++)
		{
			if (arr[i][j] > max){
				max = arr[i][j];
				row = i+1;
				column = j+1;
			}

		}
	}
    
    //3. 출력
	//3-1. 최대값
	printf("%d\n", max);
	//3-2. 최대값 위치
	printf("%d %d", row, column);


	return 0;
}