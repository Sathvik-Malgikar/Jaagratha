
// import {useState} from "react";
import {login} from "./authorisation";

function Login({cb}){

    var url = "";

    function loginhandle(){
        login()
            cb(true);
    }

    return<>
      
      <h2>Login using the credentials to get access to control Panel.</h2>
      
        <form>
          <input className="Input" type="text" name="username" placeholder="username" />
          <input className="Input" type="password" name="password" placeholder="password" />
          <button className="Button"  type="button" onClick={loginhandle}>Login</button>
        </form>

    </>


}

export default Login;