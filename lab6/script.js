document.getElementById("outputButton").addEventListener("click" , function (){
    xhr = new XMLHttpRequest();
    xhr.open('GET', 'cgi-bin/output.py');
    xhr.send();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                container = document.getElementById("outputTableDiv");
                table = xhr.response
                container.innerHTML = table
            }
        }
    };
})