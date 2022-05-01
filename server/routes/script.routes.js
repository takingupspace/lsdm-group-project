module.exports = app => {
    const script = require("../controllers/script.controller.js");
    
    app.post('/download', script.download);
    
    };