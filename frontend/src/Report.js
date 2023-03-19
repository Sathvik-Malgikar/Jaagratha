import {React, useState} from 'react';


function Report(){

    var [imgurls, setImgurls] = useState([]);
    var url = "172.16.128.215:5000/Reports"
    //fetch
    fetch(url, {method: "GET"})
        .then((resp)=>{
                return resp.json()
            })
        .then((data)=>{
                console.log(data);
                setImgurls(data);
            })
    //   url

    return(
        <div className='grid align-center border-4'>
        {
            imgurls.map((imgurl)=>{
                <img key={imgurl} src={imgurl} alt="report"></img>
            })
        }
        </div>
    )
}

export default Report;