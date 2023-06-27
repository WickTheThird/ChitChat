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
                
                try {

                    const response = await fetch('', {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                        }
                    });

                    if (response.status === 400) {
                        const data = await response.json();
                        console.log("Failed to fetch contacts: " + data.message);
                        //? Handle error
                    } else {
                        //? Handle success
                    }

                } catch (event) {

                    console.error('Error fetching contacts: ' + event.message);

                }

            }

        };

        //> UI
        return (

            <div className="flex flex-col justify-center items-center box-border h-screen w-1/3 text-center align-baseline shadow-2xl z-0"> 

                {/* Profile Icon + Search */}
                    <div className=''>

                    </div>
                {/* Profile Icon + Search */}


                {/* Messages */}
                    <div className=''>

                    </div>
                {/* Messages */}


                {/* FOOTER => Setting and other */}
                    <div className=''>

                    </div>
                {/* FOOTER => Setting and other */}

            </div>

        );
    };

    //? Right Side view aka Displaying messages
    const messageToUser = (toUser) => {

        //> Request all messages between toUser and mainUser
        const viewMessages = async (event, toUser) => {

            if (event) {

                try {

                    const response = await fetch('', {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                        }
                    });

                    if (response.status === 400) {
                        const data = await response.json();
                        console.log("Failed to fetch messages: " + data.message);
                        //? Handle error
                    } else {
                        //? Handle success
                    }

                } catch (error) {

                    console.error('Error fetching messages: ' + error.message);

                }
            }
        };

        //> Submit messsage to user
        const sendMessage = async (event, toUser) => {

            if (event) {
                
                try {

                    const response = await fetch('', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            //TODO: complete request body points
                        }),
                    });

                    if (response.status === 400) {
                        const data = JSON.parse(response.json());
                        console.log("Failed to send message: " + data.message);
                        //? Handle error
                    } else {
                        //? Handle success
                    }

                } catch (error) {

                    console.log('Error sending message: ' + error.message);

                }

            }

        };

        //> UI
        return (
            <div className="flex flex-col justify-center items-center box-border h-screen w-2/3 p-5 shadow-md z-1"> 


                {/* Contact Box/ Profile */}
                    <div className='flex justify-center absolute top-5 right-auto w-3/5 h-16 bg-violet-500 text-white rounded-lg shadow-md backdrop-blur-xl drop-shadow-lg'>

                    </div>
                {/* Contact Box/ Profile */}


                {/* The messages */}
                    <div className='flex justify-center absolute h-4/5 w-3/5 text-white shadow-2xl bg-silver rounded-lg bg-opacity-50 backdrop-blur-xl drop-shadow-lg'>

                    </div>
                {/* The messages */}


                {/* The texting box  */}
                <div className="flex justify-center absolute bottom-5 right-auto w-3/5 h-16 bg-violet-500 text-white rounded-lg shadow-md backdrop-blur-xl drop-shadow-lg">
                    <form method="POST" action="none" className="flex-grow flex">
                        <input type="text" htmlFor="messaging" placeholder="Type message..." className="flex-grow p-2 text-black"/>
                    </form>
                    <button className="p-2">Send</button>
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
