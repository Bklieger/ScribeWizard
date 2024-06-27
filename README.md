<h2 align="center">
 <br>
 <img src="https://i.imgur.com/scoiUgD.png" alt="Generate Organizes Notes with GroqNotes" width="150">
 <br>
 <br>
 GroqNotes: Generate organized notes from audio<br>using Groq, Whisper, and Llama3
 <br>
</h2>

<p align="center">
 <a href="https://github.com/bklieger/groqnotes/stargazers"><img src="https://img.shields.io/github/stars/bklieger/groqnotes"></a>
 <a href="https://github.com/bklieger/groqnotes/blob/main/LICENSE.md">
 <img src="https://img.shields.io/badge/License-MIT-green.svg">
 </a>
</p>

<p align="center">
 <a href="#Overview">Overview</a> •
 <a href="#Features">Features</a> •
 <a href="#Quickstart">Quickstart</a> •
 <a href="#Contributing">Contributing</a>
</p>

<br>

[Demo of GroqNotes](https://github.com/Bklieger/groqnotes/assets/62450410/9c54dab3-21ad-42d6-8504-364e0aa6acde)

> Demo of GroqNotes fast transcription of audio and generation of structured notes


## Overview

GroqNotes is a streamlit app that scaffolds the creation of structured lecture notes by iteratively structuring and generating notes from transcribed audio lectures using Groq's Whisper API. The app mixes Llama3-8b and Llama3-70b, utilizing the larger model for generating the notes structure and the faster of the two for creating the content.


### Features

- 🎧 Generate structured notes using transcribed audio by Whisper-large and text by Llama3
- ⚡ Lightning fast speed transcribing audio and generating text using Groq
- 📖 Scaffolded prompting strategically switches between Llama3-70b and Llama3-8b to balance speed and quality
- 🖊️ Markdown styling creates aesthetic notes on the streamlit app that can include tables and code 
- 📂 Allows user to download a text or PDF file with the entire notes contents

### Example Generated Notes:

| Example                                      | Youtube Link                                                                                                                                |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| [Transformers Explained by Google Cloud Tech](examples/transformers_explained/generated_notes.pdf)             |  https://www.youtube.com/watch?v=SZorAJ4I-sA                                       |
| [The Essence of Calculus by 3Blue1Brown](examples/essence_calculus/generated_notes.pdf) | https://www.youtube.com/watch?v=WUvTyaaNkzM                                            |

> As with all generative AI, content may include inaccurate or placeholder information. GroqNotes is in beta and all feedback is welcome!

---

## Quickstart

> [!IMPORTANT]
> To use GroqNotes, you can use a hosted version at [groqnotes.streamlit.app](https://groqnotes.streamlit.app) or [groqnotes.replit.app](https://groqnotes.streamlit.app).
> Alternatively, you can run GroqNotes locally with Streamlit using the quickstart instructions.


### Hosted on Streamlit:

To use GroqNotes, you can use the hosted version at [groqnotes.streamlit.app](https://groqnotes.streamlit.app)

### Hosted on Replit:

You can also use the hosted version on replit at [groqnotes.replit.app](https://groqnotes.streamlit.app)
> The project can be forked on replit here: [replit.com/@bklieger/groqnotes](https://replit.com/@bklieger/groqnotes)


### Run locally:

Alternative, you can run GroqNotes locally with streamlit.

#### Step 1
First, you can set your Groq API key in the environment variables:

~~~
export $GROQ_API_KEY = gsk_yA...
~~~

This is an optional step that allows you to skip setting the Groq API key later in the streamlit app.

#### Step 2
Next, you can set up a virtual environment and install the dependencies.

~~~
python3 -m venv venv
~~~

~~~
source venv/bin/activate
~~~

~~~
pip3 install -r requirements.txt
~~~


#### Step 3
Finally, you can run the streamlit app.

~~~
python3 -m streamlit run main.py
~~~

## Details


### Technologies

- Streamlit
- Llama3 on Groq Cloud
- Whisper-large on Groq Cloud

### Limitations

GroqNotes may generate inaccurate information or placeholder content. It should be used to generate notes for entertainment purposes only.


## Contributing

Improvements through PRs are welcome!


## One-Click Deployment

[![Deploy to RepoCloud](https://d16t0pc4846x52.cloudfront.net/deploylobe.svg)](https://repocloud.io/details/?app_id=296)


## Changelog

### v0.1.0

This release is an initial release of the application codebase. It includes the following features:

🎧 Generate structured notes using transcribed audio by Whisper-large and text by Llama3

⚡ Lightning fast speed transcribing audio and generating text using Groq

📖 Scaffolded prompting strategically switches between Llama3-70b and Llama3-8b to balance speed and quality

🖊️ Markdown styling creates aesthetic notes on the streamlit app that can include tables and code

📂 Allows user to download a text or PDF file with the entire notes contents


### Future Features:

- Create summary version of transcript, batching into sections of n characters.
- Allow upload of multiple audio files
