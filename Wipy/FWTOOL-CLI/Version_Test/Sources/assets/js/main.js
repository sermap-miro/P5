function showCurrentDate(e) {
    now = new Date, year = now.getFullYear(), month = now.getMonth() + 1, day = now.getDate(), day < 10 && (day = "0" + day), h = now.getHours(), h < 10 && (h = "0" + h), m = now.getMinutes(), m < 10 && (m = "0" + m), s = now.getSeconds(), s < 10 && (s = "0" + s), result = day + "/" + month + "/" + year + " - " + h + ":" + m + ":" + s, document.getElementById(e).innerHTML = result, setTimeout('showCurrentDate("' + e + '");', "1000")
}
function Programme_cmd(cmd){
    var resp, xmlhttp=new XMLHttpRequest();
    xmlhttp.onreadystatechange=function() {
        if (xmlhttp.readyState==4 && xmlhttp.status==200){
            resp = xmlhttp.responseText;
            console.log(resp);
            }
    }
    xmlhttp.open("GET","Valp=" + cmd,true); xmlhttp.send()  
}
function Manuel_cmd(cmd){
    var resp, xmlhttp=new XMLHttpRequest();
    xmlhttp.onreadystatechange=function() {
        if (xmlhttp.readyState==4 && xmlhttp.status==200){
            resp = xmlhttp.responseText;
            console.log(resp);
            }
    }
    xmlhttp.open("GET","Val=" + cmd,true); xmlhttp.send()   
}
/*function Info_cmd(e){
	var resp, xmlhttp=new XMLHttpRequest();
	xmlhttp.onreadystatechange=function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			resp = xmlhttp.responseText;
			console.log(resp);
			}
	}
	xmlhttp.open("GET","Plan=" + cmd,true); xmlhttp.send()	
}*/
function Calibration_cmd(cmd){
	var resp, xmlhttp=new XMLHttpRequest();
	xmlhttp.onreadystatechange=function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			resp = xmlhttp.responseText;
			console.log(resp);
			}
	}
	xmlhttp.open("GET","Valc=" + cmd,true); xmlhttp.send()	
}
function Planning_cmd(cmd){
	var resp, xmlhttp=new XMLHttpRequest();
	xmlhttp.onreadystatechange=function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			resp = xmlhttp.responseText;
			console.log(resp);
			}
	}
	xmlhttp.open("GET","Plan=" + cmd,true); xmlhttp.send()	
}
function Send_Clock_hidden2(){
	var d = new Date();
	var hours = d.getHours();
	var mins = d.getMinutes();
	document.getElementById("h1").value = hours
	document.getElementById("m1").value = mins
    var resp, xmlhttp=new XMLHttpRequest();
	xmlhttp.onreadystatechange=function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			resp = xmlhttp.responseText;
			console.log(resp);
		}
    }
	xmlhttp.open("GET","H="+hours+":"+mins,true); 
	xmlhttp.send();
	setTimeout(Send_Clock_hidden2() => window.open('http://192.168.4.1/', '_self'), 1000);
}
$(document).ready(function() {
    showCurrentDate("now");
	Programme_cmd(cmd);
	Manuel_cmd(cmd);
	Planning_cmd(cmd);
	Calibration_cmd(cmd);
	Send_Clock_hidden2();
	/*Info_cmd(cmd)*/
});
