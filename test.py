from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.clearcolor = (169/255, 169/255, 169/255, 1)

char_set_one = {
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
}

char_set_two = {
    'A': '10',
    'B': '11',
    'C': '12',
    'D': '13',
    'E': '14',
    'F': '15'
}


class MyLayout(Widget):
    # function for returning decimal number from other bases
    def decimal(self):
        info = self.data.text.upper()
        try:
            if '-' in info:
                self.data.text = "Error"
            elif 'DEC' in info:
                self.data.text = str(int(info.replace('DEC', '')))
            elif 'BIN' in info:
                if '2' in info or '3' in info or '4' in info or '5' in info or '6' in info or '7' in info or '8' in info or '9' in info:
                    self.data.text = 'Error'
                else:
                    piece = info.replace('BIN', '')
                    length = len(piece)
                    answer = 0
                    for a in range(len(piece)):
                        answer += int(piece[length - (a+1)]) * (2**a)
                    self.data.text = str(answer)
            elif 'OCT' in info:
                piece = info.replace('OCT', '')
                if '8' in info or '9' in info:
                    self.data.text = "Error"
                else:
                    length = len(piece)
                    answer = 0
                    for a in range(len(piece)):
                        answer += int(piece[length - (a + 1)]) * (8 ** a)
                    self.data.text = str(answer)
            elif 'HEX' in info:
                piece = info.replace('HEX', '')
                length = len(piece)
                answer = 0
                for a in range(len(piece)):
                    point = piece[length - (a + 1)]
                    answer += int(char_set_two.get(point, point)) * (16 ** a)
                self.data.text = str(answer)
            else:
                self.data.text = "Error"
        except:
            self.data.text = "Error"

    # function for returning binary number from other bases
    def binary(self):
        info = self.data.text.upper()
        try:
            if '-' in info:
                self.data.text = "Error"
            elif 'BIN' in info:
                value = str(int(info.replace('BIN', '')))
                if '2' in value or '3' in value or '4' in value or '5' in value or '6' in value or '7' in value or '8' in value or '9' in value:
                    self.data.text = 'Error'
                else:
                    self.data.text = value

            elif 'DEC' in info:
                piece = int(info.replace('DEC', ''))
                part = ''
                while int(piece) > 0:
                    part = str(piece % 2) + part
                    piece = piece // 2
                self.data.text = part
            elif 'OCT' in info:
                piece = info.replace('OCT', '')
                if '8' in info or '9' in info:
                    self.data.text = "Error"
                else:
                    length = len(piece)
                    answer = 0
                    for a in range(len(piece)):
                        answer += int(piece[length - (a + 1)]) * (8 ** a)
                    part = ''
                    while answer > 0:
                        part = str(answer % 2) + part
                        answer = answer // 2
                    self.data.text = part
            elif 'HEX' in info:
                piece = info.replace('HEX', '')
                length = len(piece)
                answer = 0
                for a in range(len(piece)):
                    point = piece[length - (a + 1)]
                    answer += int(char_set_two.get(point, point)) * (16 ** a)
                part = ''
                while answer > 0:
                    part = str(answer % 2) + part
                    answer = answer // 2
                self.data.text = part
            else:
                self.data.text = "Error"
        except:
            self.data.text = "Error"

    # function for returning octal number from other bases
    def octal(self):
        info = self.data.text.upper()
        try:
            if '-' in info:
                self.data.text = "Error"
            elif 'OCT' in info:
                value = str(int(info.replace('OCT', '')))
                if '8' in value or '9' in value:
                    self.data.text = "Error"
                else:
                    self.data.text = value
            elif 'DEC' in info:
                piece = int(info.replace('DEC', ''))
                part = ''
                while int(piece) > 0:
                    part = str(piece % 8) + part
                    piece = piece // 8
                self.data.text = part
            elif 'BIN' in info:
                piece = info.replace('BIN', '')
                if '2' in info or '3' in info or '4' in info or '5' in info or '6' in info or '7' in info or '8' in info or '9' in info:
                    self.data.text = 'Error'
                else:
                    length = len(piece)
                    answer = 0
                    for a in range(len(piece)):
                        answer += int(piece[length - (a + 1)]) * (2 ** a)
                    part = ''
                    while answer > 0:
                        part = str(answer % 8) + part
                        answer = answer // 8
                    self.data.text = part
            elif 'HEX' in info:
                piece = info.replace('HEX', '')
                length = len(piece)
                answer = 0
                for a in range(len(piece)):
                    point = piece[length - (a + 1)]
                    answer += int(char_set_two.get(point, point)) * (16 ** a)
                part = ''
                while answer > 0:
                    part = str(answer % 8) + part
                    answer = answer // 8
                self.data.text = part
            else:
                self.data.text = "Error"
        except:
            self.data.text = "Error"

    # function for returning hexadecimal number from other bases
    def hexadecimal(self):
        info = self.data.text.upper()
        try:
            if '-' in info:
                self.data.text = "Error"
            elif 'HEX' in info:
                self.data.text = info.replace('HEX', '')
            elif 'DEC' in info:
                piece = int(info.replace('DEC', ''))
                part = ''
                while int(piece) > 0:
                    portion = str(piece % 16)
                    part = char_set_one.get(portion, portion) + part
                    piece = piece // 16
                self.data.text = part
            elif 'BIN' in info:
                piece = info.replace('BIN', '')
                if '2' in info or '3' in info or '4' in info or '5' in info or '6' in info or '7' in info or '8' in info or '9' in info:
                    self.data.text = 'Error'
                else:
                    length = len(piece)
                    answer = 0
                    for a in range(len(piece)):
                        answer += int(piece[length - (a + 1)]) * (2 ** a)
                    part = ''
                    while answer > 0:
                        portion = str(answer % 16)
                        part = char_set_one.get(portion, portion) + part
                        answer = answer // 16
                    self.data.text = part
            elif 'OCT' in info:
                piece = info.replace('OCT', '')
                if '8' in info or '9' in info:
                    self.data.text = "Error"
                else:
                    length = len(piece)
                    answer = 0
                    for a in range(len(piece)):
                        answer += int(piece[length - (a + 1)]) * (8 ** a)
                    part = ''
                    while answer > 0:
                        portion = str(answer % 16)
                        part = char_set_one.get(portion, portion) + part
                        answer = answer // 16
                    self.data.text = part
            else:
                self.data.text = "Error"
        except:
            self.data.text = "Error"


class BaseApp(App):
    def build(self):
        self.title = '7XBaseConverter'
        return MyLayout()


if __name__ == '__main__':
    BaseApp().run()
