import React from 'react';
import Home_page from './Home_page';
import "./App.css";
import LoginPage from './login'; // import the login component
import WebPage from './WebPage'

const MongoClient = require('mongodb').MongoClient;

const url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  console.log("Database connected!");
  db.close();
});

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mydb");
  console.log("Database created!");
  db.close();
});

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mydb");
  dbo.createCollection("customers", function(err, res) {
    if (err) throw err;
    console.log("Collection created!");
    db.close();
  });
});

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mydb");
  var myobj = { name: "Company Inc", address: "Highway 37" };
  dbo.collection("customers").insertOne(myobj, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
});



//home page works!
function App() {
    return (
      <div className="App">
        {/* <Home_page /> */}
        <WebPage />
        <header className="App-header"> </header>
      </div>
    );
  }




export default App;
