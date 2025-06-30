#include <stdio.h>
#include <string.h>


int main(void) {
	//1. 숫자별로 담긴 알파벳 2차원 배열 생성
	char arr[][4] = { {}, {}, {'A','B','C',},{'D','E','F',},
		{'G','H','I',},{'J','K','L',},{'M','N','O',},
		{'P','Q','R','S'},{'T','U','V',},{'W','X','Y','Z'} };

	//2. 문자 입력
	char word[16] = {};
	scanf("%s", word);

	//3. 한 문자씩 찾기
	int time = 0;
	for (int k = 0; k < strlen(word); k++) {
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 4; j++) {
				if (word[k] == arr[i][j]){
;					time += (i+1);
					break;		
				}
			}
		}
	}

	//4. 출력
	printf("%d", time);

		return 0;
	}