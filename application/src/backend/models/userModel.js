const mongoose = require("mongoose")

const userSchema = mongoose.Schema(
    {
        name: {
            type: String,
            required: true,
        },
        email: {
            type: String,
            required: true,
            unique: true,
        },
        password: {
            type: String,
            required: true,
        },
    },
);

// compares entered password versus one existing in database
userSchema.methods.passwordCorrect = async function (enteredPassword) {
    return (enteredPassword === this.password);
};

const User = mongoose.model("User", userSchema);

module.exports = User;