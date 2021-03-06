import os
from time import sleep

# 点击(x,y)
def ClickScreen(x,y):
    os.system(f'adb shell input tap {x} {y}')

#从坐标(x1,y1)，滑动到(x2,y2)，耗时t毫秒秒
def SlipScreen(x1,y1,x2,y2,t):
    os.system(f'adb shell input swipe {x1} {y1} {x2} {y2} {t}')

def Repeat(Auto,Control):
    print('开始挑战')

    # 闯关
    ClickScreen(1780, 895)
    sleep(9)

    # 跳过
    print('点击跳过')
    ClickScreen(2143, 53)
    sleep(1)

    # 自动
    if Control == False:
        if Auto == False:
            print('点击自动')
            ClickScreen(2205, 115)
            Auto = True
            # 打完
            sleep(70)
            print('打完了')

            # 跳过
            ClickScreen(2143, 53)
            sleep(10)
    else:
        SlipScreen(441,741,297,545,7100)
        SlipScreen(1994,634,1876,478,100)
        sleep(9)
        ClickScreen(1983, 918)
        sleep(13)

        # 跳过
        print('点击跳过')
        ClickScreen(2143, 53)
        sleep(1)


        ClickScreen(2205, 115)
        ClickScreen(1780, 895)
        Auto = True


    print('挑战完成\n')
    # 点击屏幕继续
    ClickScreen(1160, 985)
    sleep(1)

    # 再次挑战
    print('再次挑战\n')
    ClickScreen(1990, 990)
    sleep(1)
    Repeat(Auto,Control)

if __name__ == '__main__':
    print('刷金币初始化......')
    Start = os.popen('adb devices')
    p = Start.read()
#    if p.find('5037'):
#        GetPID = os.popen('netstat -aon|findstr 5037')
#        PID = (GetPID.split('\n', 1)[0])[-4,-1]
#        os.system('taskkill /pid {PID} /f')
    print('初始化完成......')
    AutoCondition = input('目前游戏自动操作的状况是开启还是关闭的?\n（开启输入“T”,关闭输入“F”）：')
    if AutoCondition == 'T':
        Auto = True
    elif AutoCondition == 'F':
        Auto = False
    AutoControl = input('您是否需要脚本自动操作?\n注意：脚本刷会更快，但稳定性一般\n（开启输入“T”,关闭输入“F”）：')
    if AutoControl == 'T':
        Control = True
    elif AutoControl == 'F':
        Control = False
    ClickScreen(1655, 820)  # 万象天工
    sleep(1)
    ClickScreen(220, 285)   # 冒险玩法
    sleep(1)
    ClickScreen(1170, 490)  # 挑战
    sleep(2)
    ClickScreen(1730, 965)  # 下一步
    sleep(2)
    print('通天塔')
    print('刷金币重复阶段......')
    Repeat(Auto,Control)
