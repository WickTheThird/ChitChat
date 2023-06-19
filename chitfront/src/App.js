import React from "react";
import {useState, useEffect} from "react";
import EntryForm from './components/entry_forms';

function App() {
    //> States
    const [reg, setReg] = useState(false);

    //> SignUp Button aka swich
    const signUp = () => {
      return (
        <div onClick={(event) => setReg(!reg)} className="flex flex-col justify-center items-center min-h-screen box-border h-10 w-20 text-center align-baseline bg-sky-500/100 text-zinc-50/100 absolute top-100" style={{cursor:'pointer'}}>
          {!reg ? "SignUp" : "LogIn"}
        </div>
      );
    };
    //?Testing
    useEffect(() => {
      console.log("Main: " + reg);
    }, [reg]);

    //> About Button

    return (
      <div>
        {signUp()}

        <EntryForm  isRegister={reg} />
        <a href="/" data-testid="learn-react-link" style={{visibility: 'hidden'}}>Learn React</a>
      </div>
    );
}

export default App;
