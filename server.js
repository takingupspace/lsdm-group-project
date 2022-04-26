const express = require("express");
const bodyParser = require("body-parser");
const app = express();
var cors = require('cors')

app.use(bodyParser.json());

app.use(cors());

app.get("/", (req, res) => {
    res.send("Hello From my Server")
})

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});