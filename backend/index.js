const express = require('express');  
const http = require('http');  

const hostname = 'localhost';  
const port = 8080;  

const app = express();  

// Serve static files from the 'public' directory  
app.use(express.static('backend'));  

app.get('/', (req, res) => {  
    res.sendFile(__dirname + '/index.html'); // Serve the HTML file  
});  

const sample_server = http.createServer(app);  

sample_server.listen(port, hostname, () => {  
    console.log(`Server running at http://${hostname}:${port}/`);  
});