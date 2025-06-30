//20240530
#include <stdio.h>

int main(void) {

	//입력 받은 숫자만큼 파일명 입력 받기
    //    파일 이름은 모두 동일, 50자 미만
	//한글자씩 비교
	//    서로 다르면 다른 위치에 ? 출력

	int num;
	scanf("%d", &num);

	char s[50] = {};
	char tmp[50] = {};

	scanf("%s", s);

	for (int i = 1; i < num; i++) {
		scanf("%s", tmp);

		for (int j = 0; j < sizeof(s); j++) {
			if (s[j] != tmp[j]) {
				s[j] = '?';
			}
		}
	}


	printf("%s", s);
	
	return 0;
}