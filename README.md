![License](https://img.shields.io/badge/license-MIT-green)

# Groqnotes: Generate organized notes from audio using Groq, Whisper, and Llama3

Groqnotes is a streamlit app that scaffolds the creation of structured lecture notes by iteratively parsing and generating notes from transcribed audio lectures using Groq's Whisper API. The app mixes Llama3-8b and Llama3-70b, utilizing the larger model for generating the notes structure and the faster of the two for creating the content.

[Demo of Groqnotes](https://github.com/Bklieger/groqnotes/assets/62450410/9c54dab3-21ad-42d6-8504-364e0aa6acde)
> Demo of Groqnotes fast transcription of audio and generation of structured notes

---

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

> As with all generative AI, content may include inaccurate or placeholder information. Groqnotes is in beta and all feedback is welcome!

---

## Quickstart

> [!IMPORTANT]
> To use Groqnotes, you can use the hosted version at [groqnotes.streamlit.app](https://groqnotes.streamlit.app)
> Alternatively, you can run groqnotes locally with streamlit using the quickstart instructions.


### Hosted on Streamlit:

To use Groqnotes, you can use the hosted version at [groqnotes.streamlit.app](https://groqnotes.streamlit.app)


### Run locally:

Alternative, you can run groqnotes locally with streamlit.

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

Groqnotes may generate inaccurate information or placeholder content. It should be used to generate books for entertainment purposes only.


## Contributing

Improvements through PRs are welcome!


## Changelog

Coming soon!

### Future Features:

- Create summary version of transcript, batching into sections of n characters.
- Allow upload of multiple audio files
