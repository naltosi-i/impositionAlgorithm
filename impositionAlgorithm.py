import sys

n = 0

print("コピ本（中綴じ）用の面付をするプログラムです。\n原稿の頁数を半角数字で入力してください。")

while n == 0:

    try:
        n = int(input())
    except ValueError:
        print("半角数字を入力してください")
        n = 0


if n % 4 != 0:
    print("4の倍数頁の原稿を用意してください。\n4の倍数頁でない原稿は中綴じ製本できません。\nプログラムを終了します。")
    sys.exit
else:
    pages = int(n/4)

    print(str(n) + "頁の原稿を" + str(pages) + "枚の用紙に面付を行います")

    manuscriptList = []

    while manuscriptList == []:
        print("原稿は縦書きですか？横書きですか？\n縦書き=0, 横書き=1 を入力してください")

        try:
            vh = int(input())
        except ValueError:
            vh = None

        if vh == 1:
            #原稿ページリストの作成
            manuscriptList = [i+1 for i in range(n)]
        elif vh == 0:
            manuscriptList = [i+1 for i in range(n)]
            manuscriptList.reverse()
        else:
            print("0か1を半角数字で入力してください")


    # print(manuscriptList)

    impositionList = []
    side = ["L","R"]
    
    for i in range(pages):
        pageStock = []

        for k in range(2):
            for j , r in enumerate(side):
                if r == "L":
                    index = -1
                    pmSign = -1
                    pageStock.append(manuscriptList[index + pmSign * ( k + 2 * i)])       

                elif r == "R":
                    index = 0
                    pmSign = 1
                    pageStock.append(manuscriptList[index + pmSign * ( k + 2 * i)])       
            
        front = "表面", "左頁" + str(pageStock[0]), "右頁" + str(pageStock[1])
        back = "裏面", "左頁" + str(pageStock[3]), "右頁" + str(pageStock[2])

        impositionList.append((str(i+1) + "枚目", front, back))

        print(impositionList[i])

status = 1
while status > 0:
    print("終了するときは exit と入力してください")
    s = input()
    if s == "exit":
        status = 0