const sql = require("./db.js");

const Query = function(query){
    this.table = query.table;
    this.offset = query.offset;
}

Query.getData = (req, result) => {
    let table = req.body.table;
    let tableOffset = req.body.offset;
    console.log("req.body.secondTable = " + req.body.secondTable)
    console.log("req.body.firstTable " + req.body.table)

    if(req.body.table === "word_count_analysis"){

    sql.query(`SELECT * FROM ${table} LIMIT 20 OFFSET ${tableOffset}`, (err, res) => {
        if(err){
            console.log('error in the query model');
            return result('error in query model', null);
        }else{
            console.log('query was successful in the query model')
            return result(null, res);
        }
    })
 }else{
     sql.query(`SELECT od.row_id as original_row_id, od.sentiment_score as original_sentiment,
     sa.sentiment_score as our_analysis_sentiment_score
     FROM original_dataset od INNER JOIN sentiment_analysis sa ON
     od.row_id = sa.row_id LIMIT 20 OFFSET ${tableOffset}`, (err, res) => {
         if(err){
             console.log('error in the query model');
             return result('error in query model', null);
         }else{
             console.log('query was successful in the query model')
             return result(null, res);
         }
     })
 }
}

module.exports = Query;