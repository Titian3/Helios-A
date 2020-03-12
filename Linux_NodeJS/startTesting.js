var exec = require('child_process').execFile;

var mysql = require('mysql');

const linkDB = require('./exportToDB.js');



function sqlBuild(table, data) {

	    var mbitVal = 125000;

	    var slqBuilder =

		    "INSERT INTO " + table + "(interface_externalIp, server_id, server_name, server_location, ping_latency, download_bandwidth, upload_bandwidth)" + " VALUES ('" + data.interface.externalIp + "'," + data.server.id + ",'" + data.server.name + "','" + data.server.location + "'," + data.ping.latency + "," + (data.download.bandwidth / mbitVal) + "," + (data.upload.bandwidth / mbitVal) + ")";      

	    console.log("SQLBuilderinter: " + slqBuilder)    

	    return slqBuilder;

}



var startTest =function(serverID){

	   console.log("Starting Test to " + serverID);

	   exec('speedtest', ['-f', 'json', '-s', serverID], function(err, data) {  

		           console.log(err);

		           var results = JSON.parse(data);

		           var sqlQuery = sqlBuild("speedTest_results", results);

		           linkDB.writeToDB(sqlQuery);

		           console.log("SQLQuery: " + sqlQuery);

		           

			   });
		//RGB Status indication, Only for Tinkerboard.
	    //exec('python', ['/home/linaro/OoklaTesting/RGBStatus.py', 'blue', '5', '25'], function(err) {
		//console.log("RGB error")})

};
//Voyager Server
startTest('18822');

//startTest('2629');
