# -*- coding: utf-8 -*-
"""Mockinterview-Falcon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hCKPV5U_bg7QQXPUIwwDvCdB1N8fgz0z

## Install dependencies
"""


"""## Import dependencies"""

import os
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    pipeline
)

import csv
import codecs

from langchain import PromptTemplate,  LLMChain
import random
import json

"""## Creating pipeline for Falcon-7b"""

from langchain import HuggingFacePipeline
from transformers import AutoTokenizer, pipeline
import torch

model = "tiiuae/falcon-7b-instruct" #tiiuae/falcon-40b-instruct

tokenizer = AutoTokenizer.from_pretrained(model)

pipeline = pipeline(
    "text-generation", #task
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
    max_length=512,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id
)

llm = HuggingFacePipeline(pipeline = pipeline, model_kwargs = {'temperature':0})

"""## Loading csv (attempting the program without RAG)

* RAG was reducing program efficiency.
"""

file = "/content/Combined_Data_set.csv"

fields = []
rows = []

with codecs.open(file, 'r', 'utf-8') as csvfile:
  csvreader = csv.reader(csvfile)
  fields = next(csvreader)

  for row in csvreader:
    rows.append(row)

"""## LLMChain for deciding next question"""

# Here we can make certain changes through the prompt template, like the tone in which we want the questions to be asked, we may use few shots for that.

record = random.randint(0,len(rows))

def get_question():
    topic = rows[record][0] #extracting question from csv

    template1 = """
    You are a data science interviewer between an interview, ask a question regarding the following given topic:
    Topic to ask question on as a interviewer: {question}
    """
    prompt1 = PromptTemplate(template=template1, input_variables=["question"])

    llm_chain = LLMChain(prompt=prompt1, llm=llm)

    next_question = llm_chain.run(topic)
    # print(next_question)
    json_string = "{{\"question\": \"{}\"}}".format(next_question)

    json_ques = json.loads(json_string, strict=False)

    return json_ques

result = get_question()
result

result['question']

"""## LLMChain for evaluating user response"""

# Now we can improve performance through the prompt, like we can provide a few shots, tell it about how to give positive and negative responses using some shots.

# corr_ans = rows[record][1] #extracting answer from csv

def get_evaluation(response):
    template2 = '''
    You are a data scientist interviewer and you are taking the interview of someone.
    Evaluate the response given by that person: {response}

    '''
    prompt2 = PromptTemplate(template=template2, input_variables=["response"])

    llm_chain2 = LLMChain(prompt=prompt2, llm=llm)

    evaluation = llm_chain2.run(response)
    #print(evaluation)
    json_string = "{{\"response\" : \"{}\" }}".format(evaluation)

    json_eval = json.loads(json_string, strict=False)
    return json_eval

response = input("Enter your response: ")
result = get_evaluation(response)
result

result['response']