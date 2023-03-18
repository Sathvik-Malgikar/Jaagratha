
import {useState} from "react";
// import { socket } from './socket';

function CCTVGrid(){

    var url = "";

    // socket.on('connect', onConnect);
    // socket.on('disconnect', onDisconnect);
    // socket.on('welcome', onWelcomeEvent);

    function onConnect(){
        console.log("connected");
    }
    function onDisconnect(){
        console.log("disconnected");
    }
    function onWelcomeEvent(){
        console.log("welcome");
    }

    return<>
        <video controls autoPlay>
            <source src={url+"\\data\\oneid"} ></source>
        </video>
    </>


}

export default CCTVGrid;