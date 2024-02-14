const asyncHandler = require('express-async-handler')
const User = require("../models/userModel")

// Registers user with DB from user input request
const registerUser = asyncHandler(async (req, res) => {
    const {name, email, password} = req.body;

    const userExists = await User.findOne({email});

    // Registering with email that already has account
    if (userExists) {
        res.status(404);
        throw new Error("Account with Email Already Exists");
    }

    const user = await User.create({
        name,
        email,
        password,
    });

    if (user) {
        res.status(201).json({
            // creates unique user id
            _id: user._id,
            name: user.name,
            email: user.email,
        });
    }
});

// Logs user in with DB from user input request
const loginUser = asyncHandler(async (req, res) => {
    const {email, password} = req.body;

    const user = await User.findOne({email});

    // Checks that entered password matches one in DB
    if (user && (await user.passwordCorrect(password))) {
        res.json({
            _id: user._id,
            name: user.name,
            email: user.email,
        });
    } else {
        res.status(401);
        throw new Error("Email or Password is Invalid");
    }
});

module.exports={registerUser, loginUser}