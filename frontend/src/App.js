import logo from './logo.svg';
import './App.css';
import CCTVGrid from './CCTVGrid';
import Login from './Login';
import Report from './Report';
import { useState } from 'react';

function App() {
  const [Authorised, setAuthorised] = useState(false);
  const [hidden, setHidden] = useState(true);
  
  function hidhandler (){
    setHidden(false);
  }
  function hidhandler2 (){
    setHidden(true);
  }

 

  const desc= "	This website captures the real-time images given by the CCTV's which will be used for detecting any crime happening in the surrounding areas.Received information shall be regarded as sufficient to suspect and immediate step would be to send th troops to the suspected area after verifying the feed. By this the troops get to know about the crime happening and can take the disciplinery actions towards the criminal.This website makes the government work more efficiently  and reduce the time needed by the troops to entrap the bandit by following the other CCTV feed located nearby.";
  return (
    <div className="App">
      <header className="App-header">
    
    
    <img className='absolute w-full top-0 -z-10' src={require('./bg1.jpg')} ></img>

      {
        Authorised? <>

    
        <div>
          <p onMouseEnter={hidhandler} onMouseLeave={hidhandler2} className='text-md p-4'>
       {  hidden ? "Know more" : desc}
          </p>
        </div> <br></br>
        
        </> : <img src={require('./logo1.webp')} />
      }
     

    <h1 className='Title'> Jaagratha Automatic Crime detection. </h1> 

    { Authorised?   <CCTVGrid></CCTVGrid> : <Login cb={setAuthorised} ></Login>}
    

      </header>
    </div>
  );
}

export default App;
