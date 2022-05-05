const Auth = require("../models/auth.model.js");
const jwt = require('jsonwebtoken')
require('dotenv').config();

exports.signUpForLSDM = (req, res) => {
    Auth.createUserForLSDM(req.body.userName, req.body.password, (err, data) => {
        if(err){
            res.send({
                message : "This user already exists!"
            })
        }else res.send({
            message : `Thank you ${req.body.userName}, you have successfully signed up!`
        });
    });
}

exports.signInForLSDM = (req, res) => {
    Auth.userLoginForLSDM(req.body.userName, req.body.password, (err, data) => {
        if(err){
            return res.send({
            message: "Passwords do not Match or no User with that name on file"
            });
            }else{

            res.cookie("jwt", data, {secure: true, httpOnly: false, maxAge : 60, SameSite: true})
            userName = req.body.userName

            return res.send({
                message: `Passwords Match ${req.body.userName}, issuing a token`,
                data : data,
                userName : userName
        });
        }
    })
}

exports.verify = (req, res, next) => {
    Auth.verifySession(req, (err, data) => {
        //console.log("req.body inside Auth controller = " + JSON.stringify(req.body));
        if(err){
            res.send({
                message : err,
                userName : req.body.userName
            })
            console.log("error before next call in verify")
            return;
        }else{
            // TODO: Add response from server to client, but it's probably going to be just passing flow to the next function with next(), right?
            //console.log("inside verify controller after verifySession Auth model has returned: session is = " + (data))
            /*try{
                
                // now we verify the token
                //payload = jwt.verify(data, process.env.ACCESS_TOKEN_SECRET)
                //console.log("payload is " + JSON.stringify(payload))
                //next()
            }catch(e){
                console.log("catch was activated")
            }
            
            res.send('success!')*/
            console.log("inside verify controller after verifySession Auth Model returns")
            next()
        }
    });
}