const sql = require("./db.js");
const bcrypt = require('bcrypt');
const rounds = 10
const jwt = require('jsonwebtoken');
require('dotenv').config();

const Auth = function(auth){
    this.userName = auth.userName;
    this.password = auth.password;
};
Auth.verifySession = (req, result) => {
    let checkAccessToken = req.body.userName;
    // console.log("checkAccessToken in Auth Model = " + checkAccessToken);
    sql.query(`SELECT session_token from admin_accounts c WHERE c.user_name = '${checkAccessToken}'`, (err, res) => {
        //console.log(`isAdmin in verifySession model = ` + res[0].isAdmin);
        if(res[0] == null) return result("This user doesn't exist!", null)
        if(res[0].session_token == null){
            return result("There is no session for this user or the user does not exist", null)
        }else{
            console.log(res[0].session_token)
            return result(null, res[0].session_token)
        }
    })
}

Auth.createUserForLSDM = (userName, password, result) => {
    bcrypt.hash(password, rounds, (error, hash) => {
        if (error) result(null, error)
        else {
            sql.query(`INSERT INTO admin_accounts (user_name, password) VALUES ('${userName}', '${hash}')`, (err, res) => {
                if(err){
                    console.log("This user already exists!");
                    result("This user already exists!", null);
                    return;
                }
                console.log("User entered into the admin_accounts table")
                result(null, res);
        });
    }
});

};

Auth.userLoginForLSDM = (userName, password, result) => {
    sql.query(`SELECT user_name, password from admin_accounts c WHERE c.user_name = '${userName}'`, (err, res) => {
        if(err){
            console.log("error" + err);
            result(err, null);
            return
        }

        if(res[0] == null){
            return result("There is no user in the database with these credentials", null)
        }
        bcrypt.hash(password, rounds, (error, hash) => {
            if (error) result(null, error)

        const match = bcrypt.compareSync(password, res[0].password)
        if(match){
            console.log("Passwords match, issuing a token")
           
            let payload = {userName : userName}
            let accessToken = jwt.sign(payload, process.env.ACCESS_TOKEN_SECRET, {
                algorithm: "HS256",
                expiresIn: process.env.ACCESS_TOKEN_LIFE
            })
            let refreshToken = jwt.sign(payload, process.env.REFRESH_TOKEN_SECRET, {
                algorithm: "HS256",
                expiresIn: process.env.REFRESH_TOKEN_LIFE
            })
            console.log("access token is = " + accessToken)
            sql.query(`UPDATE admin_accounts c SET session_token = '${accessToken}' WHERE c.user_name ='${userName}'`, (err, res) => {
                if(err){
                    console.log("error: couldn't add cookie to DB", err)
                }else{
                    console.log("cookie successfully added to DB")
                }
            })
            console.log('res for inserting new token into DB in userLogin model is ', res);
            result(null, res[0]);
        }else{
            console.log('passwords did not match')
            result("passwords do not match", null)
        }
        
    })
})
}

module.exports = Auth;