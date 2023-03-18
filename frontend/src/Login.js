
// import {useState} from "react";
import {login} from "./authorisation";

function Login({cb}){

    var url = "";

    async function loginhandle(e){
        e.preventDefault()
        
        let result = await login(e.target.elements.username.value,e.target.elements.password.value)
        console.log(result,"he");
        if(result)
            cb(true);
            else{
                console.log("incorrect credentials!");
            }
    }

    return<>
      
      <h2>Login using the credentials to get access to control Panel.</h2>
      
        <form onSubmit={loginhandle}>
          <input className="Input" type="text" name="username" placeholder="username" />
          <input className="Input" type="password" name="password" placeholder="password" />
          <button className="Button"  type="submit" >Login</button>
        </form>

    </>


}

export default Login;