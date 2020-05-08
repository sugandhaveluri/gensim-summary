from gensim.summarization import summarize
def nltk_summarizer(raw_text):
	


	summary_sentences = summarize(raw_text)

	#summary = ' '.join(summary_sentences)  
	return summary_sentences