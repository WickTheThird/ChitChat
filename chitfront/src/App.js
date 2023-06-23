import React from "react";
import {useState, useEffect} from "react";
import EntryForm from './components/entry_forms';
import { Routes, Route } from "react-router-dom";

function App() {

    //?Testing

    //> About Button

    return (
      <div>

        <>
          <Routes>
            <Route path="/" element={<EntryForm />} />
          </Routes>
        </>

        <a href="/" data-testid="learn-react-link" style={{visibility: 'hidden'}}>Learn React</a>
      </div>
    );
}

export default App;
