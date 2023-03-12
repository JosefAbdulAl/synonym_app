import './App.css';
import React, { useState, useEffect } from 'react';

function App() {
  const [homeString, setHomeString] = useState({})
  const [word, setWord] = useState("")
  const [synonyms, setSynonyms] = useState([])
  const [synonymsInput, setSynonymsInput] = useState("")
  
  const searchWord = (event) => {
    event.preventDefault();
    fetch(`http://localhost:5000/get/${word}`).then(
      res => res.json()
    ).then(
      synonyms => {
        const wordSynonyms = synonyms[word]
        setSynonyms(wordSynonyms)
      }
    )
  }

  const addWord = (event) => {
    event.preventDefault();
    fetch(`http://localhost:5000/add/${word}/${synonymsInput}`).then(
      res => res.json()
    ).then(
      synonyms => {
        const wordSynonyms = synonyms[word]
        setSynonyms(wordSynonyms)
      }
    )
  }

  useEffect(() => {
    fetch("http://localhost:5000/").then(
      res => res.json()
    ).then(
      homeString => {
        setHomeString(homeString)
      }
    )
  }, [])

  return (
    <div className = "App">
      <h1>{homeString.home_string}</h1>
      <div>
        <label>Word: </label>  
          <input
            type="text"
            value={word}
            onChange={(e) => setWord(e.target.value)}
          />
        </div>
        <div>
        <label>Synonyms: </label>  
          <input
            type="text"
            value={synonymsInput}
            onChange={(e) => setSynonymsInput(e.target.value)}
          />
        </div>
        <div><button onClick={searchWord}>Search</button>
        <button onClick={addWord}>Add</button></div>
      <ul>
        {synonyms.map(synonym => (
        <li key={synonym}>{synonym}</li>
        ))}
      </ul>
    </div>
  )
}

export default App;
