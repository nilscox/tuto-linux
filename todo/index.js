const express = require('express');
const bodyParser = require('body-parser');
const pg = require('pg');

const pgconfig = {
  user: 'postgres',
  password: '',
  database: 'todo',
  host: 'localhost',
  port: 5432,
  max: 10,
  idleTimeoutMillis: 30000,
};

const app = express();
const pool = new pg.Pool(pgconfig);

app.use(bodyParser.urlencoded());
app.use(bodyParser.json());

app.post('/add', (req, res) => {
  const text = req.body.text;
  const query = 'INSERT INTO todos(text) VALUES($1)';
  pool.query(query, [text], (err, result) => {
    if (err)
      res.status(500).json(err);
    else
      res.redirect('/');
  });
});

app.get('/remove/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const query = 'DELETE FROM todos WHERE id = $1';
  pool.query(query, [id], (err, result) => {
    if (err)
      res.status(500).json(err);
    else
      res.redirect('/');
  });
});

app.get('/', (req, res) => {
  const query = 'SELECT * FROM todos';
  pool.query(query, [], (err, result) => {
    if (err)
      res.status(500).json(err);
    else
      res.render('index.twig', { todos: result.rows });
  });
});

app.use(express.static('public'));

console.log('server started on port 4242...');
app.listen(4242);
