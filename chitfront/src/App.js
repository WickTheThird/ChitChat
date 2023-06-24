import React from "react";
import {useState, useEffect} from "react";
import { Routes, Route } from "react-router-dom";

import EntryForm from './components/entry_forms';
import Home from "./components/home";

function App() {

    return (
      <div>

        <Routes>
          <Route path="/" element={<EntryForm />} />
          <Route path="/home" element={<Home />} />
        </Routes>

        <a href="/" data-testid="learn-react-link" style={{visibility: 'hidden'}}>Learn React</a>
      </div>
    );
}

export default App;
