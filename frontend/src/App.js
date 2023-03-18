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
    
    <h1 className='Title'> Jaagratha Automatic Crime detection. </h1>

    { Authorised?   <CCTVGrid></CCTVGrid> : <Login cb={setAuthorised} ></Login>}

      </header>
    </div>
  );
}

export default App;
