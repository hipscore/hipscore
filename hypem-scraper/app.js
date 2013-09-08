var express = require('express')
, jsdom = require('jsdom')
, request = require('request')
, url = require('url')
, http = require('http')
, constants = require("./constants")
, path = require('path');

var app = express();

app.configure(function(){
    app.set('port', process.env.PORT || 3000);
    app.use(express.favicon());
    app.use(express.logger('dev'));
    app.use(express.bodyParser());
    app.use(express.methodOverride());
    app.use(express.static(path.join(__dirname, 'public')));
});

app.configure('development', function(){
    app.use(express.errorHandler());
});

app.get("/",function(req,res) {
    res.end("dobby not so smart");
});

app.get('/popular/:week?/', function(req, res) {
    var endpoint = "http://hypem.com/popular/";
    if (req.params.week) { endpoint+="week:"+req.params.week }
    endpoint+="?ax=1";

    request({uri: endpoint}, function(err, response, body){
        var self = this;
        if(err && response.statusCode !== 200){console.log('Request error.');}

	jsdom.env({
            html: body,
            scripts: [constants.APP_DOMAIN+'/javascripts/jquery-1.6.min.js']
        }, function(err, window) {
            res.writeHead(200, { 'Content-Type': 'application/json' });
            var $ = window.jQuery;
	    
	    var trackData = JSON.parse($('#displayList-data').html());	    
	    trackData['cookie'] = response.headers["set-cookie"];
	    res.end(JSON.stringify(trackData));
	});
    });
});

http.createServer(app).listen(app.get('port'), function(){
    console.log("Express server listening on port " + app.get('port'));
});
