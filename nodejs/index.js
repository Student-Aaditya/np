const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

app.get('/', async (req, res) => {
  try {
    const response = await axios.post('http://flask-api-np-l69s.onrender.com//predict', {
      name: 'Aaditya'
    });

    res.send(`Python says: ${response.data.message}`);
  } catch (error) {
    res.status(500).send('Error contacting Python service');
  }
});

app.listen(3000, () => {
  console.log('Node.js server running on http://localhost:3000');
});
