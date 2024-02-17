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

    // Adjust the path to the Python script according to its location
    const pythonProcess = spawn('/usr/local/bin/python3', ['./AbstractGraphForDemo.py', abstract]);

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
            // Assuming the script prints the full path to the generated image
            // Trim the path for any leading or trailing whitespace
            imagePath = imagePath.trim();

            // Option 1: Send the image path to the client
            res.status(200).send({ imagePath });

            // Option 2: Directly send the image file to the client
            // This requires the server to have access to the file system path where the image is saved
            // res.sendFile(imagePath, { root: '.' }, (err) => {
            //     if (err) {
            //         console.error('Error sending graph image file:', err);
            //         res.status(500).send('Error sending graph image file');
            //     }
            // });
        } catch (error) {
            console.error('Error processing Python script output:', error);
            res.status(500).send('Error processing Python script output');
        }
    });
});

app.post('/generate-sequential-array', (req, res) => {
  const protocol = req.body.protocol;
    
  if (!protocol) {
      return res.status(400).send('Protocol is required');
  }

  const pythonProcess = spawn('/usr/local/bin/python3', ['./ProtocolGraphDemo.py', protocol]);

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
            imagePath = imagePath.trim();
            // Option 1: Send the image path to the client
            res.status(200).send({ imagePath });
        } catch (error) {
            console.error('Error processing Python script output:', error);
            res.status(500).send('Error processing Python script output');
        }
    });

  
});

app.listen(port, () => {
    console.log(`Server is running on port: ${port}`);
});
