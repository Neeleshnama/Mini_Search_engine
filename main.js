function getdata() {
    var query = document.getElementById("queryfield").value
    alert(query)

    let options = {
        scriptPath: "",
        args: [query]
    }

    const { PythonShell } = require('python-shell')


    PythonShell.run('\main.py', options, (err, res) => {
        if (res) {
            document.writeln('relevant docs are: ' + res) 
        }
        if (err) {
            document.writeln('relevant docs are: ' + err) 
        }
    });
}


