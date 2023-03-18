import logo from './logo.svg';
import './App.css';
import CCTVGrid from './CCTVGrid';
import Login from './Login';
import { useState } from 'react';

function App() {
  const [Authorised, setAuthorised] = useState(false);

  return (
    <div className="App">
      <header className="App-header">
    
    

    <img className='absolute w-full top-0 -z-10' src={require('./bg1.jpg')} ></img>

      {
        Authorised? <></> : <img src={require('./logo1.webp')} />
      }
     

    <h1 className='Title'> Jaagratha Automatic Crime detection. </h1>

    { Authorised?   <CCTVGrid></CCTVGrid> : <Login cb={setAuthorised} ></Login>}

      </header>
    </div>
  );
}

export default App;
