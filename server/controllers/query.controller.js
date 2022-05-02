const Query = require('../models/query.model.js');

exports.getData = (req, res) => {
    Query.getData(req, (err, data) => {
        if(err){
            res.send({
                data : "Some Error on Server Side"
            });
        }else{
            res.send({
                data : data
            })
        }
    })
}