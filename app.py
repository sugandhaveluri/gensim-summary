from __future__ import unicode_literals
from flask import Flask,render_template,request
from urllib.request import urlopen
from gensim.summarization import summarize
from bs4 import BeautifulSoup
from spacy_summarization import nltk_summarizer
#import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
#import time
import spacy
from gensim.summarization import summarize
nlp = spacy.load("en_core_web_md")
app = Flask(__name__)

# Reading Time
'''def readingTime(mytext):
	total_words = len([ token.text for token in nlp(mytext)])
	estimatedTime = total_words/200.0
	return estimatedTime'''

# Fetch Text From Url
def get_text(url):
	page = urlopen(url)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	return fetched_text

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/analyze',methods=['GET','POST'])
def analyze():
#	start = time.time()
	if request.method == 'POST':
		rawtext = request.form['rawtext']
		#final_reading_time = readingTime(rawtext)
		final_summary = nltk_summarizer(rawtext)
		'''summary_reading_time = readingTime(final_summary)
		end = time.time()
		final_time = end-start'''
	return render_template('index.html',ctext=rawtext,final_summary=final_summary)

@app.route('/analyze_url',methods=['GET','POST'])
def analyze_url():
	#start = time.time()
	if request.method == 'POST':
		raw_url = request.form['raw_url']
		rawtext = get_text(raw_url)
		#final_reading_time = readingTime(rawtext)
		final_summary = nltk_summarizer(rawtext)
		'''summary_reading_time = readingTime(final_summary)
		end = time.time()
		final_time = end-start'''
	return render_template('index.html',ctext=rawtext,final_summary=final_summary)



@app.route('/compare_summary')
def compare_summary():
	return render_template('compare_summary.html')

@app.route('/comparer',methods=['GET','POST'])
def comparer():
	#start = time.time()
	if request.method == 'POST':
		rawtext = request.form['rawtext']
		#final_reading_time = readingTime(rawtext)
		#final_summary_spacy = nltk_summarizer(rawtext)
		#summary_reading_time = readingTime(final_summary_spacy)
		# Gensim Summarizer
		final_summary_gensim = summarize(rawtext)
		#summary_reading_time_gensim = readingTime(final_summary_gensim)
		#end = time.time()
		#final_time = end-start
	#return render_template('compare_summary.html',ctext=rawtext,final_summary_spacy=final_summary_spacy,summary_reading_time=summary_reading_time,summary_reading_time_gensim=summary_reading_time_gensim,final_summary_sumy=final_summary_sumy,summary_reading_time_sumy=summary_reading_time_sumy,summary_reading_time_nltk=summary_reading_time_nltk)
    
	return render_template('compare_summary.html',ctext=rawtext,final_summary_gensim=final_summary_gensim)


@app.route('/about')
def about():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)