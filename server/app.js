var express = require('express')
var app = express()

// respond with "hello world" when a GET request is made to the homepage
app.get('/solveTsp', function (req, res) {
    var spawn = require("child_process").spawn; 

    var process = spawn('python',["./test.py"] ); 
  
    process.stdout.on('data', function(data) {
        res.send(data.toString());
    }) 

})

app.use(function(req, res, next) {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Allow-Methods", "*");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type,Accept");
    next();
});

app.listen(3000, function() { 
    console.log('server running on port 3000'); 
} ) 