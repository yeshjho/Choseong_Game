import random
from PyQt5 import QtGui, uic, QtWidgets, QtCore
import sys
import time
import threading

first = [2.0, 11.0, 8.7, 14.5, 36.0, 10.6, 12.3, 12.8, 32.6, 10.5, 28.0, 2.0, 12.8, 32.6, 19.7, 26.7, 18.6, 18.4, 17.4]
second = [-0.3, 13.7, 19.0, 20.0, 10.5, 17.8, 14.5, 19.1, 7.3, 17.5, 19.8, 19.0, 18.7, 8.3, 19.2, 19.9, 19.1, 18.7,
          14.6, 19.4, 14.6]
third = [0.0, 2.0, 14.0, 22.5, 8.7, 31.5, 36.1, 24.5, 10.6, 22.6, 32.9, 33.4, 31.1, 39.2, 39.0, 38.0, 12.3, 12.8, 33.3,
         10.5, 31.0, 2.0, 22.8, 29.7, 29.7, 28.6, 28.4, 27.4]
choseong = []
cholist = ['giyeok', 'nieun', 'digeut', 'rieul', 'mieum', 'bieup', 'siot', 'ieung', 'jieut', 'chieut', 'kieuk', 'tieut',
           'pieup', 'hieut']
cholistko = [['ㄱ'], ['ㄱ', 'ㄱ'], ['ㄴ'], ['ㄷ'], ['ㄷ', 'ㄷ'], ['ㄹ'], ['ㅁ'], ['ㅂ'], ['ㅂ', 'ㅂ'], ['ㅅ'], ['ㅅ', 'ㅅ'], ['ㅇ'],
             ['ㅈ'], ['ㅈ', 'ㅈ'], ['ㅊ'], ['ㅋ'], ['ㅌ'], ['ㅍ'], ['ㅎ']]
jonglistko = [[], ['ㄱ'], ['ㄱ', 'ㄱ'], ['ㄱ', 'ㅅ'], ['ㄴ'], ['ㄴ', 'ㅈ'], ['ㄴ', 'ㅎ'], ['ㄷ'], ['ㄹ'], ['ㄹ', 'ㄱ'], ['ㄹ', 'ㅁ'],
              ['ㄹ', 'ㅂ'], ['ㄹ', 'ㅅ'], ['ㄹ', 'ㅌ'], ['ㄹ', 'ㅍ'], ['ㄹ', 'ㅎ'], ['ㅁ'], ['ㅂ'], ['ㅂ', 'ㅅ'], ['ㅅ'], ['ㅅ', 'ㅅ'],
              ['ㅇ'], ['ㅈ'], ['ㅊ'], ['ㅋ'], ['ㅌ'], ['ㅍ'], ['ㅎ']]
with open("text.txt", 'r', encoding="utf_8") as wordlist:
    words = wordlist.read().splitlines()
lists = {}


def start(self):
    global lists
    lists = {}
    self.ListWord.setText('')
    self.ListScore.setText('')
    self.OptionButton.setEnabled(False)
    self.StartButton.setEnabled(False)
    global choseong
    choseong = []
    for ii in range(1, 17):
        randomint = random.randint(1, 598040)
        if randomint <= 107658:
            choseong.append('ㄱ')
        elif randomint <= 107658 + 67356:
            choseong.append('ㄴ')
        elif randomint <= 175014 + 32969:
            choseong.append('ㄷ')
        elif randomint <= 207983 + 56167:
            choseong.append('ㄹ')
        elif randomint <= 264150 + 45970:
            choseong.append('ㅁ')
        elif randomint <= 310120 + 43123:
            choseong.append('ㅂ')
        elif randomint <= 353243 + 56751:
            choseong.append('ㅅ')
        elif randomint <= 409994 + 107561:
            choseong.append('ㅇ')
        elif randomint <= 517555 + 43203:
            choseong.append('ㅈ')
        elif randomint <= 560758 + 1860:
            choseong.append('ㅊ')
        elif randomint <= 562618 + 2000:
            choseong.append('ㅋ')
        elif randomint <= 564618 + 8205:
            choseong.append('ㅌ')
        elif randomint <= 572823 + 9582:
            choseong.append('ㅍ')
        else:
            choseong.append('ㅎ')

    for jj in cholist:
        code = jj + ' = QtGui.QIcon()'
        code2 = jj + ".addPixmap(QtGui.QPixmap('./ChoseongPic/" + jj + ".png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)"
        exec(code)
        exec(code2)
    number = 0
    for kk in choseong:
        number += 1
        if kk == 'ㄱ':
            code = 'Window.Choseong_' + str(number) + '.setIcon(giyeok)'
        elif kk == 'ㄴ':
            code = 'Window.Choseong_' + str(number) + '.setIcon(nieun)'
        elif kk == 'ㄷ':
            code = 'Window.Choseong_' + str(number) + '.setIcon(digeut)'
        elif kk == 'ㄹ':
            code = 'Window.Choseong_' + str(number) + '.setIcon(rieul)'
        elif kk == 'ㅁ':
            code = 'Window.Choseong_' + str(number) + '.setIcon(mieum)'
        elif kk == 'ㅂ':
            code = 'Window.Choseong_' + str(number) + '.setIcon(bieup)'
        elif kk == 'ㅅ':
            code = 'Window.Choseong_' + str(number) + '.setIcon(siot)'
        elif kk == 'ㅇ':
            code = 'Window.Choseong_' + str(number) + '.setIcon(ieung)'
        elif kk == 'ㅈ':
            code = 'Window.Choseong_' + str(number) + '.setIcon(jieut)'
        elif kk == 'ㅊ':
            code = 'Window.Choseong_' + str(number) + '.setIcon(chieut)'
        elif kk == 'ㅋ':
            code = 'Window.Choseong_' + str(number) + '.setIcon(kieuk)'
        elif kk == 'ㅌ':
            code = 'Window.Choseong_' + str(number) + '.setIcon(tieut)'
        elif kk == 'ㅍ':
            code = 'Window.Choseong_' + str(number) + '.setIcon(pieup)'
        else:
            code = 'Window.Choseong_' + str(number) + '.setIcon(hieut)'
        code2 = 'Window.Choseong_' + str(number) + ".setIconSize(QtCore.QSize(100, 100))"
        exec(code)
        exec(code2)
    with open("misc.txt") as values:
        value = values.read().splitlines()
    self.times = int(value[68]) * 60
    self.TimeLeft.setMaximum(self.times)
    self.TimeLeft.setValue(self.times)
    timery = Timers()
    timery.start()
    self.TextInput.setDisabled(False)
    self.playing = True
    self.TextInput.setFocus()


def textcheck(text):
    texts = text[:-1]
    cholistcopy = choseong[:]
    score = 0
    length = len(texts)
    if length == 1 or length == 2 or length == 3:
        pass
    elif length == 4:
        score += 8.1
    elif length == 5:
        score += 23.3
    elif length == 6:
        score += 27.5
    elif length == 7:
        score += 29
    elif length == 8:
        score += 29.6
    elif length == 9:
        score += 29.9
    else:
        score += 30
    for char in texts:
        if 44032 <= ord(char) <= 55203:
            pass
        else:
            return 'Wrong', 'NoNatmal'
        firstchar = (ord(char) - 44032) // 588
        secondchar = ((ord(char) - 44032) % 588) // 28
        thirdchar = ((ord(char) - 44032) % 588) % 28
        score = score + first[firstchar] + second[secondchar] + third[thirdchar]
        try:
            for i in cholistko[firstchar]:
                cholistcopy.remove(i)
            if thirdchar == 0:
                pass
            else:
                for i in jonglistko[thirdchar]:
                    cholistcopy.remove(i)
        except ValueError:
            return 'Wrong', 'NoJaeum'
    if (texts in words) is True:
        if (texts in lists) is True:
            return 'Wrong', 'NoJungbok'
        else:
            return 'Right', round(score), texts
    else:
        return 'Wrong', 'NoNatmal'


def timeout():
    Window.TextInput.setDisabled(True)
    Window.playing = False
    Window.OptionButton.setDisabled(False)
    Window.StartButton.setDisabled(False)
    Window.TimeOut.show()
    time.sleep(1)
    Window.TimeOut.hide()


class Timers(threading.Thread):
    def run(self):
        for _ in range(1, Window.times + 1):
            Window.times -= 1
            Window.timechanged()
            if Window.times == 0:
                timeout()
            time.sleep(1)


class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("GUI.ui", self)
        self.ui.show()

        with open("bscore.txt", encoding="utf_8") as bscore:
            self.score = bscore.read().splitlines()
        self.BScore.setText(self.score[0] + ' ' + self.score[1])

        self.optionwindow = None
        self.rulewindow = None
        self.times = 0
        self.playing = False
        self.TextInput.setDisabled(True)
        self.TimeOut.hide()
        self.NoJaeum.hide()
        self.NoNatmal.hide()
        self.NoJungbok.hide()

    def Options(self):
        if self.optionwindow is None:
            self.optionwindow = OptionWindow(self)
        self.optionwindow.show()

    def Rules(self):
        if self.rulewindow is None:
            self.rulewindow = RuleWindow(self)
        self.rulewindow.show()

    def StartButton_Pushed(self):
        start(self)

    def OptionButton_Pushed(self):
        self.setDisabled(True)
        self.Options()

    def RuleButton_Pushed(self):
        self.setDisabled(True)
        self.Rules()

    def TextInput_Changed(self):
        text = self.TextInput.toPlainText()
        for i in text:
            if i == '\n' and self.playing is True:
                self.TextInput.setDisabled(True)
                self.NoJaeum.hide()
                self.NoNatmal.hide()
                self.NoJungbok.hide()
                result = textcheck(text)
                if result[0] == 'Right':

                    if (self.score[0] == '') or (int(result[1]) > int(self.score[0])):
                        with open('bscore.txt', 'w', encoding="utf_8") as BScore:
                            BScore.write(str(result[1]) + '\n')
                            BScore.write(str(result[2]) + '\n')
                        self.score[0] = str(result[1])
                        self.score[1] = result[2]
                        self.BScore.setText(str(result[1]) + ' ' + result[2])

                    global lists
                    lists[result[2]] = result[1]
                    texts = ''
                    scores = ''
                    num = 0
                    for ij in sorted(lists, key=lists.get, reverse=True):
                        num += 1
                        texts = texts + ij + '\n'
                        scores = scores + str(lists[ij]) + '\n'
                        if num == 28:
                            break
                    self.ListWord.setText(texts)
                    self.ListScore.setText(scores)

                    self.TextInput.setText('')
                    self.TextInput.setDisabled(False)
                    self.TextInput.setFocus()
                else:
                    if result[1] == 'NoJaeum':
                        self.NoJaeum.show()
                    elif result[1] == 'NoNatmal':
                        self.NoNatmal.show()
                    else:
                        self.NoJungbok.show()
                    self.TextInput.setText('')
                    self.TextInput.setDisabled(False)
                    self.TextInput.setFocus()
            else:
                pass

    def timechanged(self):
        self.TimeLeft.setValue(self.times)


class OptionWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("Option.ui", self)
        self.ui.show()

        with open("misc.txt", encoding="utf_8") as miscs:
            scores = miscs.read().splitlines()
        number = 0
        for ii in scores:
            number += 1
            if number == 70:
                return
            code = 'self.a' + str(number) + '.setValue(' + str(ii) + ')'
            exec(code)

        self.SavedLabel.hide()

    @staticmethod
    def OptionDestroyed():
        Window.setDisabled(False)
        Window.optionwindow = None

    def SaveButton_Pushed(self):
        value = []
        for ii in range(1, 70):
            code = 'value.append(self.a' + str(ii) + '.value())'
            exec(code)
        global first, second, third
        first, second, third = [], [], []
        for jj in range(1, 20):
            first.append(value[jj])
        for kk in range(20, 41):
            second.append(value[kk])
        for ll in range(41, 69):
            third.append(value[ll])

        with open("misc.txt", 'w') as data:
            for ii in value:
                data.write(str(ii) + '\n')

        self.SavedLabel.show()

    def CancelButton_Pushed(self):
        Window.setDisabled(False)
        self.close()
        Window.optionwindow = None


class RuleWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("Rule.ui", self)
        self.ui.show()

    @staticmethod
    def RuleDestroyed():
        Window.setDisabled(False)
        Window.rulewindow = None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = MainWindow(None)
    p = Window.palette()
    p.setColor(Window.backgroundRole(), QtGui.QColor(189, 189, 189))
    Window.setPalette(p)
    Window.show()
    app.exec_()
