from flask import Flask, render_template,request
import pickle
import numpy as np
app = Flask(__name__)
job_datas = pickle.load(open('job_data.pkl','rb'))
job_similarity = pickle.load(open('similarity_job.pkl','rb'))

@app.route('/', methods=['GET', 'POST'])
def search_jobs():
    jobs = []
    if request.method == 'POST':
        query = request.form['query']
        index = job_datas[job_datas['job_title']==query].index[0]
        similarity = sorted(list(enumerate(job_similarity[index])),key=lambda x:x[1],reverse=True)[1:6]
        jobs = []
        for i in similarity:
            temp = job_datas.iloc[i[0]]
            temp_store={
                 'title': temp['job_title'],
                 'url': temp['company_website'],
                 'company_name': temp['company_name'],
                 'posted_date': temp['job_posted_date'],
                 'seniority_level': temp['seniority_level'],
                 'company_address_locality': temp['company_address_locality'],
                 'description': temp['job_description_text'],
            }
            jobs.append(temp_store)
        return render_template('search_job.html', jobs=jobs)
    return render_template('search_job.html')
      

if __name__ == '__main__':
    app.run(debug=True)