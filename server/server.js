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


app.post('/generate-graph', (req, res) => {
  const abstract = req.body.abstract;

  if (!abstract) {
      return res.status(400).send('Abstract is required');
  }

  const pythonProcess = spawn('/usr/local/bin/python3', ['./GraphicalabstractGenerator.py', abstract]);

  let imagePath = "";
  pythonProcess.stdout.on('data', (data) => {
      imagePath += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
      if (code !== 0) {
          console.error(`Python script exited with code ${code}`);
          return res.status(500).send('Error executing Python script');
      }

      try {
          res.status(200).send({ imagePath: imagePath.trim() });
      } catch (error) {
          console.error('Error sending graph image path:', error);
          res.status(500).send('Error sending graph image path');
      }
  });
});

app.post('/generate-sequential-array', (req, res) => {
  const protocol = req.body.protocol;
    
  if (!protocol) {
      return res.status(400).send('Protocol is required');
  }

  const pythonProcess = spawn('/usr/local/bin/python3', ['./ExperimentalProcedureGenerator.py', protocol]);

  let pythonData = '';
  pythonProcess.stdout.on('data', (data) => {
      pythonData += data.toString();
  });

  pythonProcess.on('close', (code) => {
      if (code !== 0) {
          return res.status(500).send('Error executing Python script');
      }

      try {
          const jsonData = JSON.parse(pythonData);
          console.log(jsonData);
          res.status(200).json(jsonData);
      } catch (error) {
          res.status(500).send('Error parsing Python script output');
      }
  });
});

app.listen(port, () => {
    console.log(`Server is running on port: ${port}`);
});
