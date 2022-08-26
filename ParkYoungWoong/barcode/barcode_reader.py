import cv2
import pyzbar.pyzbar as pyzbar
from playsound import playsound

data_dic = {8801043035900:'신라면',
            8801043035901:'안성탕면',
            8801043035902:'너구리',
            8801043035903:'짜파게티',
            8801043035989:'프링글스',
            8801019312069:'포카칩',
            8801019314753:'빈츠',
            8801019610080:'맛동산',
            8801062012756:'쿠쿠다스',
            8801117139100:'눈을감자',
            8801069300276:'초코파이',
            8801121020283:'화이트하임',
            8801019411598:'홈런볼',
            8801117784508:'꼬북칩초코',
            8801117784509:'꼬북칩인절미'}


cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while True:
    success, frame = cap.read()

    if success:
        for code in pyzbar.decode(frame):
            my_code = int(code.data.decode('utf-8'))

            try:

                if my_code in list(data_dic.keys()):
                    print('인식 성공', my_code, data_dic[my_code])
                    # key = waitKey(3)
                    playsound('{}.mp3'.format(data_dic[my_code]))
                else:
                    print('인식 오류')
                    playsound('다시.mp3')
            except:
                continue
            

        cv2.imshow('cam', frame)

        key = cv2.waitKey(1)

        if key == 27:
            break

cap.release()
cv2.destroyAllWindows()