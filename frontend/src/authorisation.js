import axios from "axios";

let backurl ='';


function login(un,pd){
    let body = {
        "username" : un, "password" : pd
    }
    axios.post({
        method: 'post',
        url: backurl+'/login',
        data: body
    }).then((resp)=>{
        return resp.json()
    }).then((data)=>{
        console.log(data);
    })
    
}

export {login}

