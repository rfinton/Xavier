var fs = require('fs');
var readline = require('readline');
var linesArray = [];
var matched = 0;

var studioExport = readline.createInterface({
  input: fs.createReadStream('xavier.studio.export.csv')
});

studioExport.on('line', function(line) {
  line = (line.replace(/[ "]/g, '')).toLowerCase();
  var l = line.split(',');
  linesArray.push({
    name: l[0] + l[1],
    purl: l[3]
  });
}).on('close', function() {
  var fallApps = readline.createInterface({
    input: fs.createReadStream('FALL 2018 APPS AS OF 09-06-17.csv')
  });

  fallApps.on('line', function(line) {
    line = (line.replace(/ /g, '')).toLowerCase();
    var l = line.split(',');
    var firstname = l[1];
    var lastname = l[3];
    var fn = l[1] + l[3];
    
    for(j in linesArray) {
      if(fn == linesArray[j].name) {
        ++matched;
        console.log('Matched: ' + linesArray[j].purl);
      }
    }
  }).on('close', function() {
    console.log('Total Matched: ' + matched);
  });
});