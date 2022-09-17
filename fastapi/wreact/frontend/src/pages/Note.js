import React, { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
let dummyData = [
  { id: "1", body: "Get milk" },
  { id: "2", body: "Wash car" },
  { id: "3", body: "Start coding" },
];
const Note = () => {
  let navigate = useNavigate();
  let params = useParams();
  let noteId = params.id;
  let noteItem = dummyData.find((note) => note.id === noteId);
  let [note, setNote] = useState(null);
  useEffect(() => {
    if (noteId !== "add") getNote();
  }, [noteId]);
  let getNote = async () => {
    let response = await fetch(`http://127.0.0.1:8000/notes/${noteId}`);
    let data = await response.json();
    setNote(data);
  };
  let submitData = async (e) => {
    e.preventDefault();
    let url = "http://127.0.0.1:8000/notes";
    let method = "POST";
    if (noteId !== "add") {
      url = `http://127.0.0.1:8000/notes/${params.id}`;
      method = "PUT";
    }
    await fetch(url, {
      method: method,
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ body: note.body }),
    });
    navigate("/");
  };
  return (
    <div>
      <Link to={"/"}>Go Back</Link>
      {noteId !== "add" && <button>Delete</button>}
      <textarea
        onChange={(e) => {
          setNote({ ...note, body: e.target.value });
        }}
        value={note?.body}
        placeholder="Add note..."
      ></textarea>
      <button onClick={submitData}>Save</button>
    </div>
  );
};
export default Note;
