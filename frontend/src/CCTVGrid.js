
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
    function raisealert(){
    
    }
   

    const [feedArr, setfeedArr] = useState(["http://172.16.128.215:5000/feed?id=0","http://172.16.128.215:5000/feed?id=1","http://172.16.128.215:5000/feed?id=2"])
    

    return<div className="grid grid-cols-2 gap-8">
    
    {feedArr.map((e,i) =>{
return (<div className="border-red rounded-lg overflow-clip border-4 " key={i}>
    
{/* <div className='Button z-
10  ' onClick={raisealert}>Notify troops !</div> */}


       <img className='w-50' src={e}  ></img>

   

</div>)
    })}
    </div>
// return <div className="p-10 w-100 h-100 bg-red z-10 text-red" >
// <img className='w-50' src={"http://172.16.128.215:5000/feed"}  ></img>
// </div>


}

export default CCTVGrid;