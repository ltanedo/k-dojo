// index.js (node example)

const { createClient } = require("@deepgram/sdk");
const fs = require("fs");

const transcribeFile = async () => {
  // STEP 1: Create a Deepgram client using the API key
//   const deepgram = createClient(process.env.DEEPGRAM_API_KEY);

  const deepgram = createClient("0a9f88c6622e5f95e4f39512e21003aab4669bb8");

  // STEP 2: Call the transcribeFile method with the audio payload and options
  const { result, error } = await deepgram.listen.prerecorded.transcribeFile(
    // path to the audio file
    fs.readFileSync("src/chinese.mp3"),
    // STEP 3: Configure Deepgram options for audio analysis
    {
      model: "nova-2",
      smart_format: true,
    }
  );

  if (error) throw error;
  // STEP 4: Print the results
  if (!error) console.dir(result, { depth: null });
};

transcribeFile();
