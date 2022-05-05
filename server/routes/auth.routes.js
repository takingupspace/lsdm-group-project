module.exports = app => {
    const auth = require("../controllers/auth.controller.js");
    
    app.post('/loginForLSDM', auth.signInForLSDM);
    
    app.post('/signupForLSDM', auth.signUpForLSDM);

    app.post('/verify', auth.verify);
    
    };