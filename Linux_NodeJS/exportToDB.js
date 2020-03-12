var mysql = require('mysql');

const dbInfo = {
    host: "host",
    user: "user",
    password: "password",
    database: "database"
  }
  
  exports.writeToDB = function writeToDB(sql) {
      console.log("CONNECTING TO DB: " + dbInfo.database + "... ");
  
      var con = mysql.createConnection(dbInfo);
  
      con.connect(function(err) {
        if (err) throw err;
        console.log("Connected!");
        console.log(sql);
        con.query(sql, function (err, result) {
          if (err) throw err;
          console.log("1 record inserted");
          con.end();
        });
      });
  }