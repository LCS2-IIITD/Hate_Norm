# NACL

## Demo of Web tool
[Video](https://github.com/LCS2-IIITD/Hate_Norm/blob/main/web_tool_demo.mp4)


## Main Dataset Files

### CRF_DATASET FILE should be per word per sentence.
```
<Sentence #>, Word, POS, Tag.
```
```
EXAMPLE for sentence list
[abc, defghi]
we get
Sentence 0, a, <POST TAG of the word>, <BIO SPAN of the word>
Sentence 0, b, <POST TAG of the word>, <BIO SPAN of the word>
Sentence 0, c, <POST TAG of the word>, <BIO SPAN of the word>
Sentence 1, d, <POST TAG of the word>, <BIO SPAN of the word>
Sentence 1, e, <POST TAG of the word>, <BIO SPAN of the word>
Sentence 1, f, <POST TAG of the word>, <BIO SPAN of the word>
Sentence 1, g, <POST TAG of the word>, <BIO SPAN of the word>
Sentence 1, h, <POST TAG of the word>, <BIO SPAN of the word>
Sentence 1, i, <POST TAG of the word>, <BIO SPAN of the word>
```

### Tag2idx Postag2idx
Tag2idx and Postag2idx are just a dictionary mapping the tags to their prediction class.
We save these because during data prep of span predictions we generate the tag list and pos list as as set, and then create an enumeration for the set.

### hate_norm_combined.pkl
* Contains the initally curated dataset of sentences, their normalised forms, their intensities and spans.
* Sentence and Normalised_Sentence columns are the explicitly hateful and their normalised versions respectively.
* Original_Intensity and Normalized_Intensity are the annotated intensity values of the hateful and normalised sentences respectively.
* Span colum contains a list of span indices starting from 0. It is of a dictionary per row in the form {"start":[s1,s2,...sN]},"end":[e1,e2...eN]}, where s1 and e1 correspond to the beining and end of 1st span in the original sentence and so on.
* Span_BIO and Pos_tag: One BIO and POS tag per in the sentence.

### train_df.csv
input_text, parapharase_text,<BART TOKEN> per line
where input_text and parapharase_text are hateful and normalised sentences and BART_TOKEN is set to "paraphrase".

## Main Code Files

* hate_intensity_prediction.ipynb for HIP model
* hate_span_pred_<elmo/glove>.ipynb for HSP model
* hate_int_reduce.ipynb for HIR model
* Utils.py to generate the crf_input file.
* Addtinally we have used crf.py (not able to track this source from Github)

## Hate Norm Dataset Access Request
To request access to the Hate Norm Dataset, follow the steps shown below.

Fill out the agreement form linked [here](https://forms.gle/eKMLLF93R5P7rsz7A)
Forward the google form's confirmation email to sarah@iiitd.ac.in and aflah20082@iiitd.ac.in requesting access to the dataset.

## Citation 

If you are using this work or the dataset, cite the [paper](https://arxiv.org/abs/2206.04007)

> Sarah Masud, Manjot Bedi, Mohammad Aflah Khan, Md Shad Akhtar, and Tanmoy Chakraborty. 2022. Proactively Reducing the Hate Intensity of Online Posts via Hate Speech Normalization. In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '22). Association for Computing Machinery, New York, NY, USA, 3524–3534. https://doi.org/10.1145/3534678.3539161
