import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel,
        QButtonGroup, QListWidget,
        QTextEdit, QLineEdit,
        QInputDialog)
app = QApplication([])
notes = []
win = QWidget()
win.setWindowTitle('Умные заметки')
win.resize(1000, 700)
list_notes = QListWidget()
tags_list = QListWidget()
text_Edit = QTextEdit()
search = QLineEdit()
search.setPlaceholderText('Введите тег...')
name_list_note = QLabel('Список заметок')
create_note = QPushButton('Создать заметку')
delete_note = QPushButton('Удалить заметку')
save_note = QPushButton('Сохранить заметку')
add_tag_to_note = QPushButton('Добавить к заметке')
delete_tag_note = QPushButton('Открепить от заметки')
search_note_tag = QPushButton('Искать заметки по тегу')
tag_search = QVBoxLayout()
worck_withs_notes = QHBoxLayout()
line_save_note = QHBoxLayout()
worck_with_tags = QHBoxLayout()
searchNoteTag = QHBoxLayout()
createNote = QVBoxLayout()
mainLine = QHBoxLayout()
listTags = QLabel('Список тегов')
createNote.addWidget(text_Edit)
worck_with_tags.addWidget(add_tag_to_note)
worck_with_tags.addWidget(delete_tag_note)
searchNoteTag.addWidget(search_note_tag)
tag_search.addWidget(text_Edit)
worck_withs_listnotes = QVBoxLayout()
worck_withs_listnotes.addWidget(list_notes)
worck_withs_listnotes.addWidget(name_list_note)
worck_withs_notes.addWidget(create_note)
worck_withs_notes.addWidget(delete_note)
line_save_note.addWidget(save_note)
worck_withs_listnotes.addLayout(worck_withs_notes)
worck_withs_listnotes.addLayout(line_save_note)
worck_withs_listnotes.addWidget(listTags)
worck_withs_listnotes.addWidget(tags_list)
worck_withs_listnotes.addWidget(search)
worck_withs_listnotes.addLayout(worck_with_tags)
worck_withs_listnotes.addLayout(searchNoteTag)
mainLine.addLayout(createNote)
mainLine.addLayout(worck_withs_listnotes)
win.setLayout(mainLine)

def show_note():
        note_text = list_notes.selectedItems()[0].text()
        for i in notes:
                if i[0] == note_text:
                        text_Edit.setText(i[1])
                        tags_list.clear()
                        tags_list.addItems(i[2])
list_notes.itemClicked.connect(show_note)
def add_note():
        dialog_win, new_note_name = QInputDialog.getText(win, 'Создание новой заметки', 'Введите название заметки')
        if dialog_win != '':
                note_atrebuts = [dialog_win, '', []]
                notes.append(note_atrebuts)
                list_notes.addItem(note_atrebuts[0])
                tags_list.addItems(note_atrebuts[2])
                with open (str(len(notes) - 1) + '.txt', 'w', encoding = 'utf-8') as file:
                        file.write(note_atrebuts[0] + '\n')
def saveNote():
        if list_notes.selectedItems():
                del_element = list_notes.selectedItems()[0].text()
                file_index = 0
                for i in notes:
                        if i[0] == del_element:
                                i[1] = text_Edit.toPlainText()
                                with open (str(file_index) + '.txt', 'w', encoding = 'utf-8') as file:
                                        file.write(i[0] + '\n')
                                        file.write(i[1] + '\n')
                                        for tags in i[2]:
                                                file.write(tags + ' ')
                                        file.write('\n')
                        file_index += 1
        else:
                print('Заметка не выбрана')
create_note.clicked.connect(add_note)
save_note.clicked.connect(saveNote)
win.show()
file_names = 0
list_notes_for_upload = []
while True:
        fileName = str(file_names) + '.txt'
        try:
                with open (fileName, 'r', encoding = 'utf-8') as file:
                        for line in file:
                                line = line.replace('\n', '')
                                list_notes_for_upload.append(line)
                tags_for_txt = list_notes_for_upload[2].split(' ')
                list_notes_for_upload[2] = tags_for_txt
                notes.append(list_notes_for_upload)
                list_notes_for_upload = []
                file_names += 1
        except(IOError):
                break
for i in notes:
        list_notes.addItem(i[0])
app.exec_()