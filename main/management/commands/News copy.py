from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main import models
import matplotlib
import google.generativeai as genai
import os
import urllib.request
import json
import time
import requests
from langchain_community.document_loaders import CSVLoader
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from openai import OpenAI
import tiktoken
import pandas as pd
import random
from typing import List, Optional
from scipy import spatial

def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False


def distances_from_embeddings(
    query_embedding: List[float],
    embeddings: List[List[float]],
    distance_metric="cosine",
) -> List[List]:
    """Return the distances between a query embedding and a list of embeddings."""
    distance_metrics = {
        "cosine": spatial.distance.cosine,
        "L1": spatial.distance.cityblock,
        "L2": spatial.distance.euclidean,
        "Linf": spatial.distance.chebyshev,
    }
    distances = [
        distance_metrics[distance_metric](query_embedding, embedding)
        for embedding in embeddings
    ]
    return distances

genai.configure(api_key = settings/GEMINI_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

from django.core.management.base import BaseCommand, CommandError
from llama_index.core import SimpleDirectoryReader, GPTVectorStoreIndex, ServiceContext, StorageContext, load_index_from_storage, PromptHelper
from llama_index.legacy import LLMPredictor

os.environ['OPENAI_API_KEY'] = settings.OPEN_AI_KEY

gpt_client = OpenAI(api_key= settings.OPEN_AI_KEY)

client = OpenAI(api_key= settings.OPEN_AI_KEY)

def create_context(
    question, df, max_len=1800, size="ada"
    ):
        """
        Create a context for a question by finding the most similar context from the dataframe
        """

        # Get the embeddings for the question
        q_embeddings = client.embeddings.create(input=question, model='text-embedding-ada-002').data[0].embedding

        # Get the distances from the embeddings
        df['distances'] = distances_from_embeddings(q_embeddings, df['embeddings'].values, distance_metric='cosine')


        returns = []
        cur_len = 0

        # Sort by distance and add the text to the context until the context is too long
        for i, row in df.sort_values('distances', ascending=True).iterrows():

            # Add the length of the text to the current length
            cur_len += row['n_tokens'] + 4

            # If the context is too long, break
            if cur_len > max_len:
                break

            # Else add it to the text that is being returned
            returns.append(row["text"])

        # Return the context
        return "\n\n###\n\n".join(returns)

def answer_question(
    df,
    model="gpt-3.5-turbo",
    question="Am I allowed to publish model outputs to Twitter, without a human review?",
    max_len=10000,
    size="ada",
    debug=False,
    max_tokens=600,
    stop_sequence=None
):
    """
    Answer a question based on the most similar context from the dataframe texts
    """
    context = create_context(
        question,
        df,
        max_len=max_len,
        size=size,
    )
    # If debug, print the raw model response
    if debug:
        print("Context:\n" + context)
        print("\n\n")

    # Create a chat completion using the question and context
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "response answer from context"},
            {"role": "user", "content": f"Context: {context}\n\n---\n\nQuestion: {question}"}
        ],
        temperature=0.3,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=stop_sequence,
    )
    return [response.choices[0].message.content.replace('Further reading:', '').replace('Answer:', '').replace('[Further Reading on ePlanet Brokers]', ''), context]

def get_text(text):
        df=pd.read_csv('/Analyzer/embeddings.csv', index_col=0)
        df['embeddings'] = df['embeddings'].apply(eval).apply(np.array)

        df.head()
        return answer_question(df=df, question=text)



def remove_newlines(serie):
    
    return serie

max_tokens = 500
tokenizer = tiktoken.get_encoding("cl100k_base")
# Function to split the text into chunks of a maximum number of tokens
def split_into_many(text, max_tokens = max_tokens):

    # Split the text into sentences
    sentences = text.split('. ')

    # Get the number of tokens for each sentence
    n_tokens = [len(tokenizer.encode(" " + sentence)) for sentence in sentences]

    chunks = []
    tokens_so_far = 0
    chunk = []

    # Loop through the sentences and tokens joined together in a tuple
    for sentence, token in zip(sentences, n_tokens):

        # If the number of tokens so far plus the number of tokens in the current sentence is greater
        # than the max number of tokens, then add the chunk to the list of chunks and reset
        # the chunk and tokens so far
        if tokens_so_far + token > max_tokens:
            chunks.append(". ".join(chunk) + ".")
            chunk = []
            tokens_so_far = 0

        # If the number of tokens in the current sentence is greater than the max number of
        # tokens, go to the next sentence
        if token > max_tokens:
            continue

        # Otherwise, add the sentence to the chunk and add the number of tokens to the total
        chunk.append(sentence)
        tokens_so_far += token + 1

    return chunks



def get_news_gpt():
    today = ""
    texts=[]
    for itemm in models.NewsSite.objects.all().order_by("-id"):
        fp = urllib.request.urlopen(itemm.url)
        mybytes = fp.read()

        mystr = mybytes.decode("utf8")
        print(itemm.url)
        fp.close()
                
        texts.append((str(random.randint(0, 10000000000000000)), mystr))
        print(texts)
        df = pd.DataFrame(texts, columns = ['fname', 'text'])

        # Set the text column to be the raw text with the newlines removed
        df['text'] = df.fname + ". " + remove_newlines(df.text)
        df.to_csv('/Analyzer/scraped.csv')
        df.head()

        shortened = []




        df.to_csv('/Analyzer/embeddings.csv')
        df.head()

        df = pd.read_csv('/Analyzer/scraped.csv', index_col=0)
        df.columns = ['title', 'text']

        # Tokenize the text and save the number of tokens to a new column
        df['n_tokens'] = df.text.apply(lambda x: len(tokenizer.encode(x)))

        # Visualize the distribution of the number of tokens per row using a histogram
        df.n_tokens.hist()

        shortened = []

        # Loop through the dataframe
        for row in df.iterrows():

            # If the text is None, go to the next row
            if row[1]['text'] is None:
                continue

            # If the number of tokens is greater than the max number of tokens, split the text into chunks
            if row[1]['n_tokens'] > max_tokens:
                shortened += split_into_many(row[1]['text'])

            # Otherwise, add the text to the list of shortened texts
            else:
                shortened.append( row[1]['text'] )

        df = pd.DataFrame(shortened, columns = ['text'])
        df['n_tokens'] = df.text.apply(lambda x: len(tokenizer.encode(x)))
        df.n_tokens.hist()

        

        df['embeddings'] = df.text.apply(lambda x: client.embeddings.create(input=x, model='text-embedding-ada-002').data[0].embedding)

        df.to_csv('/Analyzer/embeddings.csv')
        df.head()
        try:
            for item in models.NewsIntrest.objects.all():

                prompt = f"content related to {item.subject} as only a json with pic,description and title "
                # response = model.generate_content(prompt,).text
                #print(response.split(',')[-1])
                result = get_text(prompt)
                context = result[1]
                while '\n###\n' in context:
                    context = context.replace('\n###\n', ',')
                
                response = result[0]
                print(response)
                response = response.replace("```json", "").replace("```", "")
                # print(response)
                response = json.loads(response)
                for itemm in response:
                    if "title" in itemm and "pic" in itemm and "description" in itemm and is_url_image(itemm["pic"]):
                        if not len(models.NewsReport.objects.filter(pic=itemm["pic"])):
                            models.NewsReport.objects.create(
                                title=itemm["title"],
                                text=itemm["description"],
                                pic=itemm["pic"],
                                subject=item.subject,
                            )
                time.sleep(3)
        except:
            pass



def get_news():
    today = ""
    for itemmm in models.NewsSite.objects.all().order_by("-id"):
        fp = urllib.request.urlopen(itemmm.url)
        mybytes = fp.read()

        mystr = mybytes.decode("utf8")
        print(itemmm.url)
        fp.close()
        today = today + mystr + "\n\n\n"
        for item in models.NewsIntrest.objects.all():

            prompt = f"content related to {item.subject} as only a json with pic,description and title based on {today} "
            response = model.generate_content(prompt,).text
            #print(response.split(',')[-1])
            

            
            response = response.replace("```json", "").replace("```", "")
            print(response)
            response = json.loads(response)
            try:
                for itemm in response:
                    if "title" in itemm and "pic" in itemm and "description" in itemm and is_url_image(itemm["pic"]):
                        if not len(models.NewsReport.objects.filter(pic=itemm["pic"])):
                            models.NewsReport.objects.create(
                                user= item.user,
                                title=itemm["title"],
                                text=itemm["description"],
                                pic=itemm["pic"],
                                subject=item.subject,
                                resource = itemmm.name
                            )
            except:
                pass
            time.sleep(3)


class Command(BaseCommand):
    def handle(self, *args, **options):
            # get_news()
            get_news_gpt()
