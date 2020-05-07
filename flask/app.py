# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:52:50 2020

@author: Yury
"""
import sys
main_f='C:\\a_tree\\app\\'
sys.path.append(f'{main_f}')
import backend

from flask import Flask, flash, redirect,url_for, send_file
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

# from flask_wtf import Form

import sqlite3
from flask import render_template
from flask import request

from pandas import DataFrame as pddf
from pandas import isnull as isnull
from pandas import to_numeric as to_numeric
from pandas import notnull as notnull

app = Flask(__name__)


@app.route('/<int:iid>', methods=['GET', 'POST'])
def edit(iid):
    iid

from flask_table import Col, ButtonCol, DateCol, LinkCol, Table
  
class gen_table(Table):
    update = LinkCol('', 'booking_bp.update_booking',
                     url_kwargs=dict(id='id'),
                     anchor_attrs={'type': 'button',
                                   'class': 'btn btn-primary'})
    delete = LinkCol('Delete', 'booking_bp.delete_booking',
                     url_kwargs=dict(id='id'),
                     anchor_attrs={'type': 'button',
                                   'class': 'btn btn-danger'})
    classes = ['table', 'table-bordered', 'table-striped']
    film = Col('')
    start_date = DateCol('Start Date')
    end_date = DateCol('End Date')
    program = Col('Program')
    guarantee = Col('Guarantee')
    percentage = Col('Percentage')
    gross = Col('Gross')
    view_results = LinkCol('View Results', 'booking_bp.booking_results',
                           url_kwargs=dict(id='id'))
    distributor = Col('Distributor')
    enter_payment = LinkCol('Enter Payment', 'payments_bp.new_payment',
                            url_kwargs=dict(id='id'))
    view_payments = LinkCol('View Payments', 'payments_bp.view_payments',
                            url_kwargs=dict(id='id'))



@app.route("/", methods=["GET", "POST"])
def home():

    forma=None
    iid=None
    res=backend.view()
    forma=request.args.get('form')
    # from datetime import datetime
    # import pandas as pd


    if forma not in [None, 'None']:  
        import ast
        forma=ast.literal_eval(forma)
        # forma[3] = datetime.strptime(forma[3], '%Y-%m-%d')
        # forma[3] = pd.to_datetime(forma[3], '%Y-%m-%d', error='coerce')
        # if len(forma)>4: print('d', forma[3])
        # print('f', forma)
        
    if request.form:

            
        if request.method == 'POST':

            
            i_name = request.form.get('name')
            i_surname = request.form.get('surname')
            i_id = request.form.get('id')
            
            i_mother = request.form.get('mother_id')
            i_father = request.form.get('father_id')
            i_spouse = request.form.get('spouse_id')
            i_gen = request.form.get('gen_id')
            
            if isnull(i_mother) or i_mother==0: i_mother=None
            if isnull(i_father) or i_father==0: i_father=None
            if isnull(i_spouse) or i_spouse==0: i_spouse=None
            if isnull(i_gen) or i_gen==0: i_gen=None
            
            i_dob = request.form.get('dob')
            i_dod = request.form.get('dod')
            i_pob = request.form.get('PoB')
            i_cob = request.form.get('CoB')
            i_col = request.form.get('CoL')
            i_gender = request.form.get('gender')
            i_cluster= request.form.get('cluster')
            i_com= request.form.get('com')
            
            if request.form['submit_button'] == 'insert':
                backend.insert(i_id,   
                           i_name, 
                                                            i_surname,                                   
                                                            i_dob,
                                                            i_dod,
                                                            i_mother,
                                                            i_father,
                                                            i_spouse,                                   
                                                            i_gen,
                                                            i_cluster, 
                                                            i_gender,
                                                            i_pob,
                                                            i_cob,
                                                            i_col,
                                                            i_com)
                res=backend.view()
            
            elif request.form['submit_button'] == 'view':
                res=backend.view()
                # print (res)
                pass # do something else

            elif request.form['submit_button'] == 'draw':
                draw_tree()
                print(1)
                


                # print (res)
                pass            
            

            
            elif request.form['submit_button'] == 'update':
                backend.update(i_id,   
                           i_name, 
                                                            i_surname,                                   
                                                            i_dob,
                                                            i_dod,
                                                            i_mother,
                                                            i_father,
                                                            i_spouse,                                   
                                                            i_gen,
                                                            i_cluster, 
                                                            i_gender,
                                                            i_pob,
                                                            i_cob,
                                                            i_col,
                                                            i_com)
                res=backend.view()
                
                # print (res)
                pass # do something else
            
            else:
                pass # unknown


    return render_template("home.html", res=res, tbl='table.html', iid=iid, form=forma)

# Delete Article
# https://www.youtube.com/watch?v=Us9DuF4KWUE
@app.route('/delete_article/<string:id>', methods=['POST'])
def delete_article(id):
    backend.delete(id)

    # flash('Article Deleted', 'success')

    return redirect(url_for('index'))
    # return render_template("home.html")

@app.route('/')
def index(form=None):
    res=backend.view()
    if form is None:
        return render_template('home.html', res=res)
    else:
        return render_template('home.html' , form=form, res=res)

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/edit_item/<string:id>', methods=['GET', 'POST'])
def edit_item(id):
    form=backend.select(id)
    # print ("fffff",  form)
    # res=backend.view()
    return redirect(url_for('index', form=form))
    # return render_template('home.html' , form=form, res=res)


@app.route('/image/', methods=['GET', 'POST'])
def draw_tree():
    from PIL import ImageTk, Image as Image_PIL
    
    c_header=['id',   
            'name', 
            'surname',                                   
            'date_birth',
            'date_death',
            'mother_id',
            'father_id',
            'spouse_id',                                   
            'generation',
            'cluster', 
            'gender',
            'place_birth',
            'country_birth',
            'country',
            'comments'
             ]

    
    # Image
        
    import pydotplus as pdt
    import time
    # import pandas as pd

    df=pddf(backend.view(), columns=c_header)
    
    for c in ['id',   
            'mother_id',
            'father_id',
            'spouse_id',                                   
            'generation',
            'cluster', 
            'gender'       ]:
        df[c]=to_numeric(df[c], downcast='integer',errors='coerce')
        # df[c]=df[c].astype(int)
    
    
    
    
    # df=pd.read_excel('c:/a_tree/gen_tree.xlsx', sheet_name=nn)
    # print(df)
    
    min_level=int(df['generation'].min())
    max_level=int(df['generation'].max())
    
    g = pdt.Dot(graph_type='digraph', compound='true', rankdir='TB',newrank = 'true')
    
    i=0
    edges = []
    nodes=[]
    # create all edges
    
    
    
    #edges = [(1,2), (1,3), (2,4), (2,5), (3,5)]
    #nodes = [(1, "A", "r"), (2, "B", "g"), (3, "C", "g"), (4, "D", "r"), (5, "E", "g")]
    #for e in edges:
    #    g.add_edge(pdt.Edge(e[0], e[1], color=e[2]))
    #    
    #for n in nodes:
    #    node = pdt.Node(name=n[0], label= n[1], fillcolor=n[2], style="filled" )
    #    g.add_node(node)
    #    
    #    
    from ast import literal_eval as make_tuple
    nl=max_level-min_level+1
    s=[None]*(max_level+1)
    
    
    for i in range(min_level,max_level+1):
        s = pdt.Subgraph(i,rank='same')
        for j in df.loc[df['generation']==i, 'id'].values :
    #       s.add_node(pdt.Node(f"{df.loc[df['id']==j, 'Name'].values[0]} {df.loc[df['id']==j, 'Surname'].values[0]}"))
            s.add_node(pdt.Node(f"{df.loc[df['id']==j, 'id'].values[0]}"))
        g.add_subgraph(s)
    
    #min_cl=df['Cluster2'].min()
    #max_cl=df['Cluster2'].max()
    #nl=max_cl-min_cl+1
    #ss=[None]*(max_cl+1)
    #for i in range(min_cl,max_cl+1):
    #    if i>0:
    #        ss = pdt.Cluster(f'c2_{i}', color="blue",rankdir="TB")
    #        for j in df.loc[df['Cluster2']==i, 'id'].values :
    #    #       s.add_node(pdt.Node(f"{df.loc[df['id']==j, 'Name'].values[0]} {df.loc[df['id']==j, 'Surname'].values[0]}"))
    #            ss.add_node(pdt.Node(f"{df.loc[df['id']==j, 'id'].values[0]}"))
    #        g.add_subgraph(ss)
       
    
    min_cl=int(df['cluster'].min())
    max_cl=int(df['cluster'].max())
    nl=max_cl-min_cl+1
    ss=[None]*(max_cl+1)
    for i in range(min_cl,max_cl+1):
        ss = pdt.Cluster(f'c1_{i}', color="white",rankdir="TB")
        for j in df.loc[df['cluster']==i, 'id'].values :
    #       s.add_node(pdt.Node(f"{df.loc[df['id']==j, 'Name'].values[0]} {df.loc[df['id']==j, 'Surname'].values[0]}"))
            ss.add_node(pdt.Node(f"{df.loc[df['id']==j, 'id'].values[0]}"))
        g.add_subgraph(ss)
      
     
        
    for i in range(df.shape[0]):
        m=df.loc[i, 'mother_id']
        f=df.loc[i, 'father_id']
    #    if m in df['id'].values: edges.append((i,df.loc[df['id']==m, 'Name'].index[0],'orange'))
    #    if f in df['id'].values: edges.append((i,df.loc[df['id']==f, 'Name'].index[0],'blue'))  
    #    nodes.append((i, df.loc[i, 'Name'], 'blue'))
    
    
    #    nod=pdt.Node(f"{df.loc[i, 'id']}",label=f"{df.loc[i, 'Name']} {df.loc[i, 'Surname']}",  shape='record', color="blue", style='rounded')
        nod=pdt.Node(f"{df.loc[i, 'id']}",  shape='record', color="blue", style='rounded')
        if m in df['id'].values:        g.add_edge(pdt.Edge(pdt.Node(f"{df.loc[df['id']==m, 'id'].values[0]}"), nod, color='orange'))
        if f in df['id'].values:        g.add_edge(pdt.Edge(pdt.Node(f"{df.loc[df['id']==f, 'id'].values[0]}"), nod, color='#066dba'))
    
    
        if notnull(df.loc[i, 'spouse_id']):
    #         rel=df.loc[i, 'relation to']
    # #        tuple(map(int, re.findall(r'[0-9]+', rel)))
    #         rel=rel.replace('(','').replace(')','').split(',')
            # who=pd.to_numeric(rel[0]).astype(int)
            who=to_numeric(df.loc[i, 'spouse_id'], downcast='integer', errors='coerce')

            # how=rel[1]
    #        g.add_edge(pdt.Edge(pdt.Node(f"{df.loc[df['id']==who, 'Name'].values[0]} {df.loc[df['id']==who, 'Surname'].values[0]}"), nod,  dir='none',color='#bf3fbf')) #label='m',
            if who in df['id'].values:
                # print('yes')
                g.add_edge(pdt.Edge(pdt.Node(f"{df.loc[df['id']==who, 'id'].values[0]}"), nod,  dir='none',color='#bf3fbf')) #label='m',
    
    
    
    for i in  range(df.shape[0]):
        cc='orange'
        if df.loc[i, 'gender']==1: cc='#066dba'
        sstr=f"{df.loc[i, 'name']}"
        if notnull(df.loc[i, 'surname']): sstr=f"{sstr} {df.loc[i, 'surname']}"
        if notnull(df.loc[i, 'date_birth']): 
            if isinstance(df.loc[i, 'date_birth'], int) or isinstance(df.loc[i, 'date_birth'], str): 
                sstr=f"{sstr}\nB: {df.loc[i, 'date_birth']}"
            else: 
                sstr=f"{sstr}\nB: {df.loc[i, 'date_birth'].strftime('%d %b %Y') }" # %H:%M:%S
        
        d=df.loc[i, 'date_death']
        # import numpy as np
        if notnull(d): 
            # print("ddd" , isna(d), isnull(d), d, type(d) )
            sstr=f"{sstr}\nD: {d}"
        
        if notnull(df.loc[i, 'place_birth']): 
            sstr=f"{sstr}\nPoB: {df.loc[i, 'place_birth']} ({df.loc[i, 'country_birth']})"
        
        if not (isnull(df.loc[i, 'comments']) or df.loc[i, 'comments']==''): 
            sstr=f"{sstr}\nComments: {df.loc[i, 'comments']}"
                
        nod=pdt.Node(f"{df.loc[i, 'id']}", label=sstr, shape='box', color=cc, style='rounded')
    
    #    nod=pdt.Node(f"{df.loc[i, 'id']}", label=f"{df.loc[i, 'Name']} {df.loc[i, 'Surname']}\nB: {df.loc[i, 'DoB']}\nD: {df.loc[i, 'DoD']}\nPoB: {df.loc[i, 'Place of Birth']} ({df.loc[i, 'Country of Birth']})", shape='box', color=cc, style='rounded')
        g.add_node(nod)
    
    
    import io
    buf = io.BytesIO()
    g.write_png(buf)
    # plt.savefig(buf, format='png')
    buf.seek(0)
    
    import base64
    buf_img64 = base64.b64encode(buf.getvalue())
    # buf_im_str= u'data:img/jpeg;base64,'+buf_img64.decode('utf-8')
    
    buf_im_str=buf_img64.decode("utf-8")
    # img_g = Image_PIL.open(buf)
    
    # img=Img_IP(g.create_png())
    # img=g.create_png()
    
    # return send_file(buf, mimetype='image/PNG')

    # print (buf_img64)
    # return render_template('image.html' , img= buf_img64.decode('ascii'))


    return render_template('image.html' , img= buf_im_str)
    
# def pil2datauri(img):
#     #converts PIL image to datauri

#     data = io.BytesIO()
#     img.save(data, "JPEG")
#     data64 = base64.b64encode(data.getvalue())
#     return u'data:img/jpeg;base64,'+data64.decode('utf-8')
    
    
    # x='c:\\a_tree\\fTree_lyu.png'
    # img = Image_PIL.open(x)
    # img = img.resize((250, 250), Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(img_g, master=frame)

    
    


def draw_t():
    draw_tree()
    # print ("fffff",  form)
    # res=backend.view()
    # return redirect(url_for('index'))



    
if __name__ == "__main__":
    app.run(debug=True)