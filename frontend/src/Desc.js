
import {useState} from "react";
// import { socket } from './socket';

function Desc(){

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

   

    const [feedArr, setfeedArr] = useState(["http://172.16.128.215:5000/feed","http://172.16.128.215:5000/feed","http://172.16.128.215:5000/feed","http://172.16.128.215:5000/feed"])
    

    return<div className="grid grid-cols-2 gap-8">
    
    {feedArr.map((e,i) =>{
return (<div className="border-red rounded-lg overflow-clip border-4" key={i}>
    

       <img className='w-50' src={e}  ></img>
   

</div>)
    })}
    </div>
// return <div className="p-10 w-100 h-100 bg-red z-10 text-red" >
// <img className='w-50' src={"http://172.16.128.215:5000/feed"}  ></img>
// </div>


}

export default Desc;