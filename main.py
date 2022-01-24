import sys
import time
import pyautogui
import win32file
import winsound as sd

from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:\\Users\\chlal\\PycharmProjects\\APPLY_WORK\\main.ui")[0]
# 해당경로에서 ui를 불러온다.


class WindowClass(QMainWindow, form_class):
    # q메인윈도우라는 걸 상속받는 윈도우클래스...폼클래스를 전달할 것임.

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 연속인식버튼들 연결모음
        self.Auto_location_A.clicked.connect(self.openLocation_A)
        self.Auto_location_B.clicked.connect(self.openLocation_B)
        self.Auto_location_C.clicked.connect(self.openLocation_C)
        self.Auto_location_D.clicked.connect(self.openLocation_D)
        self.Auto_location_E.clicked.connect(self.openLocation_E)
        self.Auto_location_F.clicked.connect(self.openLocation_F)

        # 오른쪽버튼들 연결모음
        self.nogadaBtn.clicked.connect(self.getLocation)
        self.TEST_START_2.clicked.connect(self.test2_for_click)
        self.SAVE.clicked.connect(self.saveText)

        # 파일에서 텍스트 불러와서 덮기 파트
        TOPEN = open("locations.txt", 'r')
        TextLines = TOPEN.readlines()
        self.X_A1.setText(TextLines[0].strip());        self.Y_A1.setText(TextLines[1].strip())
        self.X_A2.setText(TextLines[2].strip());        self.Y_A2.setText(TextLines[3].strip())
        self.X_A3.setText(TextLines[4].strip());        self.Y_A3.setText(TextLines[5].strip())
        self.X_A4.setText(TextLines[6].strip());        self.Y_A4.setText(TextLines[7].strip())
        self.X_B1.setText(TextLines[8].strip());        self.Y_B1.setText(TextLines[9].strip())
        self.X_B2.setText(TextLines[10].strip());        self.Y_B2.setText(TextLines[11].strip())
        self.X_B3.setText(TextLines[12].strip());        self.Y_B3.setText(TextLines[13].strip())
        self.X_B4.setText(TextLines[14].strip());        self.Y_B4.setText(TextLines[15].strip())
        self.X_C1.setText(TextLines[16].strip());        self.Y_C1.setText(TextLines[17].strip())
        self.X_C2.setText(TextLines[18].strip());        self.Y_C2.setText(TextLines[19].strip())
        self.X_C3.setText(TextLines[20].strip());        self.Y_C3.setText(TextLines[21].strip())
        self.X_C4.setText(TextLines[22].strip());        self.Y_C4.setText(TextLines[23].strip())
        self.X_D1.setText(TextLines[24].strip());        self.Y_D1.setText(TextLines[25].strip())
        self.X_D2.setText(TextLines[26].strip());        self.Y_D2.setText(TextLines[27].strip())
        self.X_D3.setText(TextLines[28].strip());        self.Y_D3.setText(TextLines[29].strip())
        self.X_D4.setText(TextLines[30].strip());        self.Y_D4.setText(TextLines[31].strip())
        self.X_E1.setText(TextLines[32].strip());        self.Y_E1.setText(TextLines[33].strip())
        self.X_E2.setText(TextLines[34].strip());        self.Y_E2.setText(TextLines[35].strip())
        self.X_E3.setText(TextLines[36].strip());        self.Y_E3.setText(TextLines[37].strip())
        self.X_F1.setText(TextLines[38].strip());        self.Y_F1.setText(TextLines[39].strip())
        self.X_F2.setText(TextLines[40].strip());        self.Y_F2.setText(TextLines[41].strip())
        self.X_F3.setText(TextLines[42].strip());        self.Y_F3.setText(TextLines[43].strip())
        self.X_F4.setText(TextLines[44].strip());        self.Y_F4.setText(TextLines[45].strip())
        self.X_F5.setText(TextLines[46].strip());        self.Y_F5.setText(TextLines[47].strip())



    ########################
    ### 연속인식 함수들 정의 ###
    ########################

    def openLocation_A(self):
        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_A1.setText(str(mouseX))
        self.Y_A1.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_A2.setText(str(mouseX))
        self.Y_A2.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_A3.setText(str(mouseX))
        self.Y_A3.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_A4.setText(str(mouseX))
        self.Y_A4.setText(str(mouseY))

    def openLocation_B(self):
        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_B1.setText(str(mouseX))
        self.Y_B1.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_B2.setText(str(mouseX))
        self.Y_B2.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_B3.setText(str(mouseX))
        self.Y_B3.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_B4.setText(str(mouseX))
        self.Y_B4.setText(str(mouseY))

    def openLocation_C(self):
        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_C1.setText(str(mouseX))
        self.Y_C1.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_C2.setText(str(mouseX))
        self.Y_C2.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_C3.setText(str(mouseX))
        self.Y_C3.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_C4.setText(str(mouseX))
        self.Y_C4.setText(str(mouseY))

    def openLocation_D(self):
        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_D1.setText(str(mouseX))
        self.Y_D1.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_D2.setText(str(mouseX))
        self.Y_D2.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_D3.setText(str(mouseX))
        self.Y_D3.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_D4.setText(str(mouseX))
        self.Y_D4.setText(str(mouseY))

    def openLocation_E(self):
        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_E1.setText(str(mouseX))
        self.Y_E1.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_E2.setText(str(mouseX))
        self.Y_E2.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_E3.setText(str(mouseX))
        self.Y_E3.setText(str(mouseY))

    def openLocation_F(self):
        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_F1.setText(str(mouseX))
        self.Y_F1.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_F2.setText(str(mouseX))
        self.Y_F2.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_F3.setText(str(mouseX))
        self.Y_F3.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_F4.setText(str(mouseX))
        self.Y_F4.setText(str(mouseY))

        time.sleep(3)
        sd.Beep(1000, 500)
        mouseX, mouseY = pyautogui.position()
        self.X_F5.setText(str(mouseX))
        self.Y_F5.setText(str(mouseY))

    def test2_for_click(self):
        pyautogui.moveTo(int(self.X_A1.text()), int(self.Y_A1.text()))
        print(int(self.X_A1.text()))
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(int(self.X_A2.text()), int(self.Y_A2.text()))
        pyautogui.click()
        time.sleep(1)
        pyautogui.write(self.S_ID.text())
        time.sleep(1)
        pyautogui.moveTo(int(self.X_A3.text()), int(self.Y_A3.text()))
        pyautogui.click()
        time.sleep(1)
        pyautogui.write(self.S_PASSWORD.text())
        time.sleep(1)


    def saveText(self):
        T = open("locations.txt", 'w')
        Lines = self.X_A1.text() + '\n' + self.Y_A1.text() + '\n'
        Lines = Lines + self.X_A2.text() + '\n' + self.Y_A2.text() + '\n'
        Lines = Lines + self.X_A3.text() + '\n' + self.Y_A3.text() + '\n'
        Lines = Lines + self.X_A4.text() + '\n' + self.Y_A4.text() + '\n'
        Lines = Lines + self.X_B1.text() + '\n' + self.Y_B1.text() + '\n'
        Lines = Lines + self.X_B2.text() + '\n' + self.Y_B2.text() + '\n'
        Lines = Lines + self.X_B3.text() + '\n' + self.Y_B3.text() + '\n'
        Lines = Lines + self.X_B4.text() + '\n' + self.Y_B4.text() + '\n'
        Lines = Lines + self.X_C1.text() + '\n' + self.Y_C1.text() + '\n'
        Lines = Lines + self.X_C2.text() + '\n' + self.Y_C2.text() + '\n'
        Lines = Lines + self.X_C3.text() + '\n' + self.Y_C3.text() + '\n'
        Lines = Lines + self.X_C4.text() + '\n' + self.Y_C4.text() + '\n'
        Lines = Lines + self.X_D1.text() + '\n' + self.Y_D1.text() + '\n'
        Lines = Lines + self.X_D2.text() + '\n' + self.Y_D2.text() + '\n'
        Lines = Lines + self.X_D3.text() + '\n' + self.Y_D3.text() + '\n'
        Lines = Lines + self.X_D4.text() + '\n' + self.Y_D4.text() + '\n'
        Lines = Lines + self.X_E1.text() + '\n' + self.Y_E1.text() + '\n'
        Lines = Lines + self.X_E2.text() + '\n' + self.Y_E2.text() + '\n'
        Lines = Lines + self.X_E3.text() + '\n' + self.Y_E3.text() + '\n'
        Lines = Lines + self.X_F1.text() + '\n' + self.Y_F1.text() + '\n'
        Lines = Lines + self.X_F2.text() + '\n' + self.Y_F2.text() + '\n'
        Lines = Lines + self.X_F3.text() + '\n' + self.Y_F3.text() + '\n'
        Lines = Lines + self.X_F4.text() + '\n' + self.Y_F4.text() + '\n'
        Lines = Lines + self.X_F5.text() + '\n' + self.Y_F5.text() + '\n'
        T.write(Lines)
        T.close()

    def getLocation(self):
        time.sleep(3)
        a, b = pyautogui.position()
        self.nogada.setText(str(a) + ', ' + str(b))



app = QApplication(sys.argv)
# 앱을 만든다 = 어플리케이션을 실행할.
mainWindow = WindowClass()
# 메인윈도우 실행
mainWindow.show()
# 메인윈도우 보여줌.
app.exec_()
# 위에서 만들고 선언한 앱을 실행
# 이 위로 일종의 무한루프를 선언함. 무한루프 중 조건이 달성되면 시행하고 다시 루프하고...

def print_hi(name):
    print("테스트")


if __name__ == '__main__':
    print_hi('PyCharm')
