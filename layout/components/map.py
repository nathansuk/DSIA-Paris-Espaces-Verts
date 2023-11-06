from dash import html
import os


def create_iframe_map():
    """
    Create an Iframe containing the map of all green areas polygons
    :return: the Iframe component
    """
    current_dir = os.path.dirname(__file__)
    map_path = os.path.join(current_dir, '../../carte.html')
    return html.Iframe(id='map', srcDoc=open(map_path, 'r').read(), width='100%', height='500', className='flex-item graph5')