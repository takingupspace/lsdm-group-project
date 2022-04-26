module.exports = app => {
    const auth = require("../controllers/auth.controller.js");
    
    app.post('/login', auth.signIn);
    
    app.post('/signup', auth.signUp);

    app.post('/verify', auth.verify);
    
    };