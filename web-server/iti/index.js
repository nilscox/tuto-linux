const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');
var pug = require('pug');

const names = [
  'friend',
  'love',
  'bro',
  'dude',
  'wassup?'
];

const render = pug.compileFile('index.pug');

function randomName() {
  return names[parseInt(Math.random() * names.length)];
}

function static(uri) {
  const filename = path.join(process.cwd(), uri);

  if (!fs.existsSync(filename) || fs.statSync(filename).isDirectory())
    return null;

  return fs.readFileSync(filename, 'binary');
}

const server = http.createServer(function(req, res) {
  const reqUrl = url.parse(req.url);
  const file = static('/static' + reqUrl.pathname);

  if (file) {
    res.writeHead(200);
    res.end(file, 'binary');
  } else {
    var name = new RegExp('name=([^\/]+)').exec(reqUrl.query);

    if (name)
      name = name[1];
    else
      name = randomName();

    if (name.length > 12)
      name = 'long name';

    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end(render({ name: name }));
  }
});

server.listen(process.env.PORT);
