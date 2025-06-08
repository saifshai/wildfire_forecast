import geopandas as gpd

def download_wildfire_fuel_types():
    """Download BC wildfire fire fuel types geospatial data"""
    
    # Build the complete WFS URL
    base_url = "https://openmaps.gov.bc.ca/geo/pub/ows"
    params = {
        "service": "WFS",
        "version": "2.0.0",
        "request": "GetFeature", 
        "typeName": "pub:WHSE_LAND_AND_NATURAL_RESOURCE.PROT_FUEL_TYPE_SP",
        "outputFormat": "application/json"
    }
    
    # Create full URL
    param_string = "&".join([f"{k}={v}" for k, v in params.items()])
    full_url = f"{base_url}?{param_string}"
    
    print("Downloading BC wildfire fuel types data...")
    print(f"URL: {full_url}")
    
    # Download the data
    gdf = gpd.read_file(full_url)
    
    print(f"Downloaded {len(gdf)} features")
    print(f"Columns: {list(gdf.columns)}")
    print(f"CRS: {gdf.crs}")
    print(f"Bounds: {gdf.total_bounds}")
    
    # Convert geometry to WKT for CSV compatibility
    df = gdf.copy()
    df['geometry_wkt'] = df['geometry'].to_wkt()
    df = df.drop(columns=['geometry'])
    
    # Save as CSV
    output_file = "bc_wildfire_fuel_types.csv"
    df.to_csv(output_file, index=False)
    print(f"Saved to: {output_file} (CSV format with geometry as WKT)")
    
    return gdf

if __name__ == "__main__":
    gdf = download_wildfire_fuel_types() 