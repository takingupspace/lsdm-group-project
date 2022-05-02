const sql = require("./db.js");

const Query = function(query){
    this.table = query.table;
    this.offset = query.offset;
}

Query.getData = (req, result) => {
    let table = req.body.table;
    let tableOffset = req.body.offset;

    sql.query(`SELECT * FROM ${table} LIMIT 20 OFFSET ${tableOffset}`, (err, res) => {
        if(err){
            console.log('error in the query model');
            return result('error in query model', null);
        }else{
            console.log('query was successful in the query model')
            return result(null, res);
        }
    })
}

module.exports = Query;