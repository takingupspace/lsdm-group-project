const express = require("express");
const bodyParser = require("body-parser");
const app = express();
var cors = require('cors')
const path = require('path');
require('dotenv').config()

app.use(bodyParser.json());

app.use(cors());

// allows us to parse requests of content-type: application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, "..", "lsdm-group-project/views")));
app.set("view engine", "ejs");
app.set("signin", path.join(__dirname, "signin"));

app.get("/", (req, res) => {
    return res.render("signin.html");
  });

require("./server/routes/auth.routes.js")(app);

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});