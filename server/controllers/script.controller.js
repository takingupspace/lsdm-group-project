const Script = require("../models/script.model.js")

exports.download = (req, res) => {
    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python',["./upload.py", req.body.url]);
}