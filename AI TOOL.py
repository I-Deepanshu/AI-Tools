import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist

# Install NLTK if you haven't done it already
# !pip install nltk

# Function to process a resume and extract important words
def process_resume(resume_text):
    words = word_tokenize(resume_text.lower())
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    return words

# Keywords related to the job position you're hiring for
job_keywords = ['skills', 'experience', 'qualifications', 'team player', 'communication']

# Function to calculate the score based on keyword frequency
def calculate_keyword_score(resume_words):
    fdist = FreqDist(resume_words)
    keyword_score = sum(fdist[keyword] for keyword in job_keywords)
    return keyword_score

# Dictionary of candidates and their resumes
candidates = {
    'Candidate 1': "Experienced software engineer with excellent communication skills.",
    'Candidate 2': "Highly skilled in data analysis and a great team player.",
    'Candidate 3': "Fresh graduate with some internship experience in web development.",
}

best_candidate = None
best_score = 0

# Loop through candidates to find the best one
for candidate, resume_text in candidates.items():
    processed_resume = process_resume(resume_text)
    score = calculate_keyword_score(processed_resume)
    
    if score > best_score:
        best_candidate = candidate
        best_score = score

print("Best candidate:", best_candidate)
