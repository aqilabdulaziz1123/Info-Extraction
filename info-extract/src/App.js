import React, {useState,useEffect,useContext} from 'react';
import logo from './logo.svg';
import './App.css';
import MainForm from './Form'

function App() { 

  return (
    <div className="App">
      {/* <header className="App-header"> */}
        {/* <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
        <h1>Info-Extraction</h1>
      {/* </header> */}
      {/* <div> */}
      <div>
        <MainForm/>
        {/* <h1>tes</h1> */}
      </div>
      {/* </div> */}
    </div>
  );
}

export default App;
