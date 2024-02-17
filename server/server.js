const express = require('express');
const cors = require('cors');
const { spawn } = require('child_process');

const app = express();
const port = 9999;

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
    res.send('Welcome to SciSketch');
});

app.post('/generate-sketch', (req, res) => {
  return res.status(200).json({ sketch: 'https://www.sciencemag.org/sites/default/files/styles/article_main_large/public/images/cc_iStock-478639870_16x9.jpg?itok=3Z3Z3zvz' });

});

app.post('/generate-graph', (req, res) => {
    const abstract = req.body.abstract;
  
    if (!abstract) {
      return res.status(400).send('Abstract is required');
    }
  
    const pythonProcess = spawn('/usr/local/bin/python3', ['/Users/lilianli/Desktop/SciSketch/GraphicalAbstractGenerator.py', abstract]);

  
    let pythonData = "";
    let pythonError = "";
  
    pythonProcess.stdout.on('data', (data) => {
      pythonData += data.toString();
    });
  
    pythonProcess.stderr.on('data', (data) => {
      pythonError += data.toString();
    });
  
    pythonProcess.on('close', (code) => {
      if (code !== 0 || pythonError) {
        console.error(`Python script exited with code ${code}, error: ${pythonError}`);
        return res.status(500).send('Error executing Python script');
      }
  
      try {
        const graphData = JSON.parse(pythonData);
        res.status(200).json(graphData);
      } catch (error) {
        console.error('Error parsing Python script output:', error);
        res.status(500).send('Error parsing Python script output');
      }
    });
});

app.listen(port, () => {
    console.log(`Server is running on port: ${port}`);
});
