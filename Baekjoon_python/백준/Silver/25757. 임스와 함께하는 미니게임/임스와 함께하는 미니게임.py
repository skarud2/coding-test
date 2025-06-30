#20250415
import sys
input=sys.stdin.readline

#게임종류: Y(2), F(3), O(4)
#플레이를 신청한 사람 수, 게임 종류 입력
setting=list(input().split())
#플레이어 입력
#중복 제거를 위해 set, add 함수 사용
player=set()
for _ in range(int(setting[0])):
    player.add(input().rstrip())

#게임 종류에 따른 플레이어 수 설정
if setting[1]=='Y':
    playerNum=1
elif setting[1]=='F':
    playerNum=2
else:
    playerNum=3

print(len(player)//playerNum)