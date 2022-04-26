const express = require("express");
const bodyParser = require("body-parser");
const app = express();
var cors = require('cors')
require('dotenv').config()

app.use(bodyParser.json());

app.use(cors());

// allows us to parse requests of content-type: application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
    res.send("Hello From my Server")
})

require("./server/routes/auth.routes.js")(app);

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});