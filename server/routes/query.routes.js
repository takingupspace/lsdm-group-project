module.exports = app => {
    const query = require("../controllers/query.controller.js");
    
    app.post('/getData', query.getData);
    
    };