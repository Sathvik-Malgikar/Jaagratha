
let backurl ='http://172.16.128.215:5000';


function login(un,pd){
    let body = {
        "user" : un, "pass" : pd
    }
    // axios.post({
    //     "method": 'post',
    //     "url": 'http://172.16.128.215:5000/auth',
    //     "data": body
    // }).then((resp)=>{
    //     return resp.json()
    // }).then((data)=>{
    //     console.log(data);
    // })

   return postData(backurl+"/auth" , body).then((data)=>{
        console.log(data);
        if(data==1)
        return true
        else return false
    })

    // fetch('http://172.16.128.215:5000/auth', {
    //     method: 'POST',
    //     headers: {
    //       Accept: 'application.json',
    //       'Content-Type': 'application/json'
    //     },
    //     Body: body,
    //     Cache: 'default'
    //   }).then((resp)=>{
    //         return resp.json()
    //     }).then((data)=>{
    //         console.log(data);
    //     })
    
}

async function postData(url, data ) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: "POST", // *GET, POST, PUT, DELETE, etc.
      mode: "cors", // no-cors, *cors, same-origin
      cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      credentials: "same-origin", // include, *same-origin, omit
      headers: {
        "Content-Type": "application/json",
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: "follow", // manual, *follow, error
      referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify(data), // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }

export {login}

