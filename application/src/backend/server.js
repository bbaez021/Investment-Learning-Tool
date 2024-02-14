const express = require("express")
const stocks = require("./data/stocks")
const dotenv = require('dotenv')
const connectDB = require("./config/db")
const userRoutes = require("./routes/userRoutes") 

const app = express();
dotenv.config();
 // Connects to MongoDB associated with AJ's account
connectDB();
app.use(express.json())

app.get('/', (req, res) => {
    res.send("API Is running");
});

 // Sends data from data folder
app.get('/stocks', (req, res) => {
    res.json(stocks);
});

// Connects server with users endpoints for login and register
app.use('/users', userRoutes)

// Keeps server active on PORT 5000
app.listen(5000, console.log("Server connected"));
