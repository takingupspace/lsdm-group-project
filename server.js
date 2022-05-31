const express = require("express");
const bodyParser = require("body-parser");
const app = express();
var cors = require('cors')
const path = require('path');
require('dotenv').config()
const engine = require('ejs');
const router = express.Router();

app.use(bodyParser.json());

app.use(cors({credentials: true, origin: true}));

// allows us to parse requests of content-type: application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

// this will allow us to render the file named index.html in our views directory
app.use(express.static(path.join(__dirname, "/views")));
app.set("view engine", "ejs");

require("./server/routes/auth.routes.js")(app);
require("./server/routes/query.routes")(app);

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});