from django.utils import timezone
from .models import UserProfile, Document
import spacy

def reset_credits():
    now = timezone.now()
    today_midnight = timezone.datetime.combine(now.date(), timezone.datetime.min.time(), tzinfo=now.tzinfo)

    profiles = UserProfile.objects.all()
    for profile in profiles:
        if profile.last_reset.date() < now.date():
            profile.credits = 20
            profile.last_reset = today_midnight  
            profile.save()


def levenshtein_distance(s1, s2):
    
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

def find_matches(doc):
    
    all_docs = Document.objects.exclude(id=doc.id)
    matches = []
    for other in all_docs:
        distance = levenshtein_distance(doc.content, other.content)
        if distance < len(doc.content) * 0.3:  
            matches.append(other)
    return matches


nlp = spacy.load('en_core_web_sm')

def ai_find_matches(doc):

    doc_nlp = nlp(doc.content)

    all_docs = Document.objects.exclude(id=doc.id)
    matches = []
    
    for other in all_docs:
        other_nlp = nlp(other.content)

        similarity = doc_nlp.similarity(other_nlp)

        similarity_percentage = round(similarity * 100, 2)  # Round to 2 decimal places

        matches.append({
            'document': other,
            'similarity_percentage': similarity_percentage
        })

    matches.sort(key=lambda x: x['similarity_percentage'], reverse=True)

    return matches