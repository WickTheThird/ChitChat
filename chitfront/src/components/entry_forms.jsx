import {useState, useEffect} from "react";

//> Main
function EntryForm() {
    //> State

    //> Login
    const login = async (event) => {};

    const LogForm = () => {
        return (
            <div className="p-10 max-w-sm mx-auto bg-white rounded-xl shadow-lg text-center" style={{position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', WebkitTransform: 'translate(-50%, -50%)'}}>
                <div className="shrink-0">
                </div>

                <div>
                    <div className="text-xl font-medium text-black">ChitChat</div>
                    <p className="text-slate-500">Login</p>

                    <form id="signForm" onSubmit={(event => login(event))}>  
                        <input type="text" class="form-input px-4 py-3 shadow-lg mt-6 rounded-md focus:outline-none" placeholder="Username"/>
                        <input type="email" class="form-input px-4 py-3 shadow-lg mt-5 rounded-md focus:outline-none" placeholder="Email"/>
                        <input type="password" class="form-input px-4 py-3 shadow-lg mt-5 rounded-md focus:outline-none" placeholder="Password"/>
                        <br/>

                        <input type="submit" class="px-2 py-2 shadow mt-5 focus:outline-none bg-sky-500 rounded text-white cursor-pointer"/>
                    </form>

                </div>
            </div>
        );
    };

    //> Register
    const register = async (event) => {};

    const RegForm = () => {
        return (
            <div className="p-10 max-w-sm mx-auto bg-white rounded-xl shadow-lg text-center" style={{position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', WebkitTransform: 'translate(-50%, -50%)'}}>
                <div className="shrink-0">
                </div>

                <div>
                    <div className="text-xl font-medium text-black">ChitChat</div>
                    <p className="text-slate-500">Login</p>

                    <form id="signForm" onSubmit={(event => register(event))}>  
                        <input type="text" class="form-input px-4 py-3 shadow-lg mt-6 rounded-md focus:outline-none" placeholder="Username"/>
                        <input type="email" class="form-input px-4 py-3 shadow-lg mt-5 rounded-md focus:outline-none" placeholder="Email"/>
                        <input type="password" class="form-input px-4 py-3 shadow-lg mt-5 rounded-md focus:outline-none" placeholder="Password"/>
                        <br/>

                        <input type="submit" class="px-2 py-2 shadow mt-5 focus:outline-none bg-sky-500 rounded text-white cursor-pointer"/>
                    </form>

                </div>
            </div>
        );
    };

    return (
        <div>
            <LogForm/>
        </div>
    );
};

export default EntryForm;
