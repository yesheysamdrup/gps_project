import geopandas as gpd
import sys as die
#from .logs import die
#Path
STATIC_DIR = "C:/Users/Ysam/OneDrive - NOVAIMS/Desktop/gpsProject/data"

def read_shp(
    fname: str
    )-> gpd.GeoDataFrame:

    try: 
        gdf=gpd.read_file(fname)
    except Exception as e:
        die(f"read_shp:{e}")
       
    return gdf
         
    gdf = e.read_shp(f"{STATIC_DIR}/PlotA.shp")
    
