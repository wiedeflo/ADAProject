'''
File name: areas_handler.py
Date created: 15/12/2019
Date last modified: 17/12/2019
Python Version: 3.7.4
Handles the interactive "per capita income with respect to household incomes of areas" plot. Also contains dictionaries of region-to-color name-to-region used for this plot.
'''

import plotly
import plotly.express as px
import plotly.graph_objs as go

def interactive_plot_capita_income_wrt_households(socio_life_merged_DF):
    ''' 
    Get the plotly interactive plot of per capita income with respect to household incomes of areas
    :param socio_life_merged_DF: pd.DataFrame
    :return: plotly interactive plot
    '''
    # Make plot
    f = go.FigureWidget([go.Scatter(
        x=socio_life_merged_DF['housholds_below_poverty_perc'],
        y=socio_life_merged_DF['per_capita_income'], 
        hovertext=socio_life_merged_DF['community_area_name'].apply(lambda name: name.title()),
        hoverinfo="text",
        mode='markers',
        marker_color=socio_life_merged_DF['region'].apply(lambda reg: region_to_color[reg]),
    )])

    # Specify layout and titles
    f.update_layout(
        autosize=False,
        width=1000,
        height=700,
        xaxis_title="percentage of households below poverty",
        yaxis_title="per capita income",
        title=go.layout.Title(text="Community area per capita income with respect to households below poverty"),
    )

    # On-click interaction
    scatter = f.data[0]
    scatter.marker.size = [10] * 100

    all_regions = socio_life_merged_DF['community_area_name'].values

    # create callback function
    def update_point(trace, points, selector):
        ''' 
        On click of an area : increase the size of dots of areas of same region and decrease the size of the others
        '''
        x, y = points.xs[0], points.ys[0]

        area, region = socio_life_merged_DF[(socio_life_merged_DF['per_capita_income'] == y) & \
                                  (socio_life_merged_DF['housholds_below_poverty_perc'] == x)]\
        [['community_area_name', 'region']].values[0]

        c = list(scatter.marker.color)
        s = list(scatter.marker.size)

        same_region = socio_life_merged_DF[socio_life_merged_DF['region'] == region]['community_area_name'].values
        
        # Make areas of same region bigger and others smaller
        for area in all_regions:
            if area in same_region:
                idx = name_to_idx[area]
                c[idx] = c[idx]
                s[idx] = 20
            else:
                idx = name_to_idx[area]
                c[idx] = c[idx]
                s[idx] = 6

        with f.batch_update():
            scatter.marker.color = c
            scatter.marker.size = s
    
    # Add on-click interactivity
    scatter.on_click(update_point)

    return f

region_to_color = {
    'all': 'rgb(0, 0, 0)',
    'central': 'rgb(127, 0, 0)',
    'far north side': 'rgb(0, 127, 0)',
    'northwest side': 'rgb(0, 0, 127)',
    'north side': 'rgb(127, 0, 127)',
    'west side': 'rgb(0, 127, 127)',
    'south side': 'rgb(127, 127, 0)',
    'southwest side': 'rgb(255, 127, 0)',
    'far southeast side': 'rgb(255, 0, 127)',
    'far southwest side': 'rgb(255, 127, 127)'
}

name_to_idx = {
    'north center': 4,
    'lake view': 5,
    'lincoln park': 6,
    'near north side': 7,
    'loop': 31,
    'near south side': 32,
    'forest glen': 11,
    'beverly': 71,
    'edison park': 8,
    'mount greenwood': 73,
    'norwood park': 9,
    'jefferson park': 10,
    'garfield ridge': 55,
    'clearing': 63,
    'calumet heights': 47,
    'lincoln square': 3,
    'dunning': 16,
    'ashburn': 69,
    'portage park': 14,
    'morgan park': 74,
    'irving park': 15,
    'north park': 12,
    'west town': 23,
    'near west side': 27,
    'hyde park': 40,
    'edgewater': 76,
    'logan square': 21,
    'hegewisch': 54,
    'west ridge': 1,
    'avalon park': 44,
    "o'hare": 75,
    'montclaire': 17,
    'avondale': 20,
    'west lawn': 64,
    'west elsdon': 61,
    'archer heights': 56,
    'bridgeport': 59,
    'washington height': 72,
    'albany park': 13,
    'mckinley park': 58,
    'east side': 51,
    'roseland': 48,
    'belmont cragin': 18,
    'chicago': 77,
    'kenwood': 38,
    'uptown': 2,
    'rogers park': 0,
    'pullman': 49,
    'hermosa': 19,
    'brighton park': 57,
    'gage park': 62,
    'west pullman': 52,
    'lower west side': 30,
    'chatham': 43,
    'grand boulevard': 37,
    'douglas': 34,
    'auburn gresham': 70,
    'chicago lawn': 65,
    'austin': 24,
    'south deering': 50,
    'new city': 60,
    'south chicago': 45,
    'greater grand crossing': 68,
    'south shore': 42,
    'woodlawn': 41,
    'burnside': 46,
    'south lawndale': 29,
    'west englewood': 66,
    'humboldt park': 22,
    'oakland': 35,
    'armour square': 33,
    'washington park': 39,
    'east garfield park': 26,
    'west garfield park': 25,
    'north lawndale': 28,
    'englewood': 67,
    'fuller park': 36,
    'riverdale': 53
}

# https://en.wikipedia.org/wiki/Chicago#/media/File:Chicago_community_areas_map.svg
name_to_region = {
    'ohare': 'far north side',
    "o'hare": 'far north side',
    'jefferson park': 'far north side',
    'forest glen': 'far north side',
    'norwood park': 'far north side',
    'edison park': 'far north side',
    'north park': 'far north side',
    'albany park': 'far north side',
    'rogers park': 'far north side', 
    'lincoln square': 'far north side',
    'edgewater': 'far north side',
    'uptown': 'far north side',
    'west ridge': 'far north side',
    
    
    'dunning': 'northwest side',
    'portage park': 'northwest side',
    'irving park': 'northwest side',
    'belmont cragin': 'northwest side',
    'hermosa': 'northwest side',
    'montclaire': 'northwest side',
    'montclare': 'northwest side',
    
    
    'lincoln park': 'north side',
    'lake view': 'north side',
    'north center': 'north side',
    'avondale': 'north side',
    'logan square': 'north side',
    
    
    'humboldt park': 'west side',
    'west town': 'west side',
    'austin': 'west side',
    'west garfield park': 'west side', 
    'east garfield park': 'west side', 
    'near west side': 'west side',
    'north lawndale': 'west side',  
    'south lawndale': 'west side', 
    'lower west side': 'west side',
    
    
    'near north side': 'central',
    'near south side': 'central',
    'loop': 'central',
    
    
    'garfield ridge': 'southwest side',
    'clearing': 'southwest side',
    'new city': 'southwest side', 
    'west elsdon': 'southwest side',
    'mckinley park': 'southwest side', 
    'west lawn': 'southwest side', 
    'chicago lawn': 'southwest side', 
    'west englewood': 'southwest side', 
    'englewood': 'southwest side',
    'gage park': 'southwest side', 
    'archer heights': 'southwest side', 
    'brighton park': 'southwest side',
    
    
    'washington park': 'south side',
    'hyde park': 'south side',
    'woodlawn': 'south side',
    'douglas': 'south side',
    'grand boulevard': 'south side',
    'kenwood': 'south side',
    'greater grand crossing': 'south side',
    'armour square': 'south side',
    'bridgeport': 'south side',
    'south shore': 'south side',
    'oakland': 'south side',
    'fuller park': 'south side',
    
    
    'ashburn': 'far southwest side',       
    'auburn gresham': 'far southwest side',
    'beverly': 'far southwest side',
    'washington heights': 'far southwest side',
    'washington height': 'far southwest side',
    'mount greenwood': 'far southwest side',
    'morgan park': 'far southwest side',
    
    
    'chatham': 'far southeast side', 
    'avalon park': 'far southeast side',
    'south chicago': 'far southeast side', 
    'burnside': 'far southeast side', 
    'calumet heights': 'far southeast side',
    'roseland': 'far southeast side',
    'pullman': 'far southeast side',
    'south deering': 'far southeast side',
    'east side': 'far southeast side',
    'west pullman': 'far southeast side',
    'riverdale': 'far southeast side',
    'hegewisch': 'far southeast side',  
    
    'chicago': 'all'
}