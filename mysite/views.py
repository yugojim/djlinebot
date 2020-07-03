from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from trips.models import Book, Author, BookInstance, Genre,Post,Choice,predict
from trips.apps import TripsConfig

def index(request):
    datalist=[]
    #print(request.method)
    #reg1=TripsConfig.reg1
    if 'HEIGHT_NM' in request.POST:
        HEIGHT_NM = request.POST['HEIGHT_NM']
        WEIGHT_NM = request.POST['WEIGHT_NM']
        GCSE_NM = request.POST['GCSE_NM']
        GCSV_NM = request.POST['GCSV_NM']
        GCSM_NM = request.POST['GCSM_NM']
        SBP_NM = request.POST['SBP_NM']
        DBP_NM =request.POST['DBP_NM']
        BT_NM = request.POST['BT_NM']
        HR_NM = request.POST['HR_NM']
        RR_NM = request.POST['RR_NM']    
        SumNihssIn = request.POST['SumNihssIn']
        x=[[HEIGHT_NM,WEIGHT_NM,GCSE_NM,GCSV_NM,GCSM_NM,
           SBP_NM,DBP_NM,BT_NM,HR_NM,RR_NM,SumNihssIn]]
        '''
        Post.objects.create(title=HEIGHT_NM,
                            content=WEIGHT_NM,
                            photo=GCSE_NM,
                            location=GCSV_NM,
                            created_at=datetime.datetime.now())
        '''
        #datalist='data record'
        #datalist=reg1.predict(x)
        #datalist1=reg11.predict(x)
        #print(datalist)
    context = {'datalist': datalist ,
                   }
    return render(request, 'index.html', context)

def baseform(request):
    data = predict.objects.order_by('-predict_date').all()
    datacount = predict.objects.all().count()
    context = {
        'data' : data,
        'datacount' : datacount
    }
    return render(request, 'base.html', context )


def baseindex(request):
    from plotly.offline import plot
    from plotly.graph_objs import Scatter
    import plotly.graph_objs as go
    import pandas as pd
   
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['AAPL.Open'],
                    high=df['AAPL.High'],
                    low=df['AAPL.Low'],
                    close=df['AAPL.Close'])])
    fig.update_layout(
        autosize=False,
        width=500,
        height=500,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
        paper_bgcolor="LightSteelBlue",
    )
    plot_div = plot(fig, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

    import plotly.figure_factory as ff
    table_data = [['Team', 'Wins', 'Losses', 'Ties'],
                  ['Montréal<br>Canadiens', 18, 4, 0],
                  ['Dallas Stars', 18, 5, 0],
                  ['NY Rangers', 16, 5, 0],
                  ['Boston<br>Bruins', 13, 8, 0],
                  ['Chicago<br>Blackhawks', 13, 8, 0],
                  ['LA Kings', 13, 8, 0],
                  ['Ottawa<br>Senators', 12, 5, 0]]
    
    fig = ff.create_table(table_data, height_constant=60)
    
    teams = ['Montréal Canadiens', 'Dallas Stars', 'NY Rangers',
             'Boston Bruins', 'Chicago Blackhawks', 'LA Kings', 'Ottawa Senators']
    GFPG = [3.54, 3.48, 3.0, 3.27, 2.83, 2.45, 3.18]
    GAPG = [2.17, 2.57, 2.0, 2.91, 2.57, 2.14, 2.77]
    
    trace1 = go.Scatter(x=teams, y=GFPG,
                        marker=dict(color='#0099ff'),
                        name='Goals For<br>Per Game',
                        xaxis='x2', yaxis='y2')
    trace2 = go.Scatter(x=teams, y=GAPG,
                        marker=dict(color='#404040'),
                        name='Goals Against<br>Per Game',
                        xaxis='x2', yaxis='y2')
    
    fig.add_traces([trace1, trace2])
    
    # initialize xaxis2 and yaxis2
    fig['layout']['xaxis2'] = {}
    fig['layout']['yaxis2'] = {}
    
    # Edit layout for subplots
    fig.layout.xaxis.update({'domain': [0, .5]})
    fig.layout.xaxis2.update({'domain': [0.6, 1.]})
    
    # The graph's yaxis MUST BE anchored to the graph's xaxis
    fig.layout.yaxis2.update({'anchor': 'x2'})
    fig.layout.yaxis2.update({'title': 'Goals'})
    
    # Update the margins to add a title and see graph x-labels.
    fig.layout.margin.update({'t':50, 'b':100})
    fig.layout.update({'title': '2016 Hockey Stats'})
    plot_div1 = plot(fig, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

    latest_question_list = Post.objects.order_by('-created_at')[:5]
    
    context = {'latest_question_list': latest_question_list,
               'plot_div': plot_div,
               'plot_div1': plot_div1,
               'plot_div2': plot_div}
    return render(request, 'indexOLD.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Post, pk=question_id)
    return render(request, 'results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Post, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))