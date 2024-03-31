// server.js
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');
const app = express();
const db = new sqlite3.Database('./testdata.db');
// Use cors middleware to allow all origins
app.use(cors());

app.get('/predictions', (req, res) => {
    db.all('SELECT * FROM StudentPerformancePredictions', (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json(rows);
    });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});