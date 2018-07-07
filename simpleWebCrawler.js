// From http://www.netinstructions.com/how-to-make-a-simple-web-crawler-in-javascript-and-node-js/

var request = require('request');
var cheerio = require('cheerio');
var URL = require('url-parse');

var startURL = "http://info.cern.ch/";
var searchWord = "website";
var maxPagesToVisit = 10;

var pagesVisited = {};
var numOfPagesVisited = 0;
var pagesToVisit = [];
var url = new URL(startURL);
var baseURL = url.protocol + "//" + url.hostname;

pagesToVisit.push(startURL);
crawl();

function crawl() {
  if (numOfPagesVisited >= maxPagesToVisit) {
    console.log("Reached max limit of number of pages to visit");
    return;
  }
  var nextPage = pagesToVisit.pop();
  if (nextPage in pagesVisited) {
    // We've already visited this page, so repeat the crawl
    crawl();
  } else {
    // New page we haven't visited
    visitPage(nextPage, crawl);
  }
}

function visitPage(url, callback) {
  // Add page to our set
  pagesVisited[url] = true;
  numOfPagesVisited++;
  // Make the request
  console.log("Visiting page:", url);
  request(url, function(error, response, body) {
    // Check status code (200 is HTTP OK)
    console.log("Status code:", response.statusCode);
    if (response.statusCode !== 200) {
      callback();
      return;
    }
    // Parse the document body
    var $ = cheerio.load(body);
    var isWordFound = searchForWord($, searchWord);
    if (isWordFound) {
      console.log("Word", searchWord, "found at page", url);
    } else {
      collectInternalLinks($);
      // Our callback is just calling crawl()
      callback();
    }
  });
}

function searchForWord($, word) {
  var bodyText = $('html > body').text().toLowerCase();
  return (bodyText.indexOf(word.toLowerCase()) !== -1);
}

function collectInternalLinks($) {
  var absoluteLinks = $("a[href^='/']");
  console.log("Found", absoluteLinks.length, "absolute links on page");
  absoluteLinks.each(function() {
    pagesToVisit.push(baseURL + $(this).attr('href'));
  });
}