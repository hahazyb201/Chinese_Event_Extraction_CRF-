# Chinese_Event_Extraction_CRF-
<p>I used CRF++ 0.58 to extract event from sentences in the chinese traffic law(It is also called a sequence chunking problem). There are mainly four elements I want to extract:</p>
<p>Subject, Action, Key word,Result, Obligation, Forbidden, Right.</p>
<p>The first four elements are to describe an event and the last three are classes of the event.
Nowadays, people mainly use HMM, CRF to tag the sequence in NLP field. Compared with HMM, CRF can take the tags of the entire sentence into consideration.
So CRF performs better than HMM.</p>
<p>
Steps to use my program:
</p>

<p>1.Give me a star(very important).</p>
2.In directory ./CRF++-0.58, save Trainfile and Testfile as Trainfile.txt and Testfile.txt using UTF-8 encoding.
3.Run: .\crf_learn.exe -c 0.3 .\Template .\Trainfile.txt .\model
Parameter -c is used to control the balance between overfitting and underfitting.
Then we get the trained model.
4.Run: .\crf_test -m model Testfile.txt > result.txt
Then we get the prediction by our CRF model.
5.Evaluate:
Copy result.txt to the directory ./
and run: python3 ./evaluate.py 
And you use see the precision, recall and F-1 score.
