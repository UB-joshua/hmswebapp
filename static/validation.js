function validateUserName(){
    var name=document.forms['registrationform']['username'].value;

    if(name==''){
        document.getElementById("username").style.border="2px solid red";
        return false;
    }

    else{
        document.getElementById("username").style.border="2px solid green";
        return true;

    }

}


function validatePassword(){
    var name=document.forms['registrationform']['password'].value;

    if(name==''){
        document.getElementById("password").style.border="2px solid red";
        return false;
    }

    else{
        document.getElementById("password").style.border="2px solid green";
        return true;

    }

}


function mobile(){
    var name=document.forms['registrationform']['mobile'].value;

    if(name==''){
        document.getElementById("mobile").style.border="2px solid red";
        return false;
    }

    else{
        document.getElementById("mobile").style.border="2px solid green";
        return true;

    }

}


function validateloginuser(){
    var login=document.forms["loginform"]["vusername"].value;

    if(login==''){
        document.getElementById("vusername").style.border="2px solid red";
        return false;
    }

    else{
        document.getElementById("vusername").style.border="2px solid green";
        return true;
    }

}


function validateloginpassword(){
    var login=document.forms["loginform"]["vpassword"].value;

    if(login==''){
        document.getElementById("vpassword").style.border="2px solid red";
        return false;
    }

    else{
        document.getElementById("vpassword").style.border="2px solid green";
        return true;
    }

}


function validate_patientname(){
    var name=document.forms['bookingform']['patientname'].value;

    if(name==''){
        document.getElementById("patientname").style.border="2px solid red";
        return false;
    }

    else{
        document.getElementById("patientname").style.border="2px solid green";
        return true;

    }

}

function validate_patientage(){
    var name=document.forms['bookingform']['patientage'].value;

    if(name==''){
        document.getElementById("patientage").style.border="2px solid red";
        return false;
    }

    else{
        document.getElementById("patientage").style.border="2px solid green";
        return true;

    }

}

function validate_disease(){
    var name=document.forms['bookingform']['disease'].value;

    if(name==''){
        document.getElementById("disease").style.border="2px solid red";
        return false;
    }

    else{
        document.getElementById("disease").style.border="2px solid green";
        return true;

    }

}


function check_phone(){
    var name=document.forms['bookingform']['phone'].value;

    if(name==''){
        document.getElementById("phone").style.border="2px solid red";
        return false;
    }

    else{
        document.getElementById("phone").style.border="2px solid green";
        return true;

    }

}





function validate_appointment(){
    var name=document.forms['bookingform']['date'].value;

    if(name==''){
        document.getElementById("date").style.border="2px solid red";
        return false;
    }

    else{
        document.getElementById("date").style.border="2px solid green";
        return true;

    }

}

function validate_detailsform(){
    var name=document.forms['detailsform']['patient_name'].value;

    if(name==''){
        document.getElementById("patient_name").style.border="2px solid red";
        return false;
    }

    else{
        document.getElementById("patient_name").style.border="2px solid green";
        return true;

    }

}

function checkdetailsform(){
    if(validate_detailsform()){
        return true;
    }
    else{
        return false;
    }
}














function validatecredentials(){
    if(validateloginuser() & validateloginpassword() ){
        return true;
    }
    else{
        return false;
    }
}



function validateall(){
    if(validateUserName() & validatePassword() & mobile()){
        return true;
    }
    else{
        return false;
    }
}

function validations(){
    if(validate_patientname() & validate_patientage() & validate_disease() & validate_appointment() & check_phone() ){
        return true;
    }
    else{
        return false;
    }
}