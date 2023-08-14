
from datetime import datetime

class Note:
    def __init__(self, id, title, text, created_date, updated_date):
        self.id = id
        self.title = title
        self.text = text
        self.created_date = created_date
        self.updated_date = updated_date
        
class Notes:
    def __init__(self):
        self.notes = []

    def addNote(self, title, text):
        id = len(self.notes)+1
        created_date = datetime.now()
        updated_date = datetime.now()
        self.notes.append(Note(id, title, text, created_date, updated_date))

    def deleteNote(self, id):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
Notes.addNote(self=Notes, "title", "text",)
"""
Метод Notes.addNote() требует три параметра, я должен передавать два пареметра title и text, не понимаю как убрать self: Notes , что бы программа заработала.
"""
