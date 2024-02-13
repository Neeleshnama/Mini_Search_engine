from modules import *
import random
import pandas as pd
def finding_freq_of_word_in_doc(word, words):
    freq = words.count(word)
    return freq

def finding_all_unique_words_and_frequency(words):
    words_unique = []
    word_freq = {}
    for word in words:
        if word not in words_unique:
            words_unique.append(word)
    for word in words_unique:
        word_freq[word] = words.count(word)

    return word_freq

def cosine_sim(query, vectorizer, tfidf_transformed):
    test_tfidf = vectorizer.transform([query])
    cos = []
    cosing_similarities = linear_kernel(
        test_tfidf, tfidf_transformed).flatten()
    cos.append(cosing_similarities)
    return np.array(cos).flatten()





def read_csv():
    return pd.read_csv('C://Users//hp//Documents//IR//P40-MiniProject-MOTOR//sourcecode//data//feedback.csv')
    
def get_top_results(data, score, columns_to_display):
    top_results = score.argsort()[::-1]
    results = {
        "Code": [],
        "Similarity": [],
        "feedback": [],
        "index": [],
        "precision": [],
        "recall": []
    }
    df = read_csv()

    for i in range(1, 11):
        results["precision"].append(i/i)
        results["recall"].append(i/10)

    # read df and add feedback to the top results
    for i in top_results[:10]:
        if df.loc[df['index'] == i].empty:
            results["feedback"].append(0)
        else:
            results["feedback"].append(df.loc[df['index'] == i, 'feedback'].values[0])

    max_feedback = max(results["feedback"]) == 0 and 1 or max(results["feedback"])

    for idx in top_results[:10]:
        results["Code"].append(" ".join([str(data.iloc[idx][col]) for col in columns_to_display]))
        results["Similarity"].append(score[idx])
        results["index"].append(idx)

    for i in range(len(results["feedback"])):
        results["feedback"][i] = ((results["feedback"][i] / max_feedback) * 60 + (results["Similarity"][i]) * 40)

    results["Code"] = [x for _, x in sorted(zip(results["feedback"], results["Code"]), reverse=True)]
    results["Similarity"] = [x for _, x in sorted(zip(results["feedback"], results["Similarity"]), reverse=True)]
    results["index"] = [x for _, x in sorted(zip(results["feedback"], results["index"]), reverse=True)]
    results["feedback"] = sorted(results["feedback"], reverse=True)

    for i in range(len(results["Code"])):
        print("> Recently updated feedbacks: ", results["feedback"][i])
        
    print('--------------------------------------------------')
                
    results_str = ""
    for i in range(10):
        results_str += "Index: " + str(results["index"][i]) + "\n" + \
            results["Code"][i] + "\n" + "Cosine Similarity: " + \
            str(results["Similarity"][i]) + "\n" + "Precision: " + \
            str(results["precision"][i]) + "\n" + "Recall: " + \
            str(results["recall"][i]) + "\n"
        results_str = results_str + "-" * 50 + "\n"

    print(results_str)
    with open("data/results.txt", "w") as file:
        file.writelines(results_str)

    return results_str
