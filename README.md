# difficulty_index_online_exams

  Above code is used to find the difficulty level of question based no.of students attended each questions along with time taken , marks
obtained,  hints used for each question. Dataset is divided into multiple dataframes based on question type mentioned in dataset. During
diviision, columns that doesn't have impact on deciding difficulty is removed from every dataframe. It used concept explained in measure of
central tendency to calculate the average on marks obtained, duration, no.of times compiled (programming),no.of times changed. For each 
question average in calculated and stored. Time duration, marks_obtained, hint, no.of times compiled(programming),no.of times changed are 
mainly used to predict the difficulty of a question. Let's consider calculated average for every column as it 100%. For every column, 
calculated value is compared against actual column value. 
  Firstly duration for question greater than 140% of average of time duration and also mark_obatained less than 60% of average 
mark_obtained it increases the probability for difficulty index to "Hard", then no.of times compiled higher than usual compiled count,
question is considered as "Hard" . If there is deviation in mark_obtained and it is around average of marks_obtained, hints used is
less or equal to one, no.of times compiled is less than or around average of no.of times compiled then it considered as "Medium". If any
constraint if not satisfied then it is "Hard". If time taken is less and mark_obtained is high with zero hint it considered as "Hint" ,
else if mark_obtained is around average and hint is used it "Hard" else dificulty index is "Hard" . If mark_obtaind is less in time
duration then it considered as "Hard". Following pattern is followed to find difficulty index for other question types.
  After gettting difficulty level of every question , for every question type difficulty level is present in different data frame ,it
joined is to make a single dataframe and sorted based on challenge id(challen_id). Resultant dataframe consists of challenge id, challenge
id , difficulty index and it saved to file name called "Result.csv"

mean : marks_obtained,no.of times compiled, duration
mode : hint,answered

Usage :

python difficulty_index.py <dataset>   #csv format
  
exapmle : python difficulty_index.py dataset.csv
