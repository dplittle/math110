import streamlit as st
import numpy as np
import pandas as pd
import math
import random
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import FormatStrFormatter

st.set_page_config(
    page_title="Modeling Data Using Linear Functions",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
    # initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

# Load data
data = pd.read_csv("life-expectancy_US_Worlds.csv",
                   index_col=0).drop(columns=['World'])


def linear_function(x, m, b):
    return m * x + b


def plot_data(slope: float, intercept: float):
    x = np.linspace(0, 150, 150)
    y = linear_function(x, slope, intercept)
    # fig = plt.figure(figsize=(8, 6))

    DP = 2

    fig = plt.figure(figsize=(8, 6), dpi=100, facecolor='w', edgecolor='k')
    fig.canvas.draw()
    ax = plt.gca()

    # set up axis
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # draw curve
    ax.plot(x, y)

    # line, = ax.plot(x, y)
    ax.scatter(range(1, len(y_data) + 1), y_data, c=["red"], s=2)

    # mark point
    # ax.plot(x[129], y[129] , 'ro')

    # set bounds
    ax.set_xbound(0, 150)
    ax.set_ybound(0, 100)

    # format axes and grid
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.xaxis.grid(True, 'major', linewidth=2 / DP, linestyle='-', color='#d7d7d7', zorder=0)
    ax.yaxis.grid(True, 'major', linewidth=2 / DP, linestyle='-', color='#d7d7d7')

    ax.xaxis.set_minor_locator(MultipleLocator(2))
    ax.yaxis.set_minor_locator(MultipleLocator(2))
    ax.xaxis.grid(True, 'minor', linewidth=0.5 / DP, linestyle='-', color='#d7d7d7')
    ax.yaxis.grid(True, 'minor', linewidth=0.5 / DP, linestyle='-', color='#d7d7d7')

    ax.set_axisbelow(True)
    ax.set_aspect('equal')

    # plt.show(fig)

    # plt.plot(x, y)
    #
    # plt.xlim(0, 122)
    # plt.ylim(0, 100)
    # plt.xlabel('x')
    # plt.ylabel('y')

    st.pyplot(fig)


"""
## Modeling data with linear functions

The graph below shows average US life expectancy for every year between 1901
and 2021 (the red dots). The $x$-axis corresponds to year $1900+x$.

Looking at the red dots, you notice that they **follow a linear trend**: with
a few exceptions, the points closely follow a straight line. 

(What are the exceptions (*outliers*) and how would you explain them? In other
words, what happened in the US in 1918 and in 2020-21 that had a negative
impact on life expectancy?)

__*Use the sliders to match the blue line with the red dots as
   closely as possible.*__
"""

col1, col2 = st.columns(2, gap="large")

with col1:
    # ed_data = st.data_editor(data)

    x_data = data.index[:].to_list()
    y_data = data.iloc[0:, 0].to_list()

    slider_col1, slider_col2 = st.columns([0.4, 0.6], gap='medium')

    with slider_col1:
        user_slope = st.slider('Slope', 0.15, 0.55, 0.15)

    with slider_col2:
        user_intercept = st.slider('Intercept', 40, 65, 40)

    plot_data(user_slope, user_intercept)

with col2:
    tab1, tab2, tab3 = st.tabs(
        ["**Interpreting the model**", "**Applying the model**", "**Food for thought**"])

    # """
    # ### Interpreting the model $y=m \cdot x+b$
    # """

    with tab1:

        """The blue line represents a linear function, determined by its **slope** and its **y-intercept**, 
        that **models the data**."""

        st.write(
            f"Your model: $${str(round(user_slope, 2))} \cdot x + {str(user_intercept)}$$")

        """Mathematically, the model is simply a linear function defined by slope and intercept. But since it is 
        supposed to model data, slope and intercept have practical interpretations. Answer the questions below to 
        test your understanding."""

        #
        # Interpret intersect
        #
        """
        **What does the $y$-intercept of the line above represent in this context?**
        """
        intercept_quiz = st.radio(
            "Answer choices",
            ('The average $x$-life expectancy (in years) of a US citizen in the year 0',
             'The average life expectancy (in years) of a US citizen in the year 1900',
             'The number of US citizens in 1900 (in millions)',
             'The number of US citizens 56 or older in 1900 (in millions)'
             ),
            0,
            label_visibility="collapsed")

        if st.button('Submit', key='sub_1_1'):

            if intercept_quiz == \
                    'The average life expectancy (in years) of a US citizen in the year 1900':

                st.write('Correct!')
            else:
                st.write("Sorry, please try again.")

        #
        # Interpret slope
        #
        """
        **Which of the following statements about the slope of the model function is true?**
        """
        slope_quiz = st.radio(
            "Answer choices",
            ('Every twenty years, US life expectancy increases by $m$ years.',
             'Every year, the total US population grows by $m$ million people.',
             'Every year, US life expectancy increases by $m$ years.',
             'Every twenty years, the number of US citizens older than 50 increases by $m$ million people.'
             ),
            0,
            label_visibility="collapsed")

        if st.button('Submit', key='sub_1_2'):

            if slope_quiz == \
                    'Every year, the total US population grows by $m$ million people.':
                st.write('Correct!')
            else:
                st.write("Sorry, please try again.")

    # """
    # ### Applying the model
    # """
    with tab2:

        # """
        # We want to use our model to make predictions about the future average life expectancy of the US population.
        # """
        st.write(
            f"We want to use our model \
            $${str(round(user_slope, 2))} \cdot x + {str(user_intercept)}$$ \
            to make predictions about the future average life expectancy of the US population.")

        """
        #### Estimating future life expectancy
        
        For example, we would like to estimate the average life expectancy in 2030.
        For this purpose, we use the value of our model at $x=130$
        (keep in mind that $x=0$ corresponds to the year 1900).
        
        You can compute this value or try to read it off the graph. 
        """

        with st.expander("Estimated US life expectancy in 2030:"):
            st.write(str(round(linear_function(130, user_slope, user_intercept), 2)) + " years")

        """
        **According to the model, what is the estimated US life expectancy in 2040?**
        """
        slope_quiz = st.radio(
            "Answer choices",
            ('140.0',
             f'{round(140 * user_slope + user_intercept + 15, 2)}',
             f'{round(140 * user_slope + user_intercept - 5, 2)}',
             f'{round(140 * user_slope + user_intercept, 2)}'),
            0,
            label_visibility="collapsed")

        if st.button('Submit', key='sub_2_1'):

            if slope_quiz == \
                    f'{round(140 * user_slope + user_intercept, 2)}':
                st.write('Correct!')
            else:
                st.write("Sorry, please try again.")


        f"""
        #### Estimating life expectancy milestones 

Similarly, we can use the model to approximate when life expectancy crosses a 
certain threshold. For example, to estimate how long it will take life expectancy 
to reach 80 years, we have to find $x$ for which the model assumes the value $80$. 

**In the graph**, that corresponds to finding the $x$ at which the line intersection 
the horizontal line at $y=80$.

**Algebraically**, it means solving $80 = {str(round(user_slope,2))} x + {str(user_intercept)}$, which yields $x \\approx {str(round((80-user_intercept)/user_slope,2))}$ 
In other words, your linear model estimates that US life expectancy first reaches 
80 years in the year {str(math.floor((80-user_intercept)/user_slope)+1900)}. Check this on the graph on the left.
        """

        # new_button_2_2 = st.button('New Version', key='new_2_2')
        #
        # if new_button_2_2:
        #     target_age = random.choice([95,100,105,110,120,130])
        # else:
        #     target_age = 90

        target_age = 90
        
        f"""
        **According to the model, when does US life expectancy reach {target_age} years?**
        """

        estimate_quiz_2 = st.radio(
            "Answer choices",
            (f'{math.floor((target_age - user_intercept) / user_slope) + 1900}',
             f'{math.floor((target_age - 10 - user_intercept) / user_slope) + 1900}',
             f'{math.floor((target_age - 15 - user_intercept) / user_slope) + 1900}',
             f'{math.floor(target_age * user_slope + 1900)}'
             ),
            0,
            label_visibility="collapsed")

        if st.button('Submit', key='sub_2_2'):

            if estimate_quiz_2 == \
                    f'{math.floor((target_age - user_intercept) / user_slope) + 1900}':

                st.write('Correct!')
            else:
                st.write("Sorry, please try again.")

    with tab3:
        """
        Compute the estimated life expectancy in 2300. Does the model still make sense so far out?
        """
