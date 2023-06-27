import React, { useState, useEffect } from 'react';

function Home() {

    //? States and Effects handling
    const [messageToggle, setMessageToggle] = useState(false);
    const [contacts, setContacts] = useState([]);
    const [whichContact, setWhichContact] = useState(0);


    //? Left Side view aka Contacts
    const contactView = () => {

        //> Request for all the contacts
        const viewContacts = async (event) => {

            if (event) {
                //TODO: actions
            }

        };

        //> UI
        return (
            <div className="flex flex-col justify-center items-center box-border h-screen w-1/3 text-center align-baseline shadow-2xl z-0"> </div>
        );
    };

    //? Right Side view aka Displaying messages
    const messageToUser = (toUser) => {

        //> Request all messages between toUser and mainUser
        const viewMessages = async (event, toUser) => {

            if (event) {
                //TODO: actions
            }

        };

        //> Submit messsage to user
        const sendMessage = async (event, toUser) => {

            if (event) {
                //TODO: actions
            }

        };

        //> UI
        return (
            <div className="flex flex-col justify-center items-center box-border h-screen w-2/3 p-5 shadow-md z-1"> 


                {/* Contact Box/ Profile */}
                <div className=''>

                </div>
                {/* Contact Box/ Profile */}


                {/* The messages */}
                <div className=''>

                </div>
                {/* The messages */}


                {/* The texting box  */}
                <div className='absolute bottom-9'>
                    <form method='POST' action='none'>
                        <div className=''> {/*  <--  */}
                            <input for='message' type='text' htmlFor='messaging' placeholder='Type message...' />
                            <button>Send</button>
                        </div>
                    </form>
                </div>
                {/* The texting box  */}


            </div>
        );
    };

    return (
        <div className="flex flex-row">
            {contactView()}
            {messageToUser()}
        </div>
    );
}

export default Home;

/*
? Quick Note:
        > There is no token passed to the home function due to the fact that this token will be generated in the backend
           >> once the user has signed up.
        > Thus the token will be available in the local storage, or another way we could do it is sessions and cookies, but
           >> that way is becoming obselete and besides cookies have slower access times.
 */
