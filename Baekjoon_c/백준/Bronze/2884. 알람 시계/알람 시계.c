#include <stdio.h>


int main(void)
{
	int h, m;		//실제 일어나야 하는 시간
	int ah=0, am=0;		//알람 설정 시간

	//시,분 입력 받기
	scanf("%d %d", &h, &m);

	//00:00 ~ 23:59
	if (h >= 0 && h <= 23 && m >= 0 && m <= 59) {
		//45분 일찍 설정
		am = m - 45;

		if (am < 0)
		{
			ah = h - 1;
			am += 60;

			if (h == 0)
				ah = 24 - 1;
		}
		else
			ah = h;

		printf("%d %d", ah, am);
	}

	return 0;
}