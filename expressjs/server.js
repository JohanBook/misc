/* Express server for single page app.
 * It forwads all trafic except for 
 * landing page to an external api.
 */

const express = require("express");                                                                                                                                           
const logger = require("morgan");
const request = require("request");
const app = express();

app.use(logger("combined"));

app.use(express.static("build"));

/* Forward api requests to api */
app.route("/*").all(function(req, res) {
  const url = "http://api:5000" + req.url;
  req.pipe(request(url)).pipe(res);
});

/* Serve web page */
app.get("/", function(req, res) {
  res.sendFile("index.html");
});

app.listen(process.env.PORT || 8080);
