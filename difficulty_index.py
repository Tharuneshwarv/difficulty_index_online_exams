# -*- coding: utf-8 -*-
"""
Created on Tue May 26 18:46:31 2020

@author: HELLSHIELD
"""
import pandas as pd
import numpy as np
from scipy import stats
import warnings

def prog_difficult(program_agg,prog_dur,prog_mark,prog_com):
    for ind in program_agg.index:
        if program_agg['duration'][ind] >= prog_dur*1.5:
            if program_agg['marks_obtained'][ind] <= prog_mark*0.6:
                if program_agg['no.of times compiled(program)'][ind] >= prog_com*1.5 :
                    program_agg['diff_level'][ind] = 'Hard'
                else:
                    program_agg['diff_level'][ind] = 'Medium'
            else :
                program_agg['diff_level'][ind] = 'Medium'
        elif program_agg['duration'][ind] < prog_dur*1.5 and program_agg['duration'][ind] >= (prog_dur*0.6) :
            if program_agg['marks_obtained'][ind] >= prog_mark*1.5:
                if program_agg['no.of times compiled(program)'][ind] <= prog_com*0.5:
                    if program_agg['hint'][ind] <= 1:
                        program_agg['diff_level'][ind] = 'Easy'
                    else:
                        program_agg['diff_level'][ind] = 'Medium'
                else:
                    program_agg['diff_level'][ind] = 'Medium'
            elif program_agg['marks_obtained'][ind] < prog_mark*1.5 and program_agg['marks_obtained'][ind] > prog_mark*0.5:
                if program_agg['no.of times compiled(program)'][ind] >= prog_com*1.0:
                    if program_agg['hint'][ind] > 1:
                        program_agg['diff_level'][ind] = 'Hard'
                    else:
                        program_agg['diff_level'][ind] = 'Medium'
                else:
                    program_agg['diff_level'][ind] = 'Medium'
            else:
                program_agg['hint'][ind] = 'Easy'
        else:
            if program_agg['marks_obtained'][ind] >= prog_mark*1.5:
                if program_agg['no.of times compiled(program)'][ind] <= prog_com*0.5:
                    if program_agg['hint'][ind] <= 1:
                        program_agg['diff_level'][ind] = 'Easy'
                    else:
                        program_agg['diff_level'][ind] = 'Medium'
                else:
                    program_agg['diff_level'][ind] = 'Medium'
            elif program_agg['marks_obtained'][ind] < prog_mark*1.5:
                if program_agg['no.of times compiled(program)'][ind] <= prog_com:
                    program_agg['diff_level'][ind] = 'Medium'
                else:
                    program_agg['diff_level'][ind] = 'Hard'
    return program_agg

def mcq_difficult(mcq_agg,mcq_dur,mcq_mark,mcq_ch):
    for ind in mcq_agg.index:
        if mcq_agg['duration'][ind] >= mcq_dur*1.5 :
            if mcq_agg['marks_obtained'][ind] < mcq_mark *0.7 :
                if mcq_agg['no.of times changed(mcq)'][ind] >= mcq_ch*1.3 or mcq_agg['hint'][ind] > 1:
                    mcq_agg['diff_level'][ind] = 'Hard'
                else:
                    mcq_agg['diff_level'][ind] = 'Medium'
            elif mcq_agg['marks_obtained'][ind] >= mcq_mark*0.7 and mcq_agg['marks_obtained'][ind] < mcq_mark*1.35 :
                if mcq_agg['no.of times changed(mcq)'][ind] >= mcq_ch*1.3:
                    mcq_agg['diff_level'][ind] = 'Hard'
                elif mcq_agg['no.of times changed(mcq)'][ind] < mcq_ch*1.3 or mcq_agg['hint'][ind] <= 1:
                    mcq_agg['diff_level'][ind] = 'Medium'
                else:
                    mcq_agg['diff_level'][ind] = 'Hard'
            else:
                if mcq_agg['no.of times changed(mcq)'][ind] < mcq_ch*0.6:
                    mcq_agg['diff_level'][ind] = 'Easy'
                elif mcq_agg['hint'][ind] <= 1:
                    mcq_agg['diff_level'][ind] = 'Medium'
                else:
                    mcq_agg['diff_level'][ind] = 'Hard'
        elif mcq_agg['duration'][ind] < mcq_dur *1.5 and mcq_agg['duration'][ind] > mcq_dur*0.6 :
            if mcq_agg['marks_obtained'][ind] < mcq_mark *0.7 :
                if mcq_agg['no.of times changed(mcq)'][ind] >= mcq_ch*1.3 or mcq_agg['hint'][ind] > 1:
                    mcq_agg['diff_level'][ind] = 'Hard'
                else:
                    mcq_agg['diff_level'][ind] = 'Medium'
            elif mcq_agg['marks_obtained'][ind] >= mcq_mark*0.7 and mcq_agg['marks_obtained'][ind] < mcq_mark*1.35 :
                if mcq_agg['no.of times changed(mcq)'][ind] >= mcq_ch*1.3:
                    mcq_agg['diff_level'][ind] = 'Hard'
                elif mcq_agg['no.of times changed(mcq)'][ind] < mcq_ch*1.3 or mcq_agg['hint'][ind] <= 1:
                    mcq_agg['diff_level'][ind] = 'Medium'
                else:
                    mcq_agg['diff_level'][ind] = 'Hard'
            else:
                if mcq_agg['no.of times changed(mcq)'][ind] < mcq_ch*0.6 and mcq_agg['hint'][ind] <= 1:
                    mcq_agg['diff_level'][ind] = 'Easy'
                elif mcq_agg['hint'][ind] <= 1:
                    mcq_agg['diff_level'][ind] = 'Medium'
                else:
                    mcq_agg['diff_level'][ind] = 'Hard'
        else:
            if mcq_agg['marks_obtained'][ind] < mcq_mark *0.7 :
                if mcq_agg['no.of times changed(mcq)'][ind] >= mcq_ch*1.3:
                    mcq_agg['diff_level'][ind] = 'Hard'
                else:
                    mcq_agg['diff_level'][ind] = 'Medium'
            elif mcq_agg['marks_obtained'][ind] >= mcq_mark*0.7 and mcq_agg['marks_obtained'][ind] < mcq_mark*1.35 :
                if mcq_agg['no.of times changed(mcq)'][ind] >= mcq_ch*1.3:
                    mcq_agg['diff_level'][ind] = 'Medium'
                elif mcq_agg['no.of times changed(mcq)'][ind] < mcq_ch*1.3 or mcq_agg['hint'][ind] <= 1:
                    mcq_agg['diff_level'][ind] = 'Easy'
                else:
                    mcq_agg['diff_level'][ind] = 'Hard'
            else:
                if mcq_agg['no.of times changed(mcq)'][ind] < mcq_ch*0.6:
                    mcq_agg['diff_level'][ind] = 'Easy'
                elif mcq_agg['hint'][ind] <= 1:
                    mcq_agg['diff_level'][ind] = 'Medium'
                else:
                    mcq_agg['diff_level'][ind] = 'Hard'
    return mcq_agg

def fill_difficult(fill_agg,fill_mark,fill_dur):
    for ind in fill_agg.index:
        if fill_agg['duration'][ind] >= fill_dur*1.5 :
            if fill_agg['marks_obtained'][ind] < fill_mark*0.6:
                if fill_agg['hint'][ind] <= 1:
                    fill_agg['diff_level'][ind] = 'Medium'
                else:
                    fill_agg['diff_level'][ind] = 'Hard'
            elif fill_agg['marks_obtained'][ind] >= fill_mark*0.6 and fill_agg['marks_obtained'][ind] <= fill_mark*1.5 :
                fill_agg['diff_level'][ind] = 'Hard'
            else:
                fill_agg['diff_level'][ind] = 'Medium'
        elif fill_agg['duration'][ind] < fill_dur*1.5 and fill_agg['duration'][ind] > fill_dur*0.6 :
            if fill_agg['marks_obtained'][ind] < fill_mark*0.6 :
                if fill_agg['hint'][ind] <= 1:
                    fill_agg['diff_level'][ind] = 'Medium'
                else:
                    fill_agg['diff_level'][ind] = 'Hard'
            elif fill_agg['marks_obtained'][ind] >= fill_mark*0.6 and fill_agg['marks_obtained'][ind] <= fill_mark*1.5 :
                if fill_agg['hint'][ind] <= 1:
                    fill_agg['diff_level'][ind] = 'Easy'
                else:
                    fill_agg['diff_level'][ind] = 'Medium'
            else :
                if fill_agg['hint'][ind] == 0:
                    fill_agg['diff_level'][ind] = 'Easy'
                else:
                    fill_agg['diff_level'][ind] = 'Medium'
        else:
            if fill_agg['marks_obtained'][ind] > fill_mark*1.5:
                fill_agg['diff_level'][ind] = 'Easy'
            elif fill_agg['marks_obtained'][ind] < fill_mark*0.7:
                if fill_agg['hint'][ind] == 0:
                    fill_agg['diff_level'][ind] = 'Medium'
                else:
                    fill_agg['diff_level'][ind] = 'Hard'
            else:
                if fill_agg['hint'][ind] <= 0:
                    fill_agg['diff_level'][ind] = 'Easy'
                else:
                    fill_agg['diff_level'][ind] = 'Medium'
    return fill_agg

def match_difficult(match_agg,match_dur,match_mark):
    for ind in match_agg.index:
        if match_agg['duration'][ind] >= match_dur*1.4:
            if match_agg['marks_obtained'][ind] < match_mark*0.7:
                match_agg['diff_level'][ind] = 'Hard'
            elif match_agg['marks_obtained'][ind] >= match_mark*1.4:
                if match_agg['hint'][ind] <= 1:
                    match_agg['diff_level'][ind] = 'Medium'
                else:
                    match_agg['diff_level'][ind] = 'Hard'
            else:
                match_agg['diff_level'][ind] = 'Medium'
        elif match_agg['duration'][ind] <= match_dur*0.6:
            if match_agg['marks_obtained'][ind] >= match_mark*1.4:
                if match_agg['hint'][ind] == 0:
                    match_agg['diff_level'][ind] = 'Easy'
                else:
                    match_agg['diff_level'][ind] = 'Medium'
            elif match_agg['marks_obtained'][ind] < match_mark*0.5:
                 match_agg['diff_level'][ind] = 'Hard'     
            else:
                if match_agg['hint'][ind] <= 1:
                    match_agg['diff_level'][ind] = 'Medium'
                else:
                    match_agg['diff_level'][ind] = 'Hard'  
        else:
            if match_agg['marks_obtained'][ind] >= match_mark*1.4:
                if match_agg['hint'][ind] == 0:
                    match_agg['diff_level'][ind] = 'Easy'
                elif match_agg['hint'][ind] == 3:
                    match_agg['diff_level'][ind] = 'Hard'
                else:
                    match_agg['diff_level'][ind] = 'Medium'
            elif match_agg['marks_obtained'][ind] < match_mark*0.5:
                if match_agg['hint'][ind] <= 1:
                    match_agg['diff_level'][ind] = 'Easy'
                else:
                    match_agg['diff_level'][ind] = 'Medium'
            else:
                if match_agg['hint'][ind] == 0:
                    match_agg['diff_level'][ind] = 'Medium'
                else:
                    match_agg['diff_level'][ind] = 'Hard' 
    return match_agg

def main(dataset):

    report = pd.read_csv(dataset)
    report = report.replace(np.nan,-1)
    program_df = report.drop(['no.of times changed(mcq)','user_id'], axis = 1) 
    indexNames = program_df[ program_df['ques_type'] != 'programming' ].index
    program_df.drop(indexNames , inplace=True)
    program_agg = program_df.groupby(['challen_id']).agg({'challen_id':lambda x:stats.mode(x)[0],
                                     'challen_name':lambda x:stats.mode(x)[0],
                                     'hint': lambda x:stats.mode(x)[0], 
                                     'Answered': lambda x:stats.mode(x)[0],
                                     'language': lambda x:stats.mode(x)[0],
                                     'duration': 'mean',
                                     'marks_obtained': 'mean',
                                     'no.of times compiled(program)' : 'max',
                                     'diff_level' : lambda x:stats.mode(x)[0]})
    program_agg['duration'] = program_agg['duration'].astype(int)
    program_agg['marks_obtained'] = program_agg['marks_obtained'].astype(int)
    program_agg['no.of times compiled(program)'] = program_agg['no.of times compiled(program)'].astype(int)
    prog_dur = program_agg['duration'].mean()
    prog_mark = program_agg['marks_obtained'].mean()
    prog_com = program_agg['no.of times compiled(program)'].mean()
    program_agg = prog_difficult(program_agg,prog_dur,prog_mark,prog_com)
    #print(program_agg)
    ##########################################################################
    mcq_df = report.drop(['no.of times compiled(program)','language','user_id'], axis = 1) 
    indexNames = mcq_df[ mcq_df['ques_type'] != 'mcq' ].index
    mcq_df.drop(indexNames  , inplace=True)
    mcq_agg = mcq_df.groupby(['challen_id']).agg({'challen_id':lambda x:stats.mode(x)[0],
                                     'challen_name':lambda x:stats.mode(x)[0],
                                     'hint': lambda x:stats.mode(x)[0], 
                                     'Answered': lambda x:stats.mode(x)[0],
                                     'duration': 'mean',
                                     'marks_obtained': 'mean',
                                     'no.of times changed(mcq)' : lambda x:stats.mode(x)[0],
                                     'diff_level' : lambda x:stats.mode(x)[0]})
    
    mcq_agg['duration'] = mcq_agg['duration'].astype(int)
    mcq_agg['marks_obtained'] = mcq_agg['marks_obtained'].astype(int)
    mcq_agg['no.of times changed(mcq)'] = mcq_agg['no.of times changed(mcq)'].astype(int)
    mcq_dur = mcq_agg['duration'].mean()
    mcq_mark = mcq_agg['marks_obtained'].mean()
    mcq_ch = mcq_agg['no.of times changed(mcq)'].mean()
    mcq_agg = mcq_difficult(mcq_agg,mcq_dur,mcq_mark,mcq_ch)
    #print(mcq_agg)
    ###############################################################################
    fill_df = report.drop(['no.of times compiled(program)','no.of times changed(mcq)','language','user_id'], axis = 1) 
    indexNames = fill_df[ fill_df['ques_type'] != 'fill up' ].index
    fill_df.drop(indexNames  , inplace=True)
    fill_agg = fill_df.groupby(['challen_id']).agg({'challen_id':lambda x:stats.mode(x)[0],
                                     'challen_name':lambda x:stats.mode(x)[0],
                                     'hint': lambda x:stats.mode(x)[0], 
                                     'Answered': lambda x:stats.mode(x)[0],
                                     'duration': 'mean',
                                     'marks_obtained': 'mean',
                                     'diff_level' : lambda x:stats.mode(x)[0]})
    fill_agg['duration'] = fill_agg['duration'].astype(int)
    fill_agg['marks_obtained'] = fill_agg['marks_obtained'].astype(int)
    fill_dur = fill_agg['duration'].mean()
    fill_mark = fill_agg['marks_obtained'].mean()
    fill_agg = fill_difficult(fill_agg,fill_mark,fill_dur)
    #print(fill_agg)
    ###############################################################################
    match_df = report.drop(['no.of times compiled(program)','no.of times changed(mcq)','language','user_id'], axis = 1) 
    indexNames = match_df[ match_df['ques_type'] != 'match the following' ].index
    match_df.drop(indexNames  , inplace=True)
    match_agg = match_df.groupby(['challen_id']).agg({'challen_id':lambda x:stats.mode(x)[0],
                                     'challen_name':lambda x:stats.mode(x)[0],
                                     'hint': lambda x:stats.mode(x)[0], 
                                     'Answered': lambda x:stats.mode(x)[0],
                                     'duration': 'mean',
                                     'marks_obtained': 'mean',
                                     'diff_level' : lambda x:stats.mode(x)[0]})
    match_agg['duration'] = match_agg['duration'].astype(int)
    match_agg['marks_obtained'] = match_agg['marks_obtained'].astype(int)
    match_dur = match_agg['duration'].mean()
    match_mark = match_agg['marks_obtained'].mean()
    
    match_agg = match_difficult(match_agg,match_dur,match_mark)
    #print(match_agg)
    ##########################################################################
    final = [program_agg,mcq_agg,fill_agg,match_agg]
    result = pd.concat(final)
    result = result.filter(['challen_name','diff_level'])
    result.sort_index(inplace=True,ascending=True)
    result.to_csv('result.csv',index=True,encoding = 'utf-8')
    print(result)
if __name__ == "__main__":
        warnings.filterwarnings("ignore")
        main('dataset.csv')
