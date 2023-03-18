
import {useState} from "react";
// import { socket } from './socket';

function CCTVGrid(){

    var url = "172.16.128.215:5000";

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
       <img className='w-50' src={url +"/feed"}  ></img>
    </>


}

export default CCTVGrid;