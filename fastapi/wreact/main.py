from fastapi import FastAPI, Body
from database import db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get('/')
def get_routes():
    return ['/notes', 'notes/<pk>']

@app.get('/notes')
def get_notes():
    notes = db.sql('SELECT * FROM notesapp.notes ORDER BY __updatedtime__ DESC')
    return notes

@app.get('/notes/{pk}')
def get_note(pk:str):
    notes = db.search_by_value('notesapp','notes', [pk], get_attributes=['*'])
    return notes[0]

@app.post('/notes')
def add_note(data = Body()):
    db.insert('notesapp', 'notes', [{"body": data['body']}])
    notes = db.search_by_value('notesapp', 'notes', 'id', "*", get_attributes=['*'])
    return notes

@app.put('/notes/{id}')
def update_note(id:str, data=Body()):
    db.update('notesapp','notes',[{"id":id, "body":data["body"]}])
    notes = db.search_by_value('notesapp','notes', "id","*", get_attributes=["*"])
    return notes

@app.delete('/notes/{id}')
def delete_node(id:str):
    """ 
    Description:
    ------------
    Delete node"""
    db.delete('notesapp','notes',[id])
    notes = db.search_by_value('notesapp','notes', "id", "*", get_attributes=['*'])
    return notes
