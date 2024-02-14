 const mongoose = require("mongoose")

 // Connects to MongoDB associated with AJ's account
 const connectDB = async() => {
    try {
        const conn = await mongoose.connect("mongodb+srv://<ajjain27>:Stocks1@cs222.4rxjb2d.mongodb.net/?retryWrites=true&w=majority", {
            useUnifiedTopology: true,
            useNewUrlParser: true,
        })
        console.log(`MongoDB Connected: ${conn.connection.host}`)
    } catch(error) {
        console.error(`Error: ${error.message}`)
        process.exit()
    }
 }

 module.exports = connectDB
 