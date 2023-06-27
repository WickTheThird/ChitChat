import React, { useState, useEffect } from 'react';

function EntryForm() {
    //> States
    const [reg, setReg] = useState(false);
    const [isRegister, setIsRegister] = useState({isRegister: false});

    //> Set Auth switch
    const signUp = () => {
        return (
          <div onClick={(event) => setReg(!reg)} className="flex flex-col justify-center items-center min-h-screen box-border h-10 w-20 text-center align-baseline bg-sky-500/100 text-zinc-50/100 absolute top-100" style={{cursor:'pointer'}}>
            {!reg ? "SignUp" : "LogIn"}
          </div>
        );
      };

    //> Register
    useEffect (() => {
        setReg(isRegister);
        console.log("Register: " + isRegister);
        console.log("Reg: " + reg);
    }, [isRegister]);

    //> Login
    const login = async (event) => {
        
        if (event) {
            event.preventDefault();

            // console.log(event.target.username.value);
            // console.log(event.target.email.value);
            // console.log(event.target.password.value);

            let username = event.target.username.value;
            let email = event.target.email.value;
            let password = event.target.password.value;

            try {
                const response = await fetch('http://localhost:8000/api/login/', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json',
                  },
                  body: JSON.stringify({ 
                    "name": username, 
                    "email": email,
                    "password1": password,
                    }),
                });
            
                if (response.status === 400) {
                  const data = await response.json();
                  console.error('Validation errors:', data);
                  //? handle validation errors in your component --> small module cards at the top of the screen
                } else {
                  //? handle successful login --> store token in the local storage so that it can be used when making API calls
                }
              } catch (error) {
                console.error('Error during login:', error);
              }

        }

    };

    const LogForm = () => {
        return (
            <div className="p-10 max-w-sm mx-auto bg-white rounded-xl shadow-lg text-center" style={{position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', WebkitTransform: 'translate(-50%, -50%)'}}>
                <div className="shrink-0">
                </div>

                <div>
                    <div className="text-xl font-medium text-black">ChitChat</div>
                    <p className="text-slate-500">Login</p>

                    <form id="signForm" onSubmit={(event => login(event))}>  
                        <input type="text" htmlFor="username" id="username" className="form-input px-4 py-3 shadow-lg mt-6 rounded-md focus:outline-none" placeholder="Username"/>
                        <input type="email"  htmlFor="email" id="email"  className="form-input px-4 py-3 shadow-lg mt-5 rounded-md focus:outline-none" placeholder="Email"/>
                        <input type="password" htmlFor="password" id="password" className="form-input px-4 py-3 shadow-lg mt-5 rounded-md focus:outline-none" placeholder="Password"/>
                        <br/>

                        <input type="submit" className="px-2 py-2 shadow mt-5 focus:outline-none bg-sky-500 rounded text-white cursor-pointer"/>
                    </form>

                </div>
            </div>
        );
    };

    //> Register
    const register = async (event) => {

        if (event) {
            event.preventDefault();

            // console.log(event.target.username.value);
            // console.log(event.target.email.value);
            // console.log(event.target.password1.value);
            // console.log(event.target.password2.value);

            let username = event.target.username.value;
            let email = event.target.email.value;
            let password1 = event.target.password1.value;
            let password2 = event.target.password2.value;

            try {

                const response = await fetch(`http://localhost:8000/api/signup/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        name: username, 
                        email: email,
                        password1: password1,
                        password2: password2,
                    }),

                });

                if (response.status === 400) {
                    const data = await response.json();
                    console.error("Validation errors: ", data);
                    //? handle validation errors --> small cards modules at the top of the screen
                } else {
                    //? handle signup --> set reg to login mode since credentials are in the backend
                }

            } catch (error) {
                console.log("Error during signUp: ", error);
            }
        }
    };

    const RegForm = () => {
        return (
            <div className="p-10 max-w-sm mx-auto bg-white rounded-xl shadow-lg text-center" style={{position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', WebkitTransform: 'translate(-50%, -50%)'}}>
                <div className="shrink-0">
                </div>

                <div>
                    <div className="text-xl font-medium text-black">ChitChat</div>
                    <p className="text-slate-500">SignUp</p>

                    <form id="signForm" onSubmit={(event => register(event))}>  
                        <input type="text" htmlFor="username" id="username" className="form-input px-4 py-3 shadow-lg mt-6 rounded-md focus:outline-none" placeholder="Username"/>
                        <input type="email" htmlFor="email" id="email" className="form-input px-4 py-3 shadow-lg mt-5 rounded-md focus:outline-none" placeholder="Email"/>
                        <input type="password" htmlFor="password1" id="password1" className="form-input px-4 py-3 shadow-lg mt-5 rounded-md focus:outline-none" placeholder="Password"/>
                        <input type="password" htmlFor="password2" id = "password2" className="form-input px-4 py-3 shadow-lg mt-5 rounded-md focus:outline-none" placeholder="Password"/>
                        <br/>

                        <input type="submit" className="px-2 py-2 shadow mt-5 focus:outline-none bg-sky-500 rounded text-white cursor-pointer"/>
                    </form>

                </div>
            </div>
        );
    };

    return (
        <div>
            {signUp()}
            {reg ? <RegForm/> : <LogForm/>}
        </div>
    );
};

export default EntryForm;
