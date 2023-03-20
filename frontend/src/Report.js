import {React, useState,useEffect} from 'react';
import "./rep.css";

function Report({reportspage}){

    var [imgurls, setImgurls] = useState([]);
    var url = "http://172.16.128.215:5000/Reports"
    
    useEffect(()=>{
        fetch(url, {method: "GET"})
        .then((resp)=>{
                return resp.json()
            })
        .then((data)=>{
                console.log(data);
                setImgurls(data);
            })
    },[])

    
    //   url

    return(<>
        
        <div className='Button z-
    10 ' onClick={reportspage}>View Grid</div>;
        <div id="repcont" className='grid align-center border-4 grid-cols-2 gap-20 bg-[#0000bb] '>
        {
            imgurls.map((imgurl,i)=>{
              return  <div className='rounded border-white overflow-clip hover:scale-105 duration-300 ease-linear transition-all ' >
              <img key={i} src={imgurl} alt="report"></img>
              </div>
            })
        }
        </div>
    </>
    )
}

export default Report;