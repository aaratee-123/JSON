var a=require("readline-sync");
var fs=require("fs");
const { PassThrough } = require("stream");
const { userInfo } = require("os");
enter=a.question("Do you have Gmail account yes or no:(y/n)")
if (enter=="n"){
    user_name=a.question("enter the user name")
    console.log("for the password length is 8 1)capital letter(A-Z)\n 2)small letter(a-z)\n 3)number(0-9)\n 4)special character(@#$%^&*)")
    password=a.question("enter the password")
    confirm_password=a.question("enter the confirm password")
    if (password==confirm_password){
        console.log("confirm password is currect")
    var regexEmail = "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$";
    if (user_name.match(regexEmail)||password.match(regexEmail)){
        console.log("user name and password is matched")
        var first_name=a.question("enter the  first name")
        var last_name=a.question("enter the last name")
        var date_of_birth=a.question("enter the date of birth")
        var choose=a.question("enter the gender")
   
        object={user_info:{
                User_name:user_name,Password:password},Profile:{Name:first_name,Last_name:last_name,DOB:date_of_birth,Choose:choose}

        }
        var myJSON = JSON.stringify(object); 
        write=fs.appendFileSync(user_name+".json",myJSON, null,5,)
        console.log("congratulation you have create a/c")
        
    }
    }
                                       
}else{
    user_name=a.question("enter the user name")
    password=a.question("enter the password")
    var fs=require("fs")
    read=fs.readFileSync(user_name+".json")
    const mydata=JSON.parse(read)
    for (i in mydata){
        for(j in mydata[i]){
            if (mydata[i][j]==user_name || mydata[i][j]==password)
                console.log("you have login successful",user_name,password)
        }
        
    }
}
