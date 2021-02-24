function disableScroll() { 
  document.body.classList.add("stop-scrolling"); 
} 


function enableScroll() { 
  document.body.classList.remove("stop-scrolling"); 
} 



function checkempty(idElement, em, mess) {
    name1 = document.querySelector(idElement);
     if(name1.value == null || name1.value == ''){
         document.querySelector(em).innerHTML = 'enter a ' + mess;
         document.querySelector(em).style.display = 'initial';
         return false;
     }
     else{
         document.querySelector(em).innerHTML = '';
         document.querySelector(em).style.display = 'none';
         return true;
     }
}



function checklogin(){
  var user = checkempty('#lusername', '#emessage0', 'username');
  var pass = checkempty('#lpass', '#emessage', 'password');
  if(user && pass)
  {
    return true;
  }
  else{
    return false;
  }
}


function checkpass(idElement, em)
{
  var flag = 0;
  var pass = document.querySelector(idElement);
  var length = pass.value.length;
  document.querySelector(em).innerHTML = '';
  console.log('hered');

  if(!checkempty('#password', '#ep', 'password'))
  { 
    flag = 1;
  }
  else if(length <6){
    flag = 1;
    document.querySelector('#ep').innerHTML += 'min length should be 6';
    document.querySelector(em).style.display = 'initial';
  }
  if(!pass.value.match(/[0-9]/g)){
    flag = 1;
    document.querySelector('#ep').innerHTML += ', atleast one number';
    document.querySelector(em).style.display = 'initial';
  }
  if(!pass.value.match(/[A-Z]/g)){
    flag = 1;
    document.querySelector('#ep').innerHTML += ', atleast one Captial Letter';
    document.querySelector(em).style.display = 'initial';
  }
  if(!pass.value.match(/[a-z]/g)){
    flag = 1;
    document.querySelector('#ep').innerHTML += ', atleast one lower letter';
    document.querySelector(em).style.display = 'initial';
  }

  if(flag == 1)
  {
    return false;
  }
  else{
    document.querySelector(em).innerHTML = '';
    document.querySelector(em).style.display = 'none';
    return true;
  }

}


function checkpassmatch(idElement, idElement1, em)
{
  var flag = 0;
  if(checkempty(idElement1, em, 'confirm password'))
  {
    if(document.querySelector(idElement).value != document.querySelector(idElement1).value)
    {
      flag = 1;
      document.querySelector(em).style.display = 'initial';
      document.querySelector(em).innerHTML = "passwords don't match!";
      return false;
    }
    else{
      flag = 0;
      document.querySelector(em).innerHTML = '';
      document.querySelector(em).style.display = 'none';
      return true;

    }
  }
  else{
    return false;
  }
}

function checkemail(idElement, em){
  var flag = 1;
  var email = document.querySelector(idElement)
  if(checkempty(idElement, em, 'email'))
  {
    var mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if(!email.value.match(mailformat)){
      document.querySelector(em).style.display = 'initial';
      document.querySelector(em).innerHTML = "not a valid email";
      return false;
    }
    else{
      document.querySelector(em).innerHTML = '';
      document.querySelector(em).style.display = 'none';
      return true;
    }
  }
  else{
    return false;
  }
}


function checkreg(){
  var user = checkempty('#rusername', '#eu', 'username');
  var pass = checkpass('#password', '#ep');
  var email = checkemail('#emailr','#ee');
  var cpass = checkpassmatch('#password','#cpassword','#ecp');

  if(user && pass && email && cpass)
  {
    return true;
  }
  else{
    return false;
  }
}

function checkclick(){
  var check1 = document.querySelector('#userloc');
  if(check1.checked){
    document.querySelector('#longi').style.display = 'initial';
    document.querySelector('#lati').style.display = 'initial';
  }
  else
  {
    document.querySelector('#lati').style.display = 'none';
    document.querySelector('#longi').style.display = 'none';
  }
}

document.addEventListener('DOMContentLoaded', function(){


      // login and registration form modal
        document.querySelectorAll(".blogin").forEach(a => {
          a.onclick = function(){
              document.querySelector(".bg-modal").style.display = "flex";
              disableScroll();
          };
      });


      document.querySelector(".closelogin").onclick = function(){
          document.querySelector(".bg-modal").style.display = "none";
          enableScroll();
      };




      document.querySelectorAll(".signup").forEach(a => {
        a.onclick = function(){
            document.querySelector(".bg-modal-r").style.display = "flex";
            disableScroll();
        };
      });

      document.querySelectorAll(".newcomplain").forEach(a => {
        a.onclick = function(){
            document.querySelector(".bg-modal-n").style.display = "flex";
            disableScroll();
        };
      });


    document.querySelectorAll(".closereg").forEach(a => {
        a.onclick = ()=>
        {
            document.querySelector(".bg-modal-r").style.display = "none";
            enableScroll();
        }
    })

    document.querySelectorAll(".closenew").forEach(a => {
      a.onclick = ()=>
      {
          document.querySelector(".bg-modal-n").style.display = "none";
          enableScroll();
      }
  })


    document.querySelector(".rl").onclick = function(){
      document.querySelector(".bg-modal-r").style.display = "none";
      document.querySelector(".bg-modal").style.display = "flex";
  }

  document.querySelector(".lr").onclick = function(){
      document.querySelector(".bg-modal-r").style.display = "flex";
      document.querySelector(".bg-modal").style.display = "none";
  }

});