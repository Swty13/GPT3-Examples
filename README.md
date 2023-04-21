# GPT-3 Examples and Tools
This repository contains examples and tools related to working with GPT-3, a state-of-the-art language model developed by OpenAI. The aim of this repository is to provide a collection of code snippets and utilities that can be used to experiment with GPT-3, build applications using GPT-3, or conduct research related to GPT-3.

## Contents

The repository is organized into several directories:

1. **examples/:** This directory contains examples of using GPT-3 for various natural language processing tasks.

  ###### GPT-3 Streamlit Example
  This file demonstrates how to build a Streamlit app that uses GPT-3 to generate text. The file provides both streaming and non-streaming options for generating text, and allows the user to select option.

  ###### Usage

  Run `streamlit run stream_run.py` 

Once the app is running, you can use it to generate text in the following ways:

* Enter a prompt manually: Simply enter a prompt in the text box provided and click the "Submit" button to generate text based on that prompt.
* Switch between streaming and non-streaming modes: Use the checkbox to switch between `Streaming` and `Non-streaming` modes. In streaming mode, the app generates text one sentence at a time, allowing the user to see the output as it is generated.
![Alt Text](https://github.com/Swty13/GPT3-Examples/blob/main/streamlit_gif.gif)

2. **demos/:** This directory contains interactive demos of GPT-3, such as how to use GPT-3 on your system.
3. **experiments/:** This directory contains experimental code and scripts that can be used to test and evaluate different configurations of GPT-3, or to compare the performance of GPT-3 to other language models.


## Requirements

To run the code in this repository, you will need the following:

* A GPT-3 API key from OpenAI. Instructions for obtaining a key can be found on the OpenAI website.
* Python 3.x with the openai package installed. Instructions for installing the openai package can be found on the OpenAI GitHub page.

## Getting Started

To get started with this repository, follow these steps:

* Clone the repository to your local machine.
* Install the required dependencies using pip install -r requirements.txt.
* Set your GPT-3 API key as an environment variable named OPENAI_API_KEY.
* Navigate to one of the subdirectories (e.g., examples/)

## Contributing

If you would like to contribute to this repository, please follow these guidelines:

* Fork the repository and create a new branch for your changes.
* Make your changes and test them locally.
* Submit a pull request describing your changes and the problem they solve.

