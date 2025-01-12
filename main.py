import io
import sys
import sqlite3

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QTableWidget

my_widget_design = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>800</width>
    <height>600</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>800</width>
    <height>600</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Фильмотека</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTabWidget" name="tabWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>800</width>
      <height>600</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="toolTip">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Пасхалка)&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
    <property name="currentIndex">
     <number>0</number>
    </property>
    <property name="iconSize">
     <size>
      <width>30</width>
      <height>30</height>
     </size>
    </property>
    <widget class="QWidget" name="filmsTab">
     <attribute name="title">
      <string>Фильмы</string>
     </attribute>
     <widget class="QPushButton" name="addFilmButton">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>10</y>
        <width>141</width>
        <height>61</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>10</pointsize>
       </font>
      </property>
      <property name="text">
       <string>Добавить фильм</string>
      </property>
     </widget>
     <widget class="QPushButton" name="editFilmButton">
      <property name="geometry">
       <rect>
        <x>180</x>
        <y>10</y>
        <width>151</width>
        <height>61</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>10</pointsize>
       </font>
      </property>
      <property name="text">
       <string>Изменить фильм</string>
      </property>
     </widget>
     <widget class="QPushButton" name="deleteFilmButton">
      <property name="geometry">
       <rect>
        <x>350</x>
        <y>10</y>
        <width>141</width>
        <height>61</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>10</pointsize>
       </font>
      </property>
      <property name="text">
       <string>Удалить фильм</string>
      </property>
     </widget>
     <widget class="QTableWidget" name="filmsTable">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>90</y>
        <width>801</width>
        <height>431</height>
       </rect>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="genresTab">
     <attribute name="title">
      <string>Жанры</string>
     </attribute>
     <widget class="QPushButton" name="addGenreButton">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>10</y>
        <width>161</width>
        <height>61</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>10</pointsize>
       </font>
      </property>
      <property name="text">
       <string>Добавить жанр</string>
      </property>
     </widget>
     <widget class="QPushButton" name="editGenreButton">
      <property name="geometry">
       <rect>
        <x>190</x>
        <y>10</y>
        <width>171</width>
        <height>61</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>10</pointsize>
       </font>
      </property>
      <property name="text">
       <string>Редактировать жанр</string>
      </property>
     </widget>
     <widget class="QPushButton" name="deleteGenreButton">
      <property name="geometry">
       <rect>
        <x>390</x>
        <y>10</y>
        <width>131</width>
        <height>61</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>10</pointsize>
       </font>
      </property>
      <property name="text">
       <string>Удалить жанр</string>
      </property>
     </widget>
     <widget class="QTableWidget" name="genresTable">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>90</y>
        <width>801</width>
        <height>441</height>
       </rect>
      </property>
     </widget>
    </widget>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

add_film_widget_design = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>350</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>500</width>
    <height>350</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>500</width>
    <height>350</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Добавить элемент</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>141</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Название</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>70</y>
      <width>141</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Год выпуска</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>141</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Жанр</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>170</y>
      <width>131</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Длина</string>
    </property>
   </widget>
   <widget class="QComboBox" name="comboBox">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>130</y>
      <width>311</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>240</y>
      <width>151</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="title">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>20</y>
      <width>311</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="year">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>70</y>
      <width>311</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="duration">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>190</y>
      <width>311</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>500</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

add_genre_widget_design = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>350</width>
    <height>174</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPlainTextEdit" name="title">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>20</y>
      <width>211</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>10</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>15</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Название</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>70</y>
      <width>141</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>15</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>350</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(my_widget_design)
        uic.loadUi(f, self)

        self.con = sqlite3.connect('films_db.sqlite')

        self.selected_items = []
        self.ids = []

        self.add_film_widget = AddFilmWidget(self)
        self.edit_film_widget = AddFilmWidget(self, 1)
        self.add_genre_widget = AddGenreWidget(self)
        self.edit_genre_widget = AddGenreWidget(self, 1)

        self.addFilmButton.clicked.connect(self.add_film)
        self.editFilmButton.clicked.connect(self.edit_film)
        self.deleteFilmButton.clicked.connect(self.delete_film)
        self.addGenreButton.clicked.connect(self.add_genre)
        self.editGenreButton.clicked.connect(self.edit_genre)
        self.deleteGenreButton.clicked.connect(self.delete_genre)

        self.draw_films_table()
        self.draw_genres_table()

        self.tabWidget.currentChanged.connect(self.tab_changed)

        self.filmsTable.setSelectionMode(QTableWidget.SelectionMode.MultiSelection)
        self.genresTable.setSelectionMode(QTableWidget.SelectionMode.MultiSelection)

    def add_film(self):
        self.add_film_widget.show()

    def edit_film(self):
        self.selected_items = self.filmsTable.selectedItems()
        if self.selected_items:
            self.ids = [self.filmsTable.item(self.selected_items[0].row(), 0).text()]
            if len(set(i.row() for i in self.selected_items)) == 1:
                self.statusbar.showMessage('')
                self.edit_film_widget.update_edit_window()
                self.edit_film_widget.show()
            else:
                self.statusbar.showMessage('Для редактирования можно выбрать только 1 строку!')
        else:
            self.statusbar.showMessage('Ничего не выбрано')

    def delete_film(self):
        self.selected_items = self.filmsTable.selectedItems()
        if not len(self.selected_items):
            self.statusbar.showMessage('Ничего не выбрано')
        else:
            self.statusbar.showMessage('')
            ids = []
            for i in self.selected_items:
                id = self.filmsTable.item(i.row(), 0).text()
                if id not in ids:
                    ids.append(id)

            # Спрашиваем у пользователя подтверждение на удаление элементов
            valid = QMessageBox.question(
                self, '', "Действительно удалить элементы с id " + ",".join(ids),
                buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            # Если пользователь ответил утвердительно, удаляем элементы.
            # Не забываем зафиксировать изменения
            if valid == QMessageBox.StandardButton.Yes:
                self.con.cursor().execute("DELETE FROM films WHERE id IN (" + ", ".join(
                    '?' * len(ids)) + ")", ids)
                self.con.commit()
            else:
                # Снимаем выделение с всех выделенных ячеек
                for selected_range in self.selected_items:
                    selected_range.setSelected(False)
            self.draw_films_table()

    def add_genre(self):
        self.add_genre_widget.show()

    def edit_genre(self):
        self.selected_items = self.genresTable.selectedItems()
        if self.selected_items:
            self.ids = [self.genresTable.item(self.selected_items[0].row(), 0).text()]
            if len(set(i.row() for i in self.selected_items)) == 1:
                self.statusbar.showMessage('')
                self.edit_genre_widget.update_edit_window()
                self.edit_genre_widget.show()
            else:
                self.statusbar.showMessage('Для редактирования можно выбрать только 1 строку!')
        else:
            self.statusbar.showMessage('Ничего не выбрано')

    def delete_genre(self):
        self.selected_items = self.genresTable.selectedItems()
        if not len(self.selected_items):
            self.statusbar.showMessage('Ничего не выбрано')
        else:
            self.statusbar.showMessage('')
            ids = []
            for i in self.selected_items:
                id = self.genresTable.item(i.row(), 0).text()
                if id not in ids:
                    ids.append(id)

            # Спрашиваем у пользователя подтверждение на удаление элементов
            valid = QMessageBox.question(
                self, '', "Действительно удалить элементы с id " + ",".join(ids),
                buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            # Если пользователь ответил утвердительно, удаляем элементы.
            # Не забываем зафиксировать изменения
            if valid == QMessageBox.StandardButton.Yes:
                self.con.cursor().execute("UPDATE genres SET title = NULL WHERE id IN (" + ", ".join(
                    '?' * len(ids)) + ")", ids)
                self.con.commit()
            else:
                # Снимаем выделение с всех выделенных ячеек
                for selected_range in self.selected_items:
                    selected_range.setSelected(False)
            self.draw_films_table()
            self.draw_genres_table()

    def draw_films_table(self):
        result = self.con.cursor().execute("SELECT films.id, films.title, films.year, "
                                           "COALESCE(genres.title, films.genre), films.duration FROM films"
                                           " LEFT JOIN genres ON films.genre = genres.id").fetchall()[::-1]
        self.filmsTable.setRowCount(len(result))
        self.filmsTable.setColumnCount(len(result[0]))

        # Устанавливаем заголовки столбцов
        header_labels = ['ИД', 'Название', 'Год выпуска', 'Жанр', 'Продолжительность']
        self.filmsTable.setHorizontalHeaderLabels(header_labels)

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                item = QTableWidgetItem(str(val))
                self.filmsTable.setItem(i, j, item)

    def draw_genres_table(self):
        result = self.con.cursor().execute("SELECT * FROM genres WHERE title NOT NULL").fetchall()
        self.genresTable.setRowCount(len(result))
        self.genresTable.setColumnCount(len(result[0]))

        # Устанавливаем заголовки столбцов
        header_labels = ['ИД', 'Название жанра']
        self.genresTable.setHorizontalHeaderLabels(header_labels)

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                item = QTableWidgetItem(str(val))
                self.genresTable.setItem(i, j, item)

    def update_films_table(self):
        result = self.con.cursor().execute("SELECT * FROM films ORDER BY id DESC LIMIT 1").fetchone()

        self.filmsTable.insertRow(0)  # Вставляем строку в начало таблицы
        for j, val in enumerate(result):
            item = QTableWidgetItem(str(val))
            self.filmsTable.setItem(0, j, item)

    def update_genres_table(self):
        result = self.con.cursor().execute("SELECT * FROM genres ORDER BY id DESC LIMIT 1").fetchone()

        self.genresTable.insertRow(-1)  # Вставляем строку в начало таблицы
        for j, val in enumerate(result):
            item = QTableWidgetItem(str(val))
            self.genresTable.setItem(-1, j, item)

    def tab_changed(self, index):
        if index == 0:
            self.update_films_table()
        else:
            self.update_genres_table()


class AddFilmWidget(QMainWindow):
    def __init__(self, parent=None, film_id=None):
        super().__init__(parent)
        f = io.StringIO(add_film_widget_design)
        uic.loadUi(f, self)
        self.parent = parent
        self.con = sqlite3.connect('films_db.sqlite')

        self.film_id = film_id
        if film_id is not None:
            self.pushButton.clicked.connect(self.get_editing_verdict)
            self.pushButton.setText('Отредактировать')
            self.setWindowTitle('Редактирование записи')
        else:
            self.pushButton.clicked.connect(self.get_adding_verdict)

        self.params = {j: i for i, j in self.con.cursor().execute("SELECT * FROM genres").fetchall()}

        for i in self.params.keys():
            self.comboBox.addItem(i)

    def update_edit_window(self):
        self.title.setPlainText(self.parent.filmsTable.item(self.parent.selected_items[0].row(), 1).text())
        self.year.setPlainText(self.parent.filmsTable.item(self.parent.selected_items[0].row(), 2).text())
        self.comboBox.addItem(self.parent.filmsTable.item(self.parent.selected_items[0].row(), 3).text())
        self.comboBox.setCurrentText(self.parent.filmsTable.item(self.parent.selected_items[0].row(), 3).text())
        self.duration.setPlainText(self.parent.filmsTable.item(self.parent.selected_items[0].row(), 4).text())

    def get_adding_verdict(self):
        try:
            genre = self.comboBox.currentText()
            if not self.title.toPlainText() or not self.year.toPlainText() or not self.duration.toPlainText() or \
                    not int(self.duration.toPlainText()) > 0 or not 0 <= int(self.year.toPlainText()) < 2025:
                raise ValueError
        except ValueError:
            self.statusbar.showMessage('Неверно заполнена форма')
            return False
        query = '''INSERT INTO films (title, year, genre, duration) VALUES (?, ?, ?, ?)'''
        values = (self.title.toPlainText(), self.year.toPlainText(),
                  self.con.cursor().execute('SELECT id FROM genres WHERE title = ?', (genre,)).fetchall()[0][0]
                  if genre.isalpha() else genre, self.duration.toPlainText())
        self.title.setPlainText('')
        self.year.setPlainText('')
        self.comboBox.setCurrentText(list(self.params.keys())[0])
        self.duration.setPlainText('')
        self.con.cursor().execute(query, values)
        self.con.commit()
        self.parent.draw_films_table()
        self.close()
        return True

    def get_editing_verdict(self):
        try:
            genre = self.comboBox.currentText()
            if not self.title.toPlainText() or not self.year.toPlainText() or not self.duration.toPlainText() or \
                    not int(self.duration.toPlainText()) > 0 or not 0 <= int(self.year.toPlainText()) < 2025:
                raise ValueError
        except ValueError:
            self.statusbar.showMessage('Неверно заполнена форма')
            return False
        query = '''UPDATE films SET title = ?, year = ?, genre = ?, duration = ? WHERE id = ?'''
        values = (
            self.title.toPlainText(), self.year.toPlainText(), self.con.cursor().execute('SELECT id FROM genres WHERE '
                                                                                         'title = ?',
                                                                                         (genre,)).fetchall()[0][
                0] if genre.isalpha() else genre, self.duration.toPlainText(),
            self.parent.ids[0])
        self.con.cursor().execute(query, values)
        self.con.commit()
        self.parent.draw_films_table()
        self.close()
        return True


class AddGenreWidget(QMainWindow):
    def __init__(self, parent=None, genre_id=None):
        super().__init__(parent)
        f = io.StringIO(add_genre_widget_design)
        uic.loadUi(f, self)
        self.parent = parent
        self.setWindowTitle('Добавление записи')

        self.con = sqlite3.connect('films_db.sqlite')

        self.genre_id = genre_id
        if genre_id is not None:
            self.pushButton.clicked.connect(self.get_editing_verdict)
            self.pushButton.setText('Отредактировать')
            self.setWindowTitle('Редактирование записи')
        else:
            self.pushButton.clicked.connect(self.get_adding_verdict)

    def update_edit_window(self):
        self.title.setPlainText(self.parent.genresTable.item(self.parent.selected_items[0].row(), 1).text())

    def get_adding_verdict(self):
        try:
            title = self.title.toPlainText()
            self.title.setPlainText('')
            if not title:
                raise ValueError
        except ValueError:
            self.statusbar.showMessage('Неверно заполнена форма')
            return False
        query = '''INSERT INTO genres (title) VALUES (?)'''
        values = (title,)
        self.con.cursor().execute(query, values)
        self.con.commit()
        self.parent.draw_genres_table()
        self.close()
        return True

    def get_editing_verdict(self):
        try:
            title = self.title.toPlainText()
            if not title:
                raise ValueError
        except ValueError:
            self.statusbar.showMessage('Неверно заполнена форма')
            return False
        query = '''UPDATE genres SET title = ? WHERE id = ?'''
        values = (title, self.parent.ids[0])
        self.con.cursor().execute(query, values)
        self.con.commit()
        self.parent.draw_genres_table()
        self.close()
        return True


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

